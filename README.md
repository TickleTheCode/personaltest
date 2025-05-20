# altGPT

altGPT is a web application that scans a webpage, identifies all images, and generates suggested `alt` text for them, especially those missing it. It uses a client-side AI model for caption generation and a Python Flask backend for fetching web content.

## Features

*   Fetches and parses HTML from a given URL.
*   Identifies all `<img>` tags.
*   Displays existing `alt` text.
*   Generates `alt` text suggestions for all images using a client-side transformer model (Xenova/vit-gpt2-image-captioning).
*   Provides a user-friendly interface to view current and suggested alt texts.
*   Allows copying of suggested alt texts.
*   Enables downloading results as a CSV file.
*   Includes a backend proxy for fetching images to bypass CORS issues.

## Architecture

The application consists of:

1.  **Frontend (`index.html`)**: A static HTML page with JavaScript that handles user interaction, AI model loading, image processing, and communication with the backend.
2.  **Backend (`app.py`)**: A Python Flask application that serves two main purposes:
    *   Fetching HTML content from a user-provided URL.
    *   Proxying image requests to avoid client-side CORS errors.

## Running the Application

To run altGPT, you need to set up the Python backend and then open the frontend in your browser.

### 1. Backend Setup

The backend requires Python 3.

a.  **Install Python**:
    If you don't have Python 3 installed, download and install it from [python.org](https://www.python.org/downloads/).

b.  **Create a Virtual Environment (Recommended)**:
    It's good practice to create a virtual environment for Python projects.
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

c.  **Install Dependencies**:
    The required Python packages are listed in `requirements.txt`. Install them using pip:
    ```bash
    pip install -r requirements.txt
    ```

d.  **Run the Flask Backend**:
    Start the Flask development server:
    ```bash
    python app.py
    ```
    Alternatively, you can use the `flask` command:
    ```bash
    export FLASK_APP=app.py # On Windows use `set FLASK_APP=app.py`
    flask run
    ```
    The backend will typically start on `http://127.0.0.1:5000/`.

### 2. Frontend Usage

a.  **Ensure Backend is Running**:
    The Python Flask backend (from step 1) must be running for the application to function.

b.  **Open `index.html`**:
    Open the `index.html` file directly in your web browser.
    *   **Note on Serving Locally**: While modern browsers can often open `index.html` directly from the file system and interact with a local backend (like `http://127.0.0.1:5000`), if you encounter any issues with JavaScript execution or API requests due to file protocol restrictions, you can serve `index.html` using a simple local HTTP server:
        ```bash
        python3 -m http.server 8080 
        ```
        Then navigate to `http://localhost:8080/index.html` in your browser. The key is that the Flask backend on port 5000 must be running independently.

c.  **Using the Tool**:
    1.  Once `index.html` is loaded, enter the URL of the webpage you want to analyze into the input field.
    2.  Click **Let's rock**.
    3.  The application will fetch the page content via the backend, find all images, and display them in a table.
    4.  For every image, it will attempt to generate a suggested `alt` text.
    5.  You can click **Copy** next to any suggestion or **Download CSV** to get all results.

### Important Notes:

*   **Internet Access**:
    *   The **Flask backend** requires internet access to fetch the content of the target URL and its images.
    *   The **client-side (`index.html`)** requires internet access to download the AI model files (from Hugging Face CDN) the first time it's run or when the browser cache is cleared.
*   **CORS**: The Flask backend includes a proxy to help mitigate Cross-Origin Resource Sharing (CORS) issues when fetching images.

## Command-line Image Scraper (`scrape_images.py`)

This repository also includes `scrape_images.py`, a simple Python script for downloading all images from a given webpage. This tool is independent of the main altGPT web application.

### Installation for `scrape_images.py`

1.  Ensure you have Python 3 installed.
2.  Install the required packages:
    ```bash
    pip install requests beautifulsoup4
    ```
    *Note: If you have already run `pip install -r requirements.txt` for the main application, these dependencies will already be installed as they are included in `requirements.txt`.*

### Usage of `scrape_images.py`

Run the script from your terminal with the target URL:

```bash
python scrape_images.py https://example.com/page [output_directory]
```

The script downloads all images found on the page into the specified output directory (defaults to `images`).

### Disclaimer

Ensure you have permission to download images from the target website. Always
check the site's terms of service and abide by copyright rules when using
`scrape_images.py`.

