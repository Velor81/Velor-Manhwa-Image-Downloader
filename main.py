from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QIcon
import sys
from ui.ui_mainwindow import Ui_MainWindow

from modules.queuePage import QueuePageUI
from modules.imageGraber import ImageGrabberUI
from modules.SettingsPage import SettingsPage
from modules.websiteSettings import WebsiteSettings

class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.showMaximized()
        self.setWindowTitle("Velor Manhwa Image Downloader")
        self.setWindowIcon(QIcon("icons/main icon.ico"))
        self.setup_stacked_widget()     
        self.about_page()
        self.settings_page = SettingsPage(self.ui)
        self.settings_json = self.settings_page.load_settings()
        self.website_settings = WebsiteSettings(self.ui)
        self.queue_page_ui = QueuePageUI(self, self.ui, self.settings_json)
        self.image_grabber_ui = ImageGrabberUI(self.ui, self.settings_json)

        # queue page ui
        self.ui.bt_start_queue_downloads_qd.clicked.connect(self.queue_page_ui.start_download)
        self.ui.bt_add_chapters_qd.clicked.connect(
            self.queue_page_ui.add_chapter_url_to_queue_directly
        )
        self.ui.bt_paste_qd.clicked.connect(
            self.queue_page_ui.add_chapter_url_to_queue_directly_clipboard
        )
        self.ui.le_add_chapter_urls_qd.returnPressed.connect(
            self.queue_page_ui.add_chapter_url_to_queue_directly
        )
        self.ui.bt_clear_queue_gd.clicked.connect(self.queue_page_ui.clear_all_queue)
        
        self.ui.bt_stop_queue_downloads_qd.clicked.connect(
            self.queue_page_ui.stop_download
        )

        # image grabber ui
        self.ui.lineEdit_get_uig.returnPressed.connect(self.image_grabber_ui.get_images_url)
        self.ui.bt_get_uig.clicked.connect(self.image_grabber_ui.get_images_url)
        self.ui.bt_download_chapters_uig.clicked.connect(
            self.image_grabber_ui.download_selected_img_url
        )

        #website setting
        self.ui.bt_add_website_ws.clicked.connect(self.website_settings.add_website)
        self.ui.bt_save_web_config_ws.clicked.connect(self.website_settings.save_edit_web_config)
        self.ui.listWidget_ws.itemClicked.connect(self.website_settings.on_select_web_item)

        #settings page
        self.ui.bt_select_output_bath.clicked.connect(self.settings_page.select_output_path)
        
    def about_page(self):
            about_text = (
                "<b>Developer:</b> Alaa Hamdy (Velor)<br>"
                "<b>My Github: </b>" "<a href='https://github.com/Velor81' style='color:#58a6ff;'>""https://github.com/Velor81" "</a><br>"            
                "Licensed under the MIT License"
                "<hr>"
                
"""
<h3>
A general-purpose Manhwa chapter image downloader
designed to extract and organize chapter images without
requiring site-specific configurations or frequent updates when websites change their domains or structures.
Instead of relying on custom rules for each website, it uses a general approach to image extraction.
</h3>\n
<h3 style="color: #ff4d4d;">
Note: Some websites protected by Cloudflare or similar security systems may block automated requests, preventing the application from accessing or extracting images from their pages.
</h3>
"""
            )

            self.ui.textBrowser_about_page.setHtml(about_text)
            self.ui.textBrowser_about_page.setOpenExternalLinks(True)

    def setup_stacked_widget(self):
        button_index_map = {
            self.ui.queue_downloads_bt: 0,
            self.ui.url_image_grabber_bt: 1,
            self.ui.settings_bt: 2,
            self.ui.website_settings_bt: 3,
            self.ui.about_bt: 4,
        }
        self.ui.queue_downloads_bt.setChecked(True)
        self.ui.main_body_stackedWidget.setCurrentIndex(0)
        for button, index in button_index_map.items():
            button.clicked.connect(
                lambda checked=False, idx=index: self.ui.main_body_stackedWidget.setCurrentIndex(
                    idx
                )
            )
        
        self.ui.website_settings_bt.clicked.connect(
            self.on_website_settings_clicked
        ) 

    def on_website_settings_clicked(self):
        self.ui.verticalStackedWidget_ws.setCurrentIndex(1)

    def closeEvent(self, event):
        self.queue_page_ui.is_downloading = False
        event.accept()


def style(app):
    # app.setStyle('fusion')
    with open("static/style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.resize(950, 600)
    window.show()
    style(app)
    sys.exit(app.exec())
