# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1150, 680)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.serial_refresh_btn = QPushButton(self.centralwidget)
        self.serial_refresh_btn.setObjectName(u"serial_refresh_btn")
        self.serial_refresh_btn.setGeometry(QRect(150, 40, 101, 31))
        self.serial_combo = QComboBox(self.centralwidget)
        self.serial_combo.setObjectName(u"serial_combo")
        self.serial_combo.setGeometry(QRect(10, 41, 131, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 101, 20))
        self.serial_connect_btn = QPushButton(self.centralwidget)
        self.serial_connect_btn.setObjectName(u"serial_connect_btn")
        self.serial_connect_btn.setGeometry(QRect(260, 40, 101, 31))
        self.command_output_short = QTextBrowser(self.centralwidget)
        self.command_output_short.setObjectName(u"command_output_short")
        self.command_output_short.setGeometry(QRect(10, 570, 441, 71))
        self.command_output_short.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 500, 101, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 550, 101, 20))
        self.forward_btn = QPushButton(self.centralwidget)
        self.forward_btn.setObjectName(u"forward_btn")
        self.forward_btn.setGeometry(QRect(60, 110, 41, 41))
        self.backward_btn = QPushButton(self.centralwidget)
        self.backward_btn.setObjectName(u"backward_btn")
        self.backward_btn.setGeometry(QRect(60, 160, 41, 41))
        self.turn_left_btn = QPushButton(self.centralwidget)
        self.turn_left_btn.setObjectName(u"turn_left_btn")
        self.turn_left_btn.setGeometry(QRect(10, 160, 41, 41))
        self.turn_right_btn = QPushButton(self.centralwidget)
        self.turn_right_btn.setObjectName(u"turn_right_btn")
        self.turn_right_btn.setGeometry(QRect(110, 160, 41, 41))
        self.get_azimuth_btn = QPushButton(self.centralwidget)
        self.get_azimuth_btn.setObjectName(u"get_azimuth_btn")
        self.get_azimuth_btn.setGeometry(QRect(440, 140, 101, 31))
        self.beep_btn = QPushButton(self.centralwidget)
        self.beep_btn.setObjectName(u"beep_btn")
        self.beep_btn.setGeometry(QRect(320, 100, 101, 31))
        self.get_distance_btn = QPushButton(self.centralwidget)
        self.get_distance_btn.setObjectName(u"get_distance_btn")
        self.get_distance_btn.setGeometry(QRect(320, 140, 101, 31))
        self.kill_btn = QPushButton(self.centralwidget)
        self.kill_btn.setObjectName(u"kill_btn")
        self.kill_btn.setGeometry(QRect(440, 220, 101, 31))
        self.print_duck_btn = QPushButton(self.centralwidget)
        self.print_duck_btn.setObjectName(u"print_duck_btn")
        self.print_duck_btn.setGeometry(QRect(440, 100, 101, 31))
        self.send_btn = QPushButton(self.centralwidget)
        self.send_btn.setObjectName(u"send_btn")
        self.send_btn.setGeometry(QRect(460, 520, 101, 31))
        self.command_input = QLineEdit(self.centralwidget)
        self.command_input.setObjectName(u"command_input")
        self.command_input.setGeometry(QRect(10, 520, 441, 31))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 70, 541, 21))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 80, 121, 20))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 0, 161, 20))
        self.tab_container = QTabWidget(self.centralwidget)
        self.tab_container.setObjectName(u"tab_container")
        self.tab_container.setGeometry(QRect(560, 10, 580, 630))
        self.pole_plot_tab = QWidget()
        self.pole_plot_tab.setObjectName(u"pole_plot_tab")
        self.gridLayoutWidget_3 = QWidget(self.pole_plot_tab)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 10, 561, 541))
        self.pole_plot_layout = QGridLayout(self.gridLayoutWidget_3)
        self.pole_plot_layout.setObjectName(u"pole_plot_layout")
        self.pole_plot_layout.setContentsMargins(0, 0, 0, 0)
        self.clear_pole_data_btn = QPushButton(self.pole_plot_tab)
        self.clear_pole_data_btn.setObjectName(u"clear_pole_data_btn")
        self.clear_pole_data_btn.setGeometry(QRect(10, 560, 101, 31))
        self.tab_container.addTab(self.pole_plot_tab, "")
        self.pole_plot_3d_tab = QWidget()
        self.pole_plot_3d_tab.setObjectName(u"pole_plot_3d_tab")
        self.gridLayoutWidget_2 = QWidget(self.pole_plot_3d_tab)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 561, 581))
        self.pole_plot_3d_layout = QGridLayout(self.gridLayoutWidget_2)
        self.pole_plot_3d_layout.setObjectName(u"pole_plot_3d_layout")
        self.pole_plot_3d_layout.setContentsMargins(0, 0, 0, 0)
        self.tab_container.addTab(self.pole_plot_3d_tab, "")
        self.raw_tab = QWidget()
        self.raw_tab.setObjectName(u"raw_tab")
        self.command_output_long = QTextBrowser(self.raw_tab)
        self.command_output_long.setObjectName(u"command_output_long")
        self.command_output_long.setGeometry(QRect(10, 10, 561, 581))
        self.command_output_long.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tab_container.addTab(self.raw_tab, "")
        self.mag_cal_plot_tab = QWidget()
        self.mag_cal_plot_tab.setObjectName(u"mag_cal_plot_tab")
        self.gridLayoutWidget_4 = QWidget(self.mag_cal_plot_tab)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 10, 561, 351))
        self.mag_cal_plot_layout = QGridLayout(self.gridLayoutWidget_4)
        self.mag_cal_plot_layout.setObjectName(u"mag_cal_plot_layout")
        self.mag_cal_plot_layout.setContentsMargins(0, 0, 0, 0)
        self.clear_mag_cal_data_btn = QPushButton(self.mag_cal_plot_tab)
        self.clear_mag_cal_data_btn.setObjectName(u"clear_mag_cal_data_btn")
        self.clear_mag_cal_data_btn.setGeometry(QRect(20, 570, 141, 31))
        self.label_8 = QLabel(self.mag_cal_plot_tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 420, 54, 17))
        self.label_8.setFrameShape(QFrame.WinPanel)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.mag_cal_plot_tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 440, 54, 17))
        self.label_9.setFrameShape(QFrame.WinPanel)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(self.mag_cal_plot_tab)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 460, 54, 17))
        self.label_18.setFrameShape(QFrame.WinPanel)
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_19 = QLabel(self.mag_cal_plot_tab)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(70, 400, 54, 17))
        self.label_19.setFrameShape(QFrame.WinPanel)
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_20 = QLabel(self.mag_cal_plot_tab)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(130, 400, 54, 17))
        self.label_20.setFrameShape(QFrame.WinPanel)
        self.label_20.setAlignment(Qt.AlignCenter)
        self.min_x_label = QLabel(self.mag_cal_plot_tab)
        self.min_x_label.setObjectName(u"min_x_label")
        self.min_x_label.setGeometry(QRect(70, 420, 54, 17))
        self.min_x_label.setFrameShape(QFrame.StyledPanel)
        self.min_x_label.setAlignment(Qt.AlignCenter)
        self.min_y_label = QLabel(self.mag_cal_plot_tab)
        self.min_y_label.setObjectName(u"min_y_label")
        self.min_y_label.setGeometry(QRect(130, 420, 54, 17))
        self.min_y_label.setFrameShape(QFrame.StyledPanel)
        self.min_y_label.setAlignment(Qt.AlignCenter)
        self.max_x_label = QLabel(self.mag_cal_plot_tab)
        self.max_x_label.setObjectName(u"max_x_label")
        self.max_x_label.setGeometry(QRect(70, 440, 54, 17))
        self.max_x_label.setFrameShape(QFrame.StyledPanel)
        self.max_x_label.setAlignment(Qt.AlignCenter)
        self.max_y_label = QLabel(self.mag_cal_plot_tab)
        self.max_y_label.setObjectName(u"max_y_label")
        self.max_y_label.setGeometry(QRect(130, 440, 54, 17))
        self.max_y_label.setFrameShape(QFrame.StyledPanel)
        self.max_y_label.setAlignment(Qt.AlignCenter)
        self.offset_x_label = QLabel(self.mag_cal_plot_tab)
        self.offset_x_label.setObjectName(u"offset_x_label")
        self.offset_x_label.setGeometry(QRect(70, 460, 54, 17))
        self.offset_x_label.setFrameShape(QFrame.StyledPanel)
        self.offset_x_label.setAlignment(Qt.AlignCenter)
        self.offset_y_label = QLabel(self.mag_cal_plot_tab)
        self.offset_y_label.setObjectName(u"offset_y_label")
        self.offset_y_label.setGeometry(QRect(130, 460, 54, 17))
        self.offset_y_label.setFrameShape(QFrame.StyledPanel)
        self.offset_y_label.setAlignment(Qt.AlignCenter)
        self.measure_btn = QPushButton(self.mag_cal_plot_tab)
        self.measure_btn.setObjectName(u"measure_btn")
        self.measure_btn.setGeometry(QRect(20, 490, 141, 31))
        self.calibration_progbar = QProgressBar(self.mag_cal_plot_tab)
        self.calibration_progbar.setObjectName(u"calibration_progbar")
        self.calibration_progbar.setGeometry(QRect(170, 490, 391, 31))
        self.calibration_progbar.setValue(0)
        self.autocalibration_btn = QPushButton(self.mag_cal_plot_tab)
        self.autocalibration_btn.setObjectName(u"autocalibration_btn")
        self.autocalibration_btn.setGeometry(QRect(20, 530, 141, 31))
        self.label_22 = QLabel(self.mag_cal_plot_tab)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 370, 174, 21))
        self.label_22.setFrameShape(QFrame.WinPanel)
        self.label_23 = QLabel(self.mag_cal_plot_tab)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(200, 370, 361, 21))
        self.label_23.setFrameShape(QFrame.WinPanel)
        self.label_24 = QLabel(self.mag_cal_plot_tab)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(200, 430, 41, 17))
        self.label_24.setFrameShape(QFrame.WinPanel)
        self.label_24.setAlignment(Qt.AlignCenter)
        self.rmax_label = QLabel(self.mag_cal_plot_tab)
        self.rmax_label.setObjectName(u"rmax_label")
        self.rmax_label.setGeometry(QRect(250, 430, 51, 17))
        self.rmax_label.setFrameShape(QFrame.StyledPanel)
        self.rmax_label.setAlignment(Qt.AlignCenter)
        self.label_26 = QLabel(self.mag_cal_plot_tab)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(200, 410, 41, 17))
        self.label_26.setFrameShape(QFrame.WinPanel)
        self.label_26.setAlignment(Qt.AlignCenter)
        self.theta_label = QLabel(self.mag_cal_plot_tab)
        self.theta_label.setObjectName(u"theta_label")
        self.theta_label.setGeometry(QRect(250, 450, 51, 17))
        self.theta_label.setFrameShape(QFrame.StyledPanel)
        self.theta_label.setAlignment(Qt.AlignCenter)
        self.label_27 = QLabel(self.mag_cal_plot_tab)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(200, 450, 41, 17))
        self.label_27.setFrameShape(QFrame.WinPanel)
        self.label_27.setAlignment(Qt.AlignCenter)
        self.rmin_label = QLabel(self.mag_cal_plot_tab)
        self.rmin_label.setObjectName(u"rmin_label")
        self.rmin_label.setGeometry(QRect(250, 410, 51, 17))
        self.rmin_label.setFrameShape(QFrame.StyledPanel)
        self.rmin_label.setAlignment(Qt.AlignCenter)
        self.label_28 = QLabel(self.mag_cal_plot_tab)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(310, 390, 41, 91))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setFrameShape(QFrame.NoFrame)
        self.label_28.setAlignment(Qt.AlignCenter)
        self.costheta_label = QLabel(self.mag_cal_plot_tab)
        self.costheta_label.setObjectName(u"costheta_label")
        self.costheta_label.setGeometry(QRect(380, 420, 41, 17))
        self.costheta_label.setFrameShape(QFrame.StyledPanel)
        self.costheta_label.setAlignment(Qt.AlignCenter)
        self.sintheta_label = QLabel(self.mag_cal_plot_tab)
        self.sintheta_label.setObjectName(u"sintheta_label")
        self.sintheta_label.setGeometry(QRect(430, 420, 41, 17))
        self.sintheta_label.setFrameShape(QFrame.StyledPanel)
        self.sintheta_label.setAlignment(Qt.AlignCenter)
        self.minussintheta_label = QLabel(self.mag_cal_plot_tab)
        self.minussintheta_label.setObjectName(u"minussintheta_label")
        self.minussintheta_label.setGeometry(QRect(380, 460, 41, 17))
        self.minussintheta_label.setFrameShape(QFrame.StyledPanel)
        self.minussintheta_label.setAlignment(Qt.AlignCenter)
        self.costheta2_label = QLabel(self.mag_cal_plot_tab)
        self.costheta2_label.setObjectName(u"costheta2_label")
        self.costheta2_label.setGeometry(QRect(430, 460, 41, 17))
        self.costheta2_label.setFrameShape(QFrame.StyledPanel)
        self.costheta2_label.setAlignment(Qt.AlignCenter)
        self.label_29 = QLabel(self.mag_cal_plot_tab)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(380, 400, 41, 17))
        self.label_29.setFrameShape(QFrame.WinPanel)
        self.label_29.setAlignment(Qt.AlignCenter)
        self.label_30 = QLabel(self.mag_cal_plot_tab)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(430, 440, 41, 17))
        self.label_30.setFrameShape(QFrame.WinPanel)
        self.label_30.setAlignment(Qt.AlignCenter)
        self.label_31 = QLabel(self.mag_cal_plot_tab)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(380, 440, 41, 17))
        self.label_31.setFrameShape(QFrame.WinPanel)
        self.label_31.setAlignment(Qt.AlignCenter)
        self.label_32 = QLabel(self.mag_cal_plot_tab)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(430, 400, 41, 17))
        self.label_32.setFrameShape(QFrame.WinPanel)
        self.label_32.setAlignment(Qt.AlignCenter)
        self.noname_label_8 = QLabel(self.mag_cal_plot_tab)
        self.noname_label_8.setObjectName(u"noname_label_8")
        self.noname_label_8.setGeometry(QRect(340, 390, 41, 91))
        font1 = QFont()
        font1.setPointSize(48)
        self.noname_label_8.setFont(font1)
        self.noname_label_8.setFrameShape(QFrame.NoFrame)
        self.noname_label_8.setAlignment(Qt.AlignCenter)
        self.noname_label_9 = QLabel(self.mag_cal_plot_tab)
        self.noname_label_9.setObjectName(u"noname_label_9")
        self.noname_label_9.setGeometry(QRect(470, 390, 41, 91))
        self.noname_label_9.setFont(font1)
        self.noname_label_9.setFrameShape(QFrame.NoFrame)
        self.noname_label_9.setAlignment(Qt.AlignCenter)
        self.line_6 = QFrame(self.mag_cal_plot_tab)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(180, 370, 20, 111))
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.autocalibration_btn_2 = QPushButton(self.mag_cal_plot_tab)
        self.autocalibration_btn_2.setObjectName(u"autocalibration_btn_2")
        self.autocalibration_btn_2.setGeometry(QRect(170, 530, 141, 31))
        self.label_33 = QLabel(self.mag_cal_plot_tab)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(510, 420, 41, 17))
        self.label_33.setFrameShape(QFrame.WinPanel)
        self.label_33.setAlignment(Qt.AlignCenter)
        self.sigma_label = QLabel(self.mag_cal_plot_tab)
        self.sigma_label.setObjectName(u"sigma_label")
        self.sigma_label.setGeometry(QRect(510, 440, 41, 17))
        self.sigma_label.setFrameShape(QFrame.StyledPanel)
        self.sigma_label.setAlignment(Qt.AlignCenter)
        self.tab_container.addTab(self.mag_cal_plot_tab, "")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 470, 161, 20))
        self.tower_slider = QSlider(self.centralwidget)
        self.tower_slider.setObjectName(u"tower_slider")
        self.tower_slider.setGeometry(QRect(10, 210, 141, 21))
        self.tower_slider.setMinimum(0)
        self.tower_slider.setMaximum(180)
        self.tower_slider.setValue(90)
        self.tower_slider.setOrientation(Qt.Horizontal)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 460, 541, 21))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.connection_status_label = QLabel(self.centralwidget)
        self.connection_status_label.setObjectName(u"connection_status_label")
        self.connection_status_label.setGeometry(QRect(370, 20, 51, 51))
        font2 = QFont()
        font2.setPointSize(28)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setKerning(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.connection_status_label.setFont(font2)
        self.connection_status_label.setAlignment(Qt.AlignCenter)
        self.connection_status_label.setMargin(0)
        self.scan_btn = QPushButton(self.centralwidget)
        self.scan_btn.setObjectName(u"scan_btn")
        self.scan_btn.setGeometry(QRect(320, 220, 101, 31))
        self.turn_left_step_btn = QPushButton(self.centralwidget)
        self.turn_left_step_btn.setObjectName(u"turn_left_step_btn")
        self.turn_left_step_btn.setGeometry(QRect(10, 320, 41, 41))
        self.backward_step_btn = QPushButton(self.centralwidget)
        self.backward_step_btn.setObjectName(u"backward_step_btn")
        self.backward_step_btn.setGeometry(QRect(60, 320, 41, 41))
        self.forward_step_btn = QPushButton(self.centralwidget)
        self.forward_step_btn.setObjectName(u"forward_step_btn")
        self.forward_step_btn.setGeometry(QRect(60, 270, 41, 41))
        self.turn_right_step_btn = QPushButton(self.centralwidget)
        self.turn_right_step_btn.setObjectName(u"turn_right_step_btn")
        self.turn_right_step_btn.setGeometry(QRect(110, 320, 41, 41))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 240, 151, 20))
        self.drive_step_slider = QSlider(self.centralwidget)
        self.drive_step_slider.setObjectName(u"drive_step_slider")
        self.drive_step_slider.setGeometry(QRect(10, 430, 141, 21))
        self.drive_step_slider.setMinimum(1)
        self.drive_step_slider.setMaximum(30)
        self.drive_step_slider.setValue(10)
        self.drive_step_slider.setOrientation(Qt.Horizontal)
        self.rotate_step_slider = QSlider(self.centralwidget)
        self.rotate_step_slider.setObjectName(u"rotate_step_slider")
        self.rotate_step_slider.setGeometry(QRect(10, 400, 141, 21))
        self.rotate_step_slider.setMinimum(10)
        self.rotate_step_slider.setMaximum(90)
        self.rotate_step_slider.setSingleStep(1)
        self.rotate_step_slider.setValue(30)
        self.rotate_step_slider.setOrientation(Qt.Horizontal)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(200, 210, 101, 20))
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(200, 430, 101, 20))
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(200, 400, 101, 20))
        self.rotate_to_slider = QSlider(self.centralwidget)
        self.rotate_to_slider.setObjectName(u"rotate_to_slider")
        self.rotate_to_slider.setGeometry(QRect(10, 370, 141, 21))
        self.rotate_to_slider.setMinimum(0)
        self.rotate_to_slider.setMaximum(360)
        self.rotate_to_slider.setSingleStep(1)
        self.rotate_to_slider.setValue(180)
        self.rotate_to_slider.setOrientation(Qt.Horizontal)
        self.rotate_to_btn = QPushButton(self.centralwidget)
        self.rotate_to_btn.setObjectName(u"rotate_to_btn")
        self.rotate_to_btn.setGeometry(QRect(200, 360, 101, 31))
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(160, 400, 31, 21))
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(160, 430, 31, 21))
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(160, 370, 31, 21))
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(160, 210, 31, 21))
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 230, 301, 21))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(300, 79, 20, 390))
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(320, 80, 121, 20))
        self.clear_buffer_btn = QPushButton(self.centralwidget)
        self.clear_buffer_btn.setObjectName(u"clear_buffer_btn")
        self.clear_buffer_btn.setGeometry(QRect(460, 570, 101, 31))
        self.get_mag_btn = QPushButton(self.centralwidget)
        self.get_mag_btn.setObjectName(u"get_mag_btn")
        self.get_mag_btn.setGeometry(QRect(320, 180, 101, 31))
        self.get_mag_cal_btn = QPushButton(self.centralwidget)
        self.get_mag_cal_btn.setObjectName(u"get_mag_cal_btn")
        self.get_mag_cal_btn.setGeometry(QRect(440, 180, 101, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.serial_combo, self.serial_refresh_btn)
        QWidget.setTabOrder(self.serial_refresh_btn, self.serial_connect_btn)
        QWidget.setTabOrder(self.serial_connect_btn, self.forward_btn)
        QWidget.setTabOrder(self.forward_btn, self.turn_left_btn)
        QWidget.setTabOrder(self.turn_left_btn, self.backward_btn)
        QWidget.setTabOrder(self.backward_btn, self.turn_right_btn)
        QWidget.setTabOrder(self.turn_right_btn, self.get_distance_btn)
        QWidget.setTabOrder(self.get_distance_btn, self.get_azimuth_btn)
        QWidget.setTabOrder(self.get_azimuth_btn, self.beep_btn)
        QWidget.setTabOrder(self.beep_btn, self.print_duck_btn)
        QWidget.setTabOrder(self.print_duck_btn, self.kill_btn)
        QWidget.setTabOrder(self.kill_btn, self.command_input)
        QWidget.setTabOrder(self.command_input, self.send_btn)
        QWidget.setTabOrder(self.send_btn, self.command_output_short)
        QWidget.setTabOrder(self.command_output_short, self.tab_container)
        QWidget.setTabOrder(self.tab_container, self.command_output_long)
        QWidget.setTabOrder(self.command_output_long, self.tower_slider)

        self.retranslateUi(MainWindow)
        self.rotate_step_slider.valueChanged.connect(self.label_14.setNum)
        self.drive_step_slider.sliderMoved.connect(self.label_15.setNum)
        self.rotate_to_slider.valueChanged.connect(self.label_16.setNum)
        self.tower_slider.valueChanged.connect(self.label_17.setNum)

        self.tab_container.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ScanBot Control Application", None))
        self.serial_refresh_btn.setText(QCoreApplication.translate("MainWindow", u"refresh", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"choose serial port", None))
        self.serial_connect_btn.setText(QCoreApplication.translate("MainWindow", u"connect", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"command line", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"output", None))
        self.forward_btn.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.backward_btn.setText(QCoreApplication.translate("MainWindow", u"\\/", None))
        self.turn_left_btn.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.turn_right_btn.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.get_azimuth_btn.setText(QCoreApplication.translate("MainWindow", u"GET_AZIMUTH", None))
        self.beep_btn.setText(QCoreApplication.translate("MainWindow", u"BEEP", None))
#if QT_CONFIG(shortcut)
        self.beep_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.get_distance_btn.setText(QCoreApplication.translate("MainWindow", u"GET_DISTANCE", None))
        self.kill_btn.setText(QCoreApplication.translate("MainWindow", u"KILL", None))
        self.print_duck_btn.setText(QCoreApplication.translate("MainWindow", u"PRINT DUCK", None))
        self.send_btn.setText(QCoreApplication.translate("MainWindow", u"SEND", None))
#if QT_CONFIG(shortcut)
        self.send_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"RAW CONTROL", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"CONNECTION", None))
        self.clear_pole_data_btn.setText(QCoreApplication.translate("MainWindow", u"CLEAR DATA", None))
        self.tab_container.setTabText(self.tab_container.indexOf(self.pole_plot_tab), QCoreApplication.translate("MainWindow", u"2D view", None))
        self.tab_container.setTabText(self.tab_container.indexOf(self.pole_plot_3d_tab), QCoreApplication.translate("MainWindow", u"3D view", None))
        self.tab_container.setTabText(self.tab_container.indexOf(self.raw_tab), QCoreApplication.translate("MainWindow", u"raw output", None))
#if QT_CONFIG(accessibility)
        self.mag_cal_plot_tab.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.clear_mag_cal_data_btn.setText(QCoreApplication.translate("MainWindow", u"CLEAR DATA", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"MIN", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"MAX", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"OFFSET", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.min_x_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.min_y_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.max_x_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.max_y_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.offset_x_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.offset_y_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.measure_btn.setText(QCoreApplication.translate("MainWindow", u"MANUAL MEASUREMENT", None))
        self.autocalibration_btn.setText(QCoreApplication.translate("MainWindow", u"AUTOCALIBRATION", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"HARD IRON CORRECTION", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"SOFT IRON CORRECTION", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Rmax", None))
        self.rmax_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Rmin", None))
        self.theta_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u03b8[rad]", None))
        self.rmin_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"R =", None))
        self.costheta_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.sintheta_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.minussintheta_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.costheta2_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"cos \u03b8", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"cos \u03b8", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"-sin \u03b8", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"sin \u03b8", None))
        self.noname_label_8.setText(QCoreApplication.translate("MainWindow", u"[", None))
        self.noname_label_9.setText(QCoreApplication.translate("MainWindow", u"]", None))
        self.autocalibration_btn_2.setText(QCoreApplication.translate("MainWindow", u"SEND CALIBRATION DATA", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u03c3", None))
        self.sigma_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.tab_container.setTabText(self.tab_container.indexOf(self.mag_cal_plot_tab), QCoreApplication.translate("MainWindow", u"magnetometer calibration", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CONSOLE", None))
        self.connection_status_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u274c</p></body></html>", None))
        self.scan_btn.setText(QCoreApplication.translate("MainWindow", u"SCAN", None))
#if QT_CONFIG(shortcut)
        self.scan_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.turn_left_step_btn.setText(QCoreApplication.translate("MainWindow", u"<", None))
#if QT_CONFIG(shortcut)
        self.turn_left_step_btn.setShortcut(QCoreApplication.translate("MainWindow", u"A", None))
#endif // QT_CONFIG(shortcut)
        self.backward_step_btn.setText(QCoreApplication.translate("MainWindow", u"\\/", None))
#if QT_CONFIG(shortcut)
        self.backward_step_btn.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.forward_step_btn.setText(QCoreApplication.translate("MainWindow", u"^", None))
#if QT_CONFIG(shortcut)
        self.forward_step_btn.setShortcut(QCoreApplication.translate("MainWindow", u"W", None))
#endif // QT_CONFIG(shortcut)
        self.turn_right_step_btn.setText(QCoreApplication.translate("MainWindow", u">", None))
#if QT_CONFIG(shortcut)
        self.turn_right_step_btn.setShortcut(QCoreApplication.translate("MainWindow", u"D", None))
#endif // QT_CONFIG(shortcut)
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"ODOMETRIC CONTROL", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"tower position", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"drive step", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"rotate step", None))
        self.rotate_to_btn.setText(QCoreApplication.translate("MainWindow", u"ROTATE TO", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"180", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"90", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"FUNCTIONS", None))
        self.clear_buffer_btn.setText(QCoreApplication.translate("MainWindow", u"CLEAR BUFFER", None))
#if QT_CONFIG(shortcut)
        self.clear_buffer_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.get_mag_btn.setText(QCoreApplication.translate("MainWindow", u"GET_MAG", None))
#if QT_CONFIG(shortcut)
        self.get_mag_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.get_mag_cal_btn.setText(QCoreApplication.translate("MainWindow", u"GET_MAG_CAL", None))
#if QT_CONFIG(shortcut)
        self.get_mag_cal_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

