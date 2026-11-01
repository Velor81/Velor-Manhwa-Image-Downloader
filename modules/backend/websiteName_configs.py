import json
from urllib.parse import urlparse

def get_website_name_from_url(url):

    # Example: 'https://www.websiteName.com/path'
    # Output: 'websiteName.com'

    domain = urlparse(url).netloc
    domain = domain.removeprefix('www.')

    website_name = '.'.join(domain.split('.')[-2:])
    return website_name