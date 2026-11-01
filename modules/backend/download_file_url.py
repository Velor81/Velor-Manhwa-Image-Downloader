
import os, re
from datetime import datetime
from .custom_request import Custom_Request
import os
import re
from urllib.parse import urlparse, unquote


c_request = Custom_Request()

def download_file(url, manhwa_title, chapter_title, output_path, rename_file=None,  stop_condition=None, response =None):
        if response is None:
            response = c_request.send_request(url)
        if response:


            # Extract filename from URL path, ignoring query parameters
            basename = os.path.basename(unquote(urlparse(url).path))

            # Get extension
            ext = os.path.splitext(basename)[1]

            if rename_file:
                filename = rename_file + ext
            else:
                filename = re.sub(r'[^a-zA-Z0-9._-]', '-', basename)

            output_folder_path = os.path.join(output_path, manhwa_title, chapter_title)
            os.makedirs(output_folder_path, exist_ok=True)

            file_path = os.path.join(output_folder_path, filename)
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):#to stop thread
                    if stop_condition and not stop_condition():
                        print("Download stopped by user.")
                        response.close()  
                        return
                    if chunk:
                        file.write(chunk)
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"File successfully downloaded [{current_time}]: {filename}")
        return None

