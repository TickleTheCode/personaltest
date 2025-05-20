import os
import sys
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


def scrape_images(url, out_dir="images"):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    os.makedirs(out_dir, exist_ok=True)

    count = 0
    for img in soup.find_all("img"):
        src = img.get("src")
        if not src:
            continue
        img_url = urljoin(url, src)
        try:
            img_resp = requests.get(img_url, stream=True)
            img_resp.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to download {img_url}: {e}")
            continue
        filename = os.path.basename(urlparse(img_url).path) or f"image_{count}.jpg"
        file_path = os.path.join(out_dir, filename)
        with open(file_path, "wb") as f:
            for chunk in img_resp.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        count += 1
        print(f"Saved {img_url} -> {file_path}")

    print(f"Downloaded {count} images to {out_dir}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scrape_images.py <URL> [output_dir]")
        sys.exit(1)
    scrape_images(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "images")

