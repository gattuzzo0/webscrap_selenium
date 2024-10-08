# Website Scraper Scripts
![image](https://github.com/user-attachments/assets/4667d7d7-ed75-44b2-86c3-77c620f95a57)

This repository contains two Python scripts designed to scrape websites for data and PDF files:

1. **Data Scraper**: Recursively navigates through web pages and extracts data into a CSV file.
2. **PDF Downloader**: Recursively navigates through web pages and downloads all available PDFs for later usage.

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Data Scraper](#data-scraper)
  - [PDF Downloader](#pdf-downloader)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Recursive Navigation**: Both scripts navigate through multiple pages automatically.
- **Data Extraction**: Extracts relevant information and saves it in a structured CSV format.
- **PDF Downloading**: Downloads all available PDF files from the targeted website.
- **Customizable**: Easily adjust the scripts to target different websites or data types.
- **Error Handling**: Includes basic error handling to manage exceptions and continue processing.

---

## Prerequisites

- **Python 3.11+**
- **Libraries**:
  - `requests`
  - `selenium`
  - `pandas` (optional, if using for CSV handling)

---

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/website-scraper-scripts.git
   cd website-scraper-scripts
   ```

2. **Create a Virtual Environment (Optional)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   *If `requirements.txt` is not provided, install dependencies manually:*

   ```bash
   pip install requests beautifulsoup4 urllib3 pandas
   ```

---

## Usage

### Data Scraper

**webscrap_selenium_toCSV.ipynb**

### PDF Downloader

**webscrap__selenium_PDF_Download.ipynb**

---

## Configuration

- **Target URLs**: Modify the `base_url` variable in each script to change the starting point.
- **Data Fields**: Adjust the parsing logic to extract different data elements.
- **Download Directory**: Change the `download_dir` variable to set where PDFs are saved.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -am 'Add your feature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

**Disclaimer**: Ensure you have permission to scrape the target websites and comply with their `robots.txt` file and terms of service. Unauthorized scraping may violate the website's policies or legal regulations.
