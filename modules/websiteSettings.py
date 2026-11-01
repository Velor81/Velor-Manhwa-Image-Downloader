import json,  os
from ui.ui_mainwindow import Ui_MainWindow


"""
JSON config example:
    {
        "title_chapter_source": "html_title",
        "image_naming": "website_filename"
    }

Alternative:
    {
        "title_chapter_source": "url",
        "image_naming": "change_filename"
    }

Defaults:
    title_chapter_source: "url"
    image_naming: "website_filename"
"""


class WebsiteSettings:
    def __init__(self, ui:Ui_MainWindow):
        self.ui = ui
        self.website_settings_path = os.path.abspath("./website settings")
        self.websites_list_display()

    def add_website(self):
        self.ui.bt_add_website_ws.setEnabled(False)
        try:
            website_name = self.ui.le_add_website_ws.text().strip()
            self.ui.le_add_website_ws.clear()
            if website_name:
                data = {
                    "title_chapter_source": "url",
                    "image_naming": "website_filename"
                    }
                with open(f"{self.website_settings_path}/{website_name}.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4)
                self.websites_list_display()
        finally:
            self.ui.bt_add_website_ws.setEnabled(True)
        
    def websites_list_display(self):
        self.ui.listWidget_ws.clear()
        os.makedirs(self.website_settings_path, exist_ok=True)
        files = os.listdir(self.website_settings_path)
        for f in files:
            name, ext = os.path.splitext(f)
            website_name = name.strip()
            if website_name and ext == ".json":
                self.ui.listWidget_ws.addItem(website_name)

    def on_select_web_item(self):
        item = self.ui.listWidget_ws.currentItem()
        if item is None:
            return
        website_name = item.text()
        title_chapter_source, image_naming = self.get_website_config_data(website_name)
        self.ui.lb_web_name_config_ws.setText(website_name)
        if title_chapter_source == "url":
            self.ui.rb_title_url_ws.setChecked(True)
        elif title_chapter_source == "html_title":    
            self.ui.rb_title_html_ws.setChecked(True)
        if image_naming == "website_filename":
            self.ui.rb_image_naming_kof_ws.setChecked(True)
        elif image_naming == "change_filename":    
            self.ui.rb_image_naming_rtsn_ws.setChecked(True)
        self.ui.verticalStackedWidget_ws.setCurrentIndex(0)

    def get_website_config_data(self, website_name):
        website_json = os.path.join(
            self.website_settings_path,
            f"{website_name}.json")
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
        
    def save_edit_web_config(self):
        item = self.ui.listWidget_ws.currentItem()
        if item is None:
            return
        website_name = item.text()
        if website_name:
            self.save_website_config_data(website_name)

    def save_website_config_data(self, website_name):
        if self.ui.rb_title_url_ws.isChecked():
            title_chapter_source = "url"
        elif self.ui.rb_title_html_ws.isChecked():
            title_chapter_source = "html_title"
        if self.ui.rb_image_naming_rtsn_ws.isChecked():
            image_naming = "change_filename"
        elif self.ui.rb_image_naming_kof_ws.isChecked():
            image_naming = "website_filename"
        data = {
            "title_chapter_source": title_chapter_source,
            "image_naming": image_naming
            }
        self.websites_list_display()
        try:
            website_json = os.path.join(
                self.website_settings_path,
                f"{website_name}.json")
            with open(website_json, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except:
            return