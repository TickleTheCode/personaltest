# altGPT

altGPT scans a webpage to find all images and generates missing `alt` text using an open source language model.

## Usage

1. Open `index.html` in a browser.
2. Enter the URL of the page you want to analyze.
3. Click **Let's rock** to fetch the page and inspect each image.
4. For images without an `alt` attribute, the tool generates a suggestion and displays it in a table.
5. Click **Copy** to copy a suggested `alt` text or **Download CSV** to download all results.

Internet access is required to fetch the target page and load the LLM.

## Command-line Image Scraper

If you need a standalone tool to download images from a web page, this repository includes a simple Python script `scrape_images.py`.

### Installation

1. Ensure you have Python 3 installed.
2. Install the required packages:

   ```bash
   pip install requests beautifulsoup4
   ```

### Usage

Run the script with the target URL:

```bash
python scrape_images.py https://example.com/page [output_directory]
```

The script downloads all images found on the page into the specified output directory (defaults to `images`).

