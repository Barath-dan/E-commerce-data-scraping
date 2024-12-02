# E-commerce-data-scraping
A Python-based web scraper that extracts laptop details (name, processor, RAM, OS, SSD, price, and product link) from Flipkart using Selenium and BeautifulSoup.

---

## Features

- Scrapes details of laptops, including:
  - **Name**
  - **Processor**
  - **RAM**
  - **Operating System**
  - **SSD Storage**
  - **Price**
  - **Product Link**
- Utilizes **Selenium** for dynamic webpage interaction.
- Extracts structured data using **BeautifulSoup**.
- Paginates through Flipkart search results until the last page.

---

## Prerequisites

To run this project, ensure you have the following installed:

- Python (>= 3.7)
- Google Chrome Browser
- ChromeDriver (compatible with your Chrome version)
- Required Python libraries:
  - `selenium`
  - `bs4`

The scraper will begin extracting laptop data page by page. Once the process is complete, the details will be printed to the terminal.

## Notes

-Browser Automation: The script uses Selenium to interact with Flipkart's dynamically loaded content.
-Page Limit: The scraper automatically detects the last page and stops execution after scraping all pages.
-Legal Disclaimer: Ensure compliance with Flipkart’s terms of service before scraping data.
