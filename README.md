
# Velor Manhwa Image Downloader

A Python desktop application for extracting, downloading, and organizing Manhwa chapter images.

The application uses a general-purpose image extraction approach instead of relying on website-specific rules that require frequent updates whenever websites change their domains or structures.

## Screenshot
![Velor Manhwa Image Downloader v1.0] (./screenshots/queue-downloading.PNG)

## Wach The App In Action On Youtube
https://www.youtube.com/watch?v=M-7K7YoSnSY

## Features

- Download images from Manhwa chapter pages.
- Add multiple chapter URLs to a download queue.
- Automatically organize downloaded images into chapter folders.
- Extract chapter names from URLs or optional HTML tags.
- Configure website settings and download locations.

## Note

Some websites protected by Cloudflare or similar security systems may block automated requests, preventing the application from accessing or extracting images.

Website compatibility is not guaranteed.

## Technologies

- Python
- PySide6
- Requests
- BeautifulSoup4

## License

MIT License