from PySide6.QtWidgets import QApplication
from PySide6.QtCore import  Qt
from PySide6.QtGui import  QIcon
import threading
import queue
import os, re
from PySide6.QtWidgets import QListWidgetItem
import json
import time
from ui.ui_mainwindow import Ui_MainWindow
import random
from modules.backend.websiteName_configs import get_website_name_from_url
from modules.backend.extract_all_images import get_all_imgs_without_tag, get_all_images_without_tag_using_re
from modules.backend.download_file_url import download_file
from modules.backend.Extract_title import extract_title_from_urls, extract_title_from_html_title

from modules.backend.custom_request import Custom_Request



class QueuePageUI:
    def __init__(self, parent, ui:Ui_MainWindow, settings_json):
        self.parent = parent  #for qmessage
        self.ui = ui
        self.settings_json = settings_json
        self.lock = threading.Lock()
        self.is_downloading = False
        self.selected_urls_queue = queue.Queue()  
        self.url_set = set()  
        self.url_items = {}  # To keep track of the QListWidgetItem for each URL
        self.icon_queued = QIcon("icons/queue_icon.png")  
        self.icon_downloaded = QIcon("icons/downloaded_icon.png")  
        self.icon_already_exists = QIcon("icons/already_exists_icon.png")  
        self.downloads_directory = self.settings_json['downloads_directory']
        self.c_request = Custom_Request()
        self.stop_download()
        self.add_urls_guide_lb()
    def add_urls_guide_lb(self):
        self.ui.lb_quide_add_urls_qd.setText("Copy one or more chapter URLs and paste them here.\nYou can add multiple chapter links at once by copying them all together.")
    def get_website_config_data(self, website_name):
        website_json = os.path.join("website settings", f"{website_name}.json")
        if not os.path.exists(website_json):
            return None, None
        try:
            with open(website_json, 'r', encoding='utf-8') as f:
                website_data = json.load(f)
        except:
            return None, None
        if isinstance(website_data, dict):
            title_chapter_source = website_data.get("title_chapter_source")
            image_naming = website_data.get("image_naming")
            return title_chapter_source, image_naming
        else: 
            return None, None
        
    def prepare_images(self, url, response):
        images_v2 = get_all_images_without_tag_using_re(url, response=response)
        time.sleep(0.1)
        images_img = get_all_imgs_without_tag(url, "img", response=response)
        time.sleep(0.1)
        images_a = get_all_imgs_without_tag(url, "a", response=response)
        images = list(dict.fromkeys(images_v2 + images_img + images_a)) #using both (a, img) in case empty or trash
        return images
    def download_selected_urls(self): #main task
        empty_printed = False  
        rename_file = False
        while self.is_downloading:
            try:
                with self.lock:
                    if not self.is_downloading:
                        break
                rename_file_num = 0
                url = self.selected_urls_queue.get(timeout=1) 
                response = self.c_request.send_request(url)
                if response:

                    website_name = get_website_name_from_url(url)
                    title_chapter_source, image_naming = self.get_website_config_data(website_name)
                    if title_chapter_source:
                        if title_chapter_source == "url":   
                            manhwa_title, chapter_title = extract_title_from_urls(url)
                        elif  title_chapter_source == "html_title":
                            manhwa_title, chapter_title = extract_title_from_html_title(url)
                        else:
                            manhwa_title, chapter_title = extract_title_from_html_title(url)
                    else:
                        manhwa_title, chapter_title = extract_title_from_html_title(url)
                    if image_naming == 'change_filename':
                        rename_file = True
                    if not manhwa_title:
                        manhwa_title = str(random.randrange(100000, 999999))
                    if not chapter_title:
                        chapter_title = str(random.randrange(100000, 999999))
                    folder_path = os.path.join(self.downloads_directory, manhwa_title, chapter_title)
                    if os.path.exists(folder_path) and os.path.isdir(folder_path):
                        self.selected_urls_queue.task_done()
                        list_item = self.url_items[url]
                        list_item.setIcon(self.icon_already_exists)  # Update icon
                        list_item.setText(f"{url} (Already Exists)")
                        continue
                    images = self.prepare_images(url, response)
                    for img_src in images:
                        if not self.is_downloading:
                            break
                        if rename_file:
                            rename_file_num+=1
                            rename_file = str(rename_file_num).zfill(3)
                        stop_condition = lambda: self.is_downloading  
                        download_file(img_src, manhwa_title, chapter_title,  self.downloads_directory, rename_file, stop_condition)
                        time.sleep(0.01)
                        
                    self.selected_urls_queue.task_done()
                    list_item = self.url_items[url]
                    list_item.setIcon(self.icon_downloaded)  
                    list_item.setText(f"{url} (Downloaded)")  
                    empty_printed = False
            except queue.Empty:
                if not empty_printed:
                    print("Done Queue has no more tasks")
                    empty_printed = True  # Set flag to avoid repeated prints
                continue
        self.is_downloading = False
        print("Completed Download")

                
    def clear_all_queue(self):
        self.selected_urls_queue = queue.Queue()
        self.ui.listWidget_queue_downloads_gc.clear()
        self.url_set.clear()
        self.url_items.clear()
        print("All items cleared from queue and UI.")
    
    def add_chapter_url_to_queue_directly_clipboard(self): 
        clipboard = QApplication.clipboard()
        clipboard_text = clipboard.text()
        self.ui.le_add_chapter_urls_qd.setText(clipboard_text)
        self.add_chapter_url_to_queue_directly()
            
    def add_chapter_url_to_queue_directly(self):
        input_text = self.ui.le_add_chapter_urls_qd.text()
        self.ui.le_add_chapter_urls_qd.clear()
        # Regex to match valid URLs (HTTP, HTTPS, FTP, etc.)
        url_pattern = r'https?://[^\s,]+'
        urls = re.findall(url_pattern, input_text)
        for url in urls:
            self.add_url_to_queue(url)
    def add_url_to_gather_chapters(self):
        items = self.ui.listWidget_chapters.selectedItems()
        self.ui.listWidget_chapters.clearSelection()
        for item in items:
            url = item.data(Qt.UserRole)
            self.add_url_to_queue(url)
    def add_url_to_queue(self, url):
        if url not in self.url_set:
            self.selected_urls_queue.put(url)
            self.url_set.add(url)
            print(f"Added URL to queue: {url}")
            list_item = QListWidgetItem(f"{url} (Queued)")
            icon = QIcon(self.icon_queued) 
            list_item.setIcon(icon)  
            self.ui.listWidget_queue_downloads_gc.addItem(list_item)
            self.url_items[url] = list_item
        else:
            print(f"URL already in queue: {url}")

    def start_download(self):
        if not self.is_downloading:
            self.is_downloading = True  
            download_thread = threading.Thread(target=self.download_selected_urls)
            download_thread.start()  
            print("Downloading started.")
            self.ui.bt_start_queue_downloads_qd.setEnabled(False)
            self.ui.bt_stop_queue_downloads_qd.setEnabled(True)
    def stop_download(self):
        self.is_downloading = False  
        print("Downloading stopped.")
        self.ui.bt_stop_queue_downloads_qd.setEnabled(False)
        self.ui.bt_start_queue_downloads_qd.setEnabled(True)
