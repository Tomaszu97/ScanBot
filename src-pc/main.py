#!/usr/bin/python3
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from layout.layout import Ui_MainWindow
from pyside_material import apply_stylesheet
import serial.tools.list_ports
import serial
import datetime
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np
from math import radians, degrees, sin, cos
import time
from robot import *
from timer_emiter import *
from statistics import median
from strings import *
import randomcolor 

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.robot = Robot(self.send_command)

        QMainWindow.__init__(self)
        #apply_stylesheet(app, theme="dark_blue.xml")
        self.setFixedWidth(1150)
        self.setFixedHeight(650)

        # 2D graph
        self.setupUi(self)
        self.plot_2d = pg.PlotWidget()
        self.plot_2d.setXRange(-300,300)
        self.plot_2d.setYRange(-300,300)
        self.plot_2d.showGrid(x = True, y = True, alpha = 0.3)      
        self.grid_2d_layout.addWidget(self.plot_2d)

        # 3D graph
        self.plot_3d = gl.GLViewWidget()
        self.plot_3d.setCameraPosition(distance=10)
        gr = gl.GLGridItem()
        self.plot_3d.addItem(gr)
        # md = gl.MeshData.sphere(rows=4, cols=9)
        # m = gl.GLMeshItem(
        #     meshdata=md, smooth=False, drawFaces=False, drawEdges=True, edgeColor=(1, 0, 1, 1)
        # )
        # self.plot_3d.addItem(m)
        self.grid_3d_layout.addWidget(self.plot_3d)

        # Magnetometer calibration graph
        self.plot_3d_mag = gl.GLViewWidget()
        self.reset_mag_plot()
        # sp1 = gl.GLScatterPlotItem(pos=np.array( (0,0,0) ), color=np.array( (1,1,0,0.7) ))
        # self.plot_3d_mag.addItem(sp1)
        self.grid_mag_cal_layout.addWidget(self.plot_3d_mag)

        # Workers ##WARNING## use one worker for one task ##WARNING##
        self.calibration_timer = TimerEmiter(interval=0.2, repeat_count=50)

        # Controls' handlers
        self.connect_signals()

        # Other
        self.randcol = lambda : randomcolor.RandomColor().generate(luminosity='bright', count=1)
        self.poles = np.zeros((0,2))
        self.poles_colors = []
        self.mag_cal_points = np.zeros((0,3))
        self.mag_cal_points_colors = []

    def closeEvent(self, event):
        try:
            self.ser.close()
        except AttributeError:
            pass

    def make_message(self, title, text, informativetext=None):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle(title)
        msg.setText(text)
        if informativetext is not None:
            msg.setInformativeText(informativetext)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    def connect_signals(self):
        self.serial_refresh_btn.clicked.connect(self.serial_refresh)
        self.serial_connect_btn.clicked.connect(self.serial_connect)
        self.forward_btn.pressed.connect(lambda : self.robot.drive(90,90))
        self.forward_btn.released.connect(lambda : self.robot.drive(0,0))
        self.backward_btn.pressed.connect(lambda : self.robot.drive(-90,-90))
        self.backward_btn.released.connect(lambda : self.robot.drive(0,0))
        self.turn_left_btn.pressed.connect(lambda : self.robot.drive(-90,90))
        self.turn_left_btn.released.connect(lambda : self.robot.drive(0,0))
        self.turn_right_btn.pressed.connect(lambda : self.robot.drive(90,-90))
        self.turn_right_btn.released.connect(lambda : self.robot.drive(0,0))
        self.tower_slider.valueChanged.connect(lambda val: self.robot.rotate_tower(val))
        self.get_distance_btn.clicked.connect(lambda: self.robot.get_distance())
        self.get_azimuth_btn.clicked.connect(lambda: self.robot.get_azimuth())
        self.beep_btn.clicked.connect(lambda: self.robot.beep(30,3))
        self.print_duck_btn.clicked.connect(lambda: self.robot.print(duckstr))
        self.kill_btn.clicked.connect(self.robot.kill)
        self.get_mag_btn.clicked.connect(self.robot.get_mag)
        self.get_mag_cal_btn.clicked.connect(self.robot.get_mag_cal)
        self.send_btn.clicked.connect(lambda: self.send_command(self.command_input.text()) )
        self.scan_btn.clicked.connect(self.scan)
        self.forward_step_btn.clicked.connect(lambda : self.robot.move(self.drive_step_slider.value()))
        self.backward_step_btn.clicked.connect(lambda : self.robot.move(-self.drive_step_slider.value()))
        self.turn_left_step_btn.clicked.connect(lambda : self.robot.rotate(-self.rotate_step_slider.value()))
        self.turn_right_step_btn.clicked.connect(lambda : self.robot.rotate(self.rotate_step_slider.value()))
        self.rotate_to_btn.clicked.connect(lambda : self.robot.rotate_to(self.rotate_to_slider.value()))
        self.clear_buffer_btn.clicked.connect(self.flush_serial_buffer)
        self.measure_btn.clicked.connect(self.calibration_timer.start)
        self.mag_cal_reset_btn.clicked.connect(self.reset_mag_cal)
        self.calibration_timer.tick_signal.connect(self.measure_handler)
        self.calibration_timer.tick_signal.connect(lambda val: self.calibration_progbar.setValue(val))

    def serial_refresh(self):
        self.serial_combo.clear()
        for comport in serial.tools.list_ports.comports():
            device = comport.device
            self.serial_combo.addItem(str(device))

    def serial_connect(self):
        if self.connection_status_label.text == "✔":
            self.ser.close()

        self.connection_status_label.setText("⌚")
        try:
            self.ser = serial.Serial(
                port=f"{self.serial_combo.currentText()}",
                baudrate=38400,
                timeout=2,
                parity=serial.PARITY_NONE,
                rtscts=0,
            )
            
            self.connection_status_label.setText("✔")
        except serial.SerialException as e:
            self.connection_status_label.setText("❌")
            self.make_message("Error", "Serial connection failed.", str(e))

        x = self.ser.read_until().decode()
        toprint = f'[{datetime.datetime.now().strftime("%H:%M:%S")}] RECEIVED> {x}'
        self.command_output_long.setText(self.command_output_long.toPlainText() + toprint)
        self.command_output_short.setText(self.command_output_short.toPlainText() + toprint)

    def flush_serial_buffer(self):
        self.command_output_long.setText("")
        self.command_output_short.setText("")
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()

    def scroll_outputs(self):
        sb=self.command_output_long.verticalScrollBar()
        sb.setValue(sb.maximum())
        sb=self.command_output_short.verticalScrollBar()
        sb.setValue(sb.maximum())

    def read_until(self, terminator='\n'):
        data = ""
        while True:
            char = self.ser.recv(1).decode("ASCII")
            data += char
            if char == terminator:
                break
        return data

    def send(self, data):
        self.ser.write(data)

    def send_command(self, command):
        self.send(command.encode('ASCII'))
        toprint = f'[{datetime.datetime.now().strftime("%H:%M:%S")}] SENT> {command}\r\n'
        self.command_output_long.setText(self.command_output_long.toPlainText() + toprint)
        self.command_output_short.setText(self.command_output_short.toPlainText() + toprint)
        self.scroll_outputs()
        
        x = self.ser.read_until().decode()
        toprint = f'[{datetime.datetime.now().strftime("%H:%M:%S")}] RECEIVED> {x}'
        self.command_output_long.setText(self.command_output_long.toPlainText() + toprint)
        self.command_output_short.setText(self.command_output_short.toPlainText() + toprint)

        self.scroll_outputs()
        x = x.replace("\r\n", "")
        return x

    def place_pole(self, distance, _angle, color="#FF00FF"):
        angle = _angle - self.robot.azimuth 
        angle = radians(angle)
        x = distance * cos(angle) + self.robot.position[0]
        y = distance * sin(angle) + self.robot.position[1]
        self.poles = np.append(self.poles, np.array([[x,y]]), axis=0)
        self.poles_colors.append(color)
       
    def redraw_poles(self):
        self.plot_2d.clear()
        poles = pg.ScatterPlotItem(self.poles[:,0], self.poles[:,1], pen="#FF00FF", symbol='+') # TODO handle separate colors for each point
        self.plot_2d.addItem(poles)

        # TODO rethink this
        linedata = np.zeros((0,2))
        for pole in self.poles:
            linedata = np.append(linedata, np.array([[0,0]]), axis=0)
            linedata = np.append(linedata, np.array([[pole[0],pole[1]]]), axis=0)
            #self.plot_2d.plot((0,pole[0]), (0, pole[1]), symbol=None) 
        lines = pg.PlotCurveItem(x=linedata[:,0], y=linedata[:,1], connect="pairs")
        self.plot_2d.addItem(lines)
        ###

    def scan(self):
        data = self.robot.scan()
        for idx, dist in enumerate(data):
            if dist >= 15:
                ang = 1*idx
                self.place_pole(dist, ang)
        self.redraw_poles()
                
    def measure_handler(self):
        x,y,z = [],[],[]
        for i in range(3):
            _x, _y, _z = self.robot.get_mag()
            x.append(_x)
            y.append(_y)
            z.append(_z)
        x = median(x)
        y = median(y)
        z = median(z)
        
        if x < int(self.min_x_label.text()):
            self.min_x_label.setText(str(x))
        if x > int(self.max_x_label.text()):
            self.max_x_label.setText(str(x))
        if y < int(self.min_y_label.text()):
            self.min_y_label.setText(str(y))
        if y > int(self.max_y_label.text()):
            self.max_y_label.setText(str(y))
        if z < int(self.min_z_label.text()):
            self.min_z_label.setText(str(z))
        if z > int(self.max_z_label.text()):
            self.max_z_label.setText(str(z))

        self.offset_x_label.setText( str( int((int(self.min_x_label.text()) + int(self.max_x_label.text()))/2)) )
        self.offset_y_label.setText( str( int((int(self.min_y_label.text()) + int(self.max_y_label.text()))/2)) )
        self.offset_z_label.setText( str( int((int(self.min_z_label.text()) + int(self.max_z_label.text()))/2)) )

        self.mag_cal_points = np.append(self.mag_cal_points, np.array([[x,y,z]]), axis=0)
        self.reset_mag_plot()
        item = gl.GLScatterPlotItem( pos=self.mag_cal_points, color=(1,1,0,0.7), size=5 )
        self.plot_3d_mag.addItem(item) 

    def reset_mag_plot(self):
        self.plot_3d_mag.clear()
        self.plot_3d_mag.setCameraPosition(pos=pg.Vector(0,0,0), distance=40000, azimuth=45, elevation=30)
        gr1 = gl.GLGridItem(color=(255,0,0,76.5))
        gr1.setSize(10000, 10000, 10000)
        gr1.setSpacing(1000,1000,1000)
        gr2 = gl.GLGridItem(color=(0,255,0,76.5))
        gr2.setSize(10000, 10000, 10000)
        gr2.setSpacing(1000,1000,1000)
        gr2.rotate(90,1,0,0)
        gr3 = gl.GLGridItem(color=(0,0,255,76.5))
        gr3.setSize(10000, 10000, 10000)
        gr3.setSpacing(1000,1000,1000)
        gr3.rotate(90,0,1,0)
        self.plot_3d_mag.addItem(gr1)
        self.plot_3d_mag.addItem(gr2)
        self.plot_3d_mag.addItem(gr3)

    def reset_mag_cal(self):
        self.min_x_label.setText(str(0))
        self.max_x_label.setText(str(0))
        self.offset_x_label.setText(str(0))
        self.min_y_label.setText(str(0))
        self.max_y_label.setText(str(0))
        self.offset_y_label.setText(str(0))
        self.min_z_label.setText(str(0))
        self.max_z_label.setText(str(0))
        self.offset_z_label.setText(str(0))
        self.reset_mag_plot() 
        self.mag_cal_points_colors = []
        self.mag_cal_points = np.zeros((0,3)) 

        # TODO: Delete this, its only temporary
        self.mag_autocal()

    def mag_autocal(self):
        for i in range(10):
            self.robot.drive(90,-90)
            sleep(0.5)
            self.robot.stop()
            sleep(0.2)
            self.measure_handler()
            
if __name__ == "__main__":

    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
