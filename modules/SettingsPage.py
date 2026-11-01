from PySide6.QtWidgets import  QFileDialog
import os
import json

from ui.ui_mainwindow import Ui_MainWindow
class SettingsPage:
    def __init__(self, ui:Ui_MainWindow):
        self.ui = ui
        self.output_path = ''
        self.set_output_path()

    def set_output_path(self):
        settings_file = "settings.json"
        if os.path.exists(settings_file):
            with open(settings_file, "r", encoding="utf-8") as f:
                settings = json.load(f)
            output_path = settings.get("downloads_directory", "./downloads")
        else:
            output_path = os.path.abspath("./downloads")
            settings = {
                "downloads_directory": output_path
            }
            with open(settings_file, "w", encoding="utf-8") as f:
                json.dump(settings, f, indent=4)
        os.makedirs(output_path, exist_ok=True)
        self.ui.le_output_path.setText(output_path)
        

    def load_settings(self):
        with open("settings.json", "r") as file:
            self.settings_json = json.load(file)
        return self.settings_json
    
    def select_output_path(self):

        output_path = QFileDialog.getExistingDirectory(None,"Select Folder","")
        if output_path:
            settings_file = "settings.json"
            settings = {}
            if os.path.exists(settings_file):
                with open(settings_file, "r", encoding="utf-8") as f:
                    settings = json.load(f)
            settings["downloads_directory"] = output_path
            with open(settings_file, "w", encoding="utf-8") as f:
                json.dump(settings, f, indent=4)
            os.makedirs(output_path, exist_ok=True)
            self.ui.le_output_path.setText(output_path)
            
