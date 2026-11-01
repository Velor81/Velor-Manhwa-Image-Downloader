from bs4 import BeautifulSoup
from .custom_request import Custom_Request
import re
from urllib.parse import urlparse

c_request = Custom_Request()
allowed_extensions = ["jpg", "png", "webp", "jpeg", "gif"]

def get_all_imgs_without_tag(url, find_all_by_img_or_a="img", response=None):
    if response is None:
        response = c_request.send_request(url)
    if response:
        soup = BeautifulSoup(response.content, 'html.parser')
        elements = soup.find_all(find_all_by_img_or_a)
        image_urls = []
        for element in elements:
            if find_all_by_img_or_a == "img":
                for attr in ['src', 'data-src', 'data-lazy-src']:
                    if attr in element.attrs:
                        value = element[attr].strip()
                        if value and value not in image_urls and value.startswith("http"):
                            image_urls.append(value)
            elif find_all_by_img_or_a == "a":
                if 'href' in element.attrs:
                    value = element['href'].strip()
                    if value and value not in image_urls and value.startswith("http") and value.endswith(tuple(allowed_extensions)):
                        image_urls.append(value)
        return image_urls
    else:
        return None
    
def get_all_images_without_tag_using_re(url, response=None):
    if response is None:
        response = c_request.send_request(url)
    if response:
        matches = re.findall(r'https?://[^\s"\']+\.(?:jpg|jpeg|png|webp|gif|avif)', response.text)
        image_urls = []
        for img in matches:
            if urlparse(img).scheme in ("http", "https"):
                image_urls.append(img)
        return image_urls
    else:
        return None
