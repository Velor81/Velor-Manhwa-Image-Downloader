import re
from bs4 import BeautifulSoup
from .custom_request import Custom_Request

c_request = Custom_Request()

def sanitize_title(title):
    return re.sub(r'[<>:"/\\|?*]', '', title)

def sanitize_chapter(title):
    title = title.replace('.', '-')
    # 2. Remove illegal characters (but NOT hyphens)
    return re.sub(r'[<>:"/\\|?*]', '', title)

def extract_title_from_urls(url):
    url_splited = url.strip('/').split('/')
    chapter_title = url_splited[-1].strip()
    manhwa_title = url_splited[-2].replace('-', ' ').strip().title()
    # Define a regex pattern to match a hyphen with a letter on the left and a number on the right
    pattern = re.compile(r'(?<=[a-zA-Z])-(?=\d)')
    
    chapter_title = pattern.sub(' ', chapter_title).title()
    if manhwa_title:
        manhwa_title = sanitize_title(manhwa_title)
    if chapter_title:
        chapter_title = sanitize_chapter(chapter_title)
    return manhwa_title, chapter_title

def get_manhwa_title_only_manhwaPage(url):
    url_splited = url.strip('/').split('/')
    manhwa_title = url_splited[-1].replace('-', ' ').strip().title()
    if manhwa_title:
        manhwa_title = sanitize_title(manhwa_title)
    return manhwa_title

def extract_title_from_html_title(url, response=None):
    if response is None:
       response = c_request.send_request(url)
    if response:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip()
        text = " ".join(title.split()) 
        patterns = [
            r"(Chapter\s+\d+(?:\.\d+)?)",
            r"(Episode\s+\d+(?:\.\d+)?)",
            r"(Ch\.?\s*\d+(?:\.\d+)?)",
            r"(Ep\.?\s*\d+(?:\.\d+)?)",
            r"(\d+(?:\.\d+)?)",
        ]
        for pattern in patterns:
            m = re.findall(pattern, text, re.IGNORECASE)
            if m:
                chapter = m[-1]
                title, x = text.rsplit(chapter, 1)
                title = title.strip().rstrip(" -|:–")
                chapter = chapter.strip().rstrip(" -|:–")
                title = sanitize_title(title)
                chapter = sanitize_chapter(chapter)
                return title, chapter
        return None, None
    return None, None