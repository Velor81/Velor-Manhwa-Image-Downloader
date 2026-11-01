import requests
import time
headers_list = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
    },
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'Referer': 'https://www.google.com/',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
    },
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
]

class Custom_Request:
    def __init__(self):
        self.headers = headers_list
    def send_request(self, url):
        attempt = 0
        max_retries = 10
        response = None
        header_index = 0
        without_header = False
        while attempt < max_retries:
            try:
                if without_header:
                    response = requests.get(url, timeout=5)
                else:
                    response = requests.get(url, headers=self.headers[header_index],  timeout=5)
                response.raise_for_status()
                return response
            except (requests.exceptions.Timeout,
                    requests.exceptions.ConnectionError) as e:
                attempt += 1
                print(f"Attempt {attempt} failed ({type(e).__name__}): {e}")
            except requests.exceptions.HTTPError as e:
                status = e.response.status_code
                if status in (400, 404):
                    print("Permanent error, stopping retries.")
                    break
                elif status in (401, 403):
                    print(status)
                    if header_index < 2:
                        header_index +=1
                    elif not without_header:
                        without_header = True
                    else:
                        break
            except requests.exceptions.RequestException as e:
                print(f"{type(e).__name__}: {e}")
                attempt += 1

            if attempt < max_retries:
                wait_time = 5 * (attempt ** 2)
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print("All attempts failed.")
                return None

