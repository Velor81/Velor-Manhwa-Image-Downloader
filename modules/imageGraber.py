
from modules.backend.extract_all_images import  get_all_imgs_without_tag, get_all_images_without_tag_using_re
from modules.backend.download_file_url import download_file
from modules.backend.Extract_title import extract_title_from_urls, extract_title_from_html_title
from modules.backend.custom_request import Custom_Request
import random, time

from ui.ui_mainwindow import Ui_MainWindow


class ImageGrabberUI:
    def __init__(self, ui:Ui_MainWindow, settings_json):
        self.ui = ui
        self.settings_json = settings_json
        self.header_index = None
        self.comic_url = ''
        self.c_request = Custom_Request()

    def get_images_url(self):
        self.comic_url = self.ui.lineEdit_get_uig.text()
        response = self.c_request.send_request(self.comic_url)
        if response:
            images_v2 = get_all_images_without_tag_using_re(self.comic_url, response=response)
            time.sleep(0.5)
            images_img = get_all_imgs_without_tag(self.comic_url, "img", response=response)
            time.sleep(0.5)
            images_a = get_all_imgs_without_tag(self.comic_url, "a", response=response)
            urls = list(dict.fromkeys(images_v2 + images_img + images_a)) #using both (a, img) in case empty or trash

            self.display_urls(urls)

    def display_urls(self, urls):
        self.ui.listWidget_urls_ig.clear()
        for each_url in urls:
            self.ui.listWidget_urls_ig.addItem(each_url)

    def download_selected_img_url(self):
        try:
            manhwa_title, chapter_title = extract_title_from_html_title(self.comic_url)
        except:
            manhwa_title, chapter_title = extract_title_from_urls(self.comic_url)
        if not manhwa_title:
            manhwa_title = str(random.randrange(100000, 999999))
        if not chapter_title:
            chapter_title = str(random.randrange(100000, 999999))
        selected_items = self.ui.listWidget_urls_ig.selectedItems()
        self.ui.listWidget_urls_ig.clearSelection()
        if selected_items:
            for item in selected_items:
                url = item.text()
                output_path = self.settings_json["downloads_directory"]
                download_file(url, manhwa_title, chapter_title, output_path)
