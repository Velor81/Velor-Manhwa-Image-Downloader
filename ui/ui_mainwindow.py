# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,
    QMetaObject, 
    QSize, Qt)
from PySide6.QtGui import (
    QFont,)
from PySide6.QtWidgets import (QAbstractItemView,QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(905, 674)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_side_menu_frame = QFrame(self.centralwidget)
        self.main_side_menu_frame.setObjectName(u"main_side_menu_frame")
        self.main_side_menu_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.main_side_menu_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.main_side_menu_frame.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.main_side_menu_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.main_side_menu_frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.stacked_buttons_Frame = QFrame(self.main_side_menu_frame)
        self.stacked_buttons_Frame.setObjectName(u"stacked_buttons_Frame")
        self.stacked_buttons_Frame.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.stacked_buttons_Frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(8, 20, 0, 0)
        self.queue_downloads_bt = QPushButton(self.stacked_buttons_Frame)
        self.queue_downloads_bt.setObjectName(u"queue_downloads_bt")
        self.queue_downloads_bt.setMinimumSize(QSize(0, 30))
        self.queue_downloads_bt.setCheckable(True)
        self.queue_downloads_bt.setAutoExclusive(True)
        self.queue_downloads_bt.setFlat(True)

        self.verticalLayout_2.addWidget(self.queue_downloads_bt)

        self.url_image_grabber_bt = QPushButton(self.stacked_buttons_Frame)
        self.url_image_grabber_bt.setObjectName(u"url_image_grabber_bt")
        self.url_image_grabber_bt.setMinimumSize(QSize(0, 30))
        self.url_image_grabber_bt.setCheckable(True)
        self.url_image_grabber_bt.setAutoExclusive(True)
        self.url_image_grabber_bt.setFlat(True)

        self.verticalLayout_2.addWidget(self.url_image_grabber_bt)

        self.website_settings_bt = QPushButton(self.stacked_buttons_Frame)
        self.website_settings_bt.setObjectName(u"website_settings_bt")
        self.website_settings_bt.setMinimumSize(QSize(0, 30))
        self.website_settings_bt.setCheckable(True)
        self.website_settings_bt.setAutoExclusive(True)
        self.website_settings_bt.setFlat(True)

        self.verticalLayout_2.addWidget(self.website_settings_bt)

        self.settings_bt = QPushButton(self.stacked_buttons_Frame)
        self.settings_bt.setObjectName(u"settings_bt")
        self.settings_bt.setMinimumSize(QSize(0, 30))
        self.settings_bt.setCheckable(True)
        self.settings_bt.setAutoExclusive(True)
        self.settings_bt.setFlat(True)

        self.verticalLayout_2.addWidget(self.settings_bt)

        self.about_bt = QPushButton(self.stacked_buttons_Frame)
        self.about_bt.setObjectName(u"about_bt")
        self.about_bt.setMinimumSize(QSize(0, 30))
        self.about_bt.setCheckable(True)
        self.about_bt.setAutoExclusive(True)
        self.about_bt.setFlat(True)

        self.verticalLayout_2.addWidget(self.about_bt)


        self.verticalLayout.addWidget(self.stacked_buttons_Frame, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.quit_bt = QPushButton(self.main_side_menu_frame)
        self.quit_bt.setObjectName(u"quit_bt")
        self.quit_bt.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.quit_bt)


        self.horizontalLayout.addWidget(self.main_side_menu_frame)

        self.main_body_stackedWidget = QStackedWidget(self.centralwidget)
        self.main_body_stackedWidget.setObjectName(u"main_body_stackedWidget")
        self.queue_downloads_page_2 = QWidget()
        self.queue_downloads_page_2.setObjectName(u"queue_downloads_page_2")
        self.horizontalLayout_19 = QHBoxLayout(self.queue_downloads_page_2)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.chapterListFrame_gc = QFrame(self.queue_downloads_page_2)
        self.chapterListFrame_gc.setObjectName(u"chapterListFrame_gc")
        self.verticalLayout_7 = QVBoxLayout(self.chapterListFrame_gc)
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame = QFrame(self.chapterListFrame_gc)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalLayout_12 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_12.setSpacing(4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(1, 6, 4, 4)
        self.lb_quide_add_urls_qd = QLabel(self.verticalFrame)
        self.lb_quide_add_urls_qd.setObjectName(u"lb_quide_add_urls_qd")

        self.verticalLayout_12.addWidget(self.lb_quide_add_urls_qd)

        self.horizontalFrame_6 = QFrame(self.verticalFrame)
        self.horizontalFrame_6.setObjectName(u"horizontalFrame_6")
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalFrame_6)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.bt_add_chapters_qd = QPushButton(self.horizontalFrame_6)
        self.bt_add_chapters_qd.setObjectName(u"bt_add_chapters_qd")

        self.horizontalLayout_9.addWidget(self.bt_add_chapters_qd, 0, Qt.AlignmentFlag.AlignLeft)

        self.le_add_chapter_urls_qd = QLineEdit(self.horizontalFrame_6)
        self.le_add_chapter_urls_qd.setObjectName(u"le_add_chapter_urls_qd")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_add_chapter_urls_qd.sizePolicy().hasHeightForWidth())
        self.le_add_chapter_urls_qd.setSizePolicy(sizePolicy)
        self.le_add_chapter_urls_qd.setClearButtonEnabled(True)

        self.horizontalLayout_9.addWidget(self.le_add_chapter_urls_qd)

        self.bt_paste_qd = QPushButton(self.horizontalFrame_6)
        self.bt_paste_qd.setObjectName(u"bt_paste_qd")

        self.horizontalLayout_9.addWidget(self.bt_paste_qd)


        self.verticalLayout_12.addWidget(self.horizontalFrame_6)


        self.verticalLayout_7.addWidget(self.verticalFrame)

        self.verticalFrame_3 = QFrame(self.chapterListFrame_gc)
        self.verticalFrame_3.setObjectName(u"verticalFrame_3")
        self.verticalLayout_8 = QVBoxLayout(self.verticalFrame_3)
        self.verticalLayout_8.setSpacing(4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.listWidget_queue_downloads_gc = QListWidget(self.verticalFrame_3)
        self.listWidget_queue_downloads_gc.setObjectName(u"listWidget_queue_downloads_gc")
        self.listWidget_queue_downloads_gc.setFrameShape(QFrame.Shape.NoFrame)
        self.listWidget_queue_downloads_gc.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        self.verticalLayout_8.addWidget(self.listWidget_queue_downloads_gc)


        self.verticalLayout_7.addWidget(self.verticalFrame_3)

        self.horizontalFrame_7 = QFrame(self.chapterListFrame_gc)
        self.horizontalFrame_7.setObjectName(u"horizontalFrame_7")
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalFrame_7)
        self.horizontalLayout_10.setSpacing(4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.bt_start_queue_downloads_qd = QPushButton(self.horizontalFrame_7)
        self.bt_start_queue_downloads_qd.setObjectName(u"bt_start_queue_downloads_qd")
        self.bt_start_queue_downloads_qd.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_10.addWidget(self.bt_start_queue_downloads_qd)

        self.bt_stop_queue_downloads_qd = QPushButton(self.horizontalFrame_7)
        self.bt_stop_queue_downloads_qd.setObjectName(u"bt_stop_queue_downloads_qd")
        self.bt_stop_queue_downloads_qd.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_10.addWidget(self.bt_stop_queue_downloads_qd)

        self.bt_clear_queue_gd = QPushButton(self.horizontalFrame_7)
        self.bt_clear_queue_gd.setObjectName(u"bt_clear_queue_gd")
        self.bt_clear_queue_gd.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_10.addWidget(self.bt_clear_queue_gd)


        self.verticalLayout_7.addWidget(self.horizontalFrame_7)


        self.horizontalLayout_19.addWidget(self.chapterListFrame_gc)

        self.main_body_stackedWidget.addWidget(self.queue_downloads_page_2)
        self.Image_Grabber_3 = QWidget()
        self.Image_Grabber_3.setObjectName(u"Image_Grabber_3")
        self.verticalLayout_13 = QVBoxLayout(self.Image_Grabber_3)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame_11 = QFrame(self.Image_Grabber_3)
        self.horizontalFrame_11.setObjectName(u"horizontalFrame_11")
        self.horizontalLayout_14 = QHBoxLayout(self.horizontalFrame_11)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.bt_get_uig = QPushButton(self.horizontalFrame_11)
        self.bt_get_uig.setObjectName(u"bt_get_uig")

        self.horizontalLayout_14.addWidget(self.bt_get_uig)

        self.lineEdit_get_uig = QLineEdit(self.horizontalFrame_11)
        self.lineEdit_get_uig.setObjectName(u"lineEdit_get_uig")
        self.lineEdit_get_uig.setClearButtonEnabled(True)

        self.horizontalLayout_14.addWidget(self.lineEdit_get_uig)

        self.bt_paste_uig = QPushButton(self.horizontalFrame_11)
        self.bt_paste_uig.setObjectName(u"bt_paste_uig")

        self.horizontalLayout_14.addWidget(self.bt_paste_uig)


        self.verticalLayout_13.addWidget(self.horizontalFrame_11)

        self.chapterListFrame_uig = QFrame(self.Image_Grabber_3)
        self.chapterListFrame_uig.setObjectName(u"chapterListFrame_uig")
        self.verticalLayout_9 = QVBoxLayout(self.chapterListFrame_uig)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame_8 = QFrame(self.chapterListFrame_uig)
        self.horizontalFrame_8.setObjectName(u"horizontalFrame_8")
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalFrame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_9.addWidget(self.horizontalFrame_8)

        self.horizontalFrame_9 = QFrame(self.chapterListFrame_uig)
        self.horizontalFrame_9.setObjectName(u"horizontalFrame_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalFrame_9.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_9.setSizePolicy(sizePolicy1)
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalFrame_9)
        self.horizontalLayout_12.setSpacing(4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_9.addWidget(self.horizontalFrame_9)

        self.verticalFrame_4 = QFrame(self.chapterListFrame_uig)
        self.verticalFrame_4.setObjectName(u"verticalFrame_4")
        self.verticalLayout_10 = QVBoxLayout(self.verticalFrame_4)
        self.verticalLayout_10.setSpacing(4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.listWidget_urls_ig = QListWidget(self.verticalFrame_4)
        self.listWidget_urls_ig.setObjectName(u"listWidget_urls_ig")
        self.listWidget_urls_ig.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.listWidget_urls_ig.setFrameShape(QFrame.Shape.NoFrame)
        self.listWidget_urls_ig.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        self.verticalLayout_10.addWidget(self.listWidget_urls_ig)


        self.verticalLayout_9.addWidget(self.verticalFrame_4)

        self.horizontalFrame_10 = QFrame(self.chapterListFrame_uig)
        self.horizontalFrame_10.setObjectName(u"horizontalFrame_10")
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalFrame_10)
        self.horizontalLayout_13.setSpacing(4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.bt_download_chapters_uig = QPushButton(self.horizontalFrame_10)
        self.bt_download_chapters_uig.setObjectName(u"bt_download_chapters_uig")
        self.bt_download_chapters_uig.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_13.addWidget(self.bt_download_chapters_uig)

        self.bt_remove_chapters_uig = QPushButton(self.horizontalFrame_10)
        self.bt_remove_chapters_uig.setObjectName(u"bt_remove_chapters_uig")
        self.bt_remove_chapters_uig.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_13.addWidget(self.bt_remove_chapters_uig)


        self.verticalLayout_9.addWidget(self.horizontalFrame_10)


        self.verticalLayout_13.addWidget(self.chapterListFrame_uig)

        self.main_body_stackedWidget.addWidget(self.Image_Grabber_3)
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.gridLayout = QGridLayout(self.Settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.Settings)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bt_select_output_bath = QPushButton(self.groupBox)
        self.bt_select_output_bath.setObjectName(u"bt_select_output_bath")

        self.horizontalLayout_2.addWidget(self.bt_select_output_bath)

        self.le_output_path = QLineEdit(self.groupBox)
        self.le_output_path.setObjectName(u"le_output_path")
        self.le_output_path.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.le_output_path)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.main_body_stackedWidget.addWidget(self.Settings)
        self.website_settings_page_ws = QWidget()
        self.website_settings_page_ws.setObjectName(u"website_settings_page_ws")
        self.verticalLayout_6 = QVBoxLayout(self.website_settings_page_ws)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalFrame = QFrame(self.website_settings_page_ws)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalFrame_2 = QFrame(self.horizontalFrame)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalFrame_2.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame1 = QFrame(self.verticalFrame_2)
        self.horizontalFrame1.setObjectName(u"horizontalFrame1")
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.le_add_website_ws = QLineEdit(self.horizontalFrame1)
        self.le_add_website_ws.setObjectName(u"le_add_website_ws")

        self.horizontalLayout_4.addWidget(self.le_add_website_ws)

        self.bt_add_website_ws = QPushButton(self.horizontalFrame1)
        self.bt_add_website_ws.setObjectName(u"bt_add_website_ws")

        self.horizontalLayout_4.addWidget(self.bt_add_website_ws)


        self.verticalLayout_5.addWidget(self.horizontalFrame1)

        self.listWidget_ws = QListWidget(self.verticalFrame_2)
        self.listWidget_ws.setObjectName(u"listWidget_ws")

        self.verticalLayout_5.addWidget(self.listWidget_ws)


        self.horizontalLayout_3.addWidget(self.verticalFrame_2)

        self.verticalStackedWidget_ws = QStackedWidget(self.horizontalFrame)
        self.verticalStackedWidget_ws.setObjectName(u"verticalStackedWidget_ws")
        self.verticalStackedWidget_ws.setMinimumSize(QSize(33, 0))
        self.web_config_stacked_ws = QWidget()
        self.web_config_stacked_ws.setObjectName(u"web_config_stacked_ws")
        self.verticalLayout_4 = QVBoxLayout(self.web_config_stacked_ws)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_web_name_config_ws = QLabel(self.web_config_stacked_ws)
        self.lb_web_name_config_ws.setObjectName(u"lb_web_name_config_ws")
        font = QFont()
        font.setPointSize(17)
        self.lb_web_name_config_ws.setFont(font)
        self.lb_web_name_config_ws.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.lb_web_name_config_ws)

        self.line = QFrame(self.web_config_stacked_ws)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.gb_source_title_ws = QGroupBox(self.web_config_stacked_ws)
        self.gb_source_title_ws.setObjectName(u"gb_source_title_ws")
        sizePolicy2.setHeightForWidth(self.gb_source_title_ws.sizePolicy().hasHeightForWidth())
        self.gb_source_title_ws.setSizePolicy(sizePolicy2)
        self.gb_source_title_ws.setMaximumSize(QSize(16777215, 16666))
        self.horizontalLayout_6 = QHBoxLayout(self.gb_source_title_ws)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.rb_title_html_ws = QRadioButton(self.gb_source_title_ws)
        self.rb_title_html_ws.setObjectName(u"rb_title_html_ws")

        self.horizontalLayout_6.addWidget(self.rb_title_html_ws)

        self.rb_title_url_ws = QRadioButton(self.gb_source_title_ws)
        self.rb_title_url_ws.setObjectName(u"rb_title_url_ws")

        self.horizontalLayout_6.addWidget(self.rb_title_url_ws)


        self.verticalLayout_4.addWidget(self.gb_source_title_ws)

        self.gb_group_naming_ws = QGroupBox(self.web_config_stacked_ws)
        self.gb_group_naming_ws.setObjectName(u"gb_group_naming_ws")
        self.gb_group_naming_ws.setMinimumSize(QSize(0, 0))
        self.gb_group_naming_ws.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_5 = QHBoxLayout(self.gb_group_naming_ws)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.rb_image_naming_kof_ws = QRadioButton(self.gb_group_naming_ws)
        self.rb_image_naming_kof_ws.setObjectName(u"rb_image_naming_kof_ws")

        self.horizontalLayout_5.addWidget(self.rb_image_naming_kof_ws)

        self.rb_image_naming_rtsn_ws = QRadioButton(self.gb_group_naming_ws)
        self.rb_image_naming_rtsn_ws.setObjectName(u"rb_image_naming_rtsn_ws")

        self.horizontalLayout_5.addWidget(self.rb_image_naming_rtsn_ws)


        self.verticalLayout_4.addWidget(self.gb_group_naming_ws)

        self.line_2 = QFrame(self.web_config_stacked_ws)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.bt_save_web_config_ws = QPushButton(self.web_config_stacked_ws)
        self.bt_save_web_config_ws.setObjectName(u"bt_save_web_config_ws")

        self.verticalLayout_4.addWidget(self.bt_save_web_config_ws)

        self.verticalStackedWidget_ws.addWidget(self.web_config_stacked_ws)
        self.non_web_config_selected_stacked_ws = QWidget()
        self.non_web_config_selected_stacked_ws.setObjectName(u"non_web_config_selected_stacked_ws")
        self.non_web_config_selected_stacked_ws.setMinimumSize(QSize(0, 0))
        self.verticalLayout_11 = QVBoxLayout(self.non_web_config_selected_stacked_ws)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.lb_no_web_config_selected_ws = QLabel(self.non_web_config_selected_stacked_ws)
        self.lb_no_web_config_selected_ws.setObjectName(u"lb_no_web_config_selected_ws")
        font1 = QFont()
        font1.setPointSize(22)
        self.lb_no_web_config_selected_ws.setFont(font1)
        self.lb_no_web_config_selected_ws.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.lb_no_web_config_selected_ws)

        self.verticalStackedWidget_ws.addWidget(self.non_web_config_selected_stacked_ws)

        self.horizontalLayout_3.addWidget(self.verticalStackedWidget_ws, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_6.addWidget(self.horizontalFrame)

        self.main_body_stackedWidget.addWidget(self.website_settings_page_ws)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.verticalLayout_3 = QVBoxLayout(self.about_page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.textBrowser_about_page = QTextBrowser(self.about_page)
        self.textBrowser_about_page.setObjectName(u"textBrowser_about_page")
        self.textBrowser_about_page.setFrameShape(QFrame.Shape.NoFrame)
        self.textBrowser_about_page.setFrameShadow(QFrame.Shadow.Sunken)
        self.textBrowser_about_page.setLineWidth(6)

        self.verticalLayout_3.addWidget(self.textBrowser_about_page)

        self.main_body_stackedWidget.addWidget(self.about_page)

        self.horizontalLayout.addWidget(self.main_body_stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.main_body_stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.queue_downloads_bt.setText(QCoreApplication.translate("MainWindow", u"Queue Downloads", None))
        self.url_image_grabber_bt.setText(QCoreApplication.translate("MainWindow", u"Image Grabber", None))
        self.website_settings_bt.setText(QCoreApplication.translate("MainWindow", u"Website Settings", None))
        self.settings_bt.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.about_bt.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.quit_bt.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.lb_quide_add_urls_qd.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.bt_add_chapters_qd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
#if QT_CONFIG(tooltip)
        self.le_add_chapter_urls_qd.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.le_add_chapter_urls_qd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Add Chapter Urls", None))
        self.bt_paste_qd.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.bt_start_queue_downloads_qd.setText(QCoreApplication.translate("MainWindow", u"Start Queue Downloads", None))
        self.bt_stop_queue_downloads_qd.setText(QCoreApplication.translate("MainWindow", u"Stop Queue Downloads", None))
        self.bt_clear_queue_gd.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.bt_get_uig.setText(QCoreApplication.translate("MainWindow", u"Get", None))
        self.lineEdit_get_uig.setPlaceholderText(QCoreApplication.translate("MainWindow", u"add chapter page url", None))
        self.bt_paste_uig.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.bt_download_chapters_uig.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.bt_remove_chapters_uig.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Downloads Path", None))
        self.bt_select_output_bath.setText(QCoreApplication.translate("MainWindow", u"Select Path", None))
        self.le_output_path.setText("")
        self.le_output_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path", None))
        self.le_add_website_ws.setPlaceholderText(QCoreApplication.translate("MainWindow", u"websiteName.com", None))
        self.bt_add_website_ws.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.lb_web_name_config_ws.setText(QCoreApplication.translate("MainWindow", u"websiteName", None))
        self.gb_source_title_ws.setTitle(QCoreApplication.translate("MainWindow", u"Source for title and chapter number", None))
        self.rb_title_html_ws.setText(QCoreApplication.translate("MainWindow", u"HTML Title", None))
        self.rb_title_url_ws.setText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.gb_group_naming_ws.setTitle(QCoreApplication.translate("MainWindow", u"Image Naming", None))
        self.rb_image_naming_kof_ws.setText(QCoreApplication.translate("MainWindow", u"Keep original filenames", None))
        self.rb_image_naming_rtsn_ws.setText(QCoreApplication.translate("MainWindow", u"Rename to sequential numbers (01, 02, 03...)", None))
        self.bt_save_web_config_ws.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.lb_no_web_config_selected_ws.setText(QCoreApplication.translate("MainWindow", u"Add or Select website\n"
"to create config", None))
    # retranslateUi

