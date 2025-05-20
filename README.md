# AccessibilityGPT

AccessibilityGPT scans a webpage for accessibility issues and suggests improvements.

## Usage

1. Open `index.html` in a browser.
2. Enter the URL of the page you want to check.
3. Click **Analyze** to run an accessibility audit using [axe-core](https://github.com/dequelabs/axe-core).
4. The tool then loads an open-source language model via [transformers.js](https://github.com/xenova/transformers.js) and generates recommendations based on the audit report.

Internet access is required to fetch the target page and load the LLM.
