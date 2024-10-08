"""
========================================================
        Web Scraping Script
========================================================
Author: Gattuzzo0
Date: October 7th 2024

Description:
------------
This script uses Selenium WebDriver to take web scraped data and puts it into a CSV file
automates the process of collecting information from websites and organizing it into a structured format. 
After scraping, the script processes the data as needed and writes it into a CSV (Comma-Separated Values) 
file using modules like csv or pandas. 

Functionalities:
----------------
- Configures Chrome to download files automatically.
- Scrapes a webpage and convert it to a dataset (Pandas dataframe)

Usage:
------
Ensure that Chrome WebDriver is installed and accessible. 
Run the script to download the required PDFs.

Dependencies:
-------------
- Selenium: `pip install selenium`

"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os 

# Configurar las opciones del navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Ejecuta Chrome en modo headless
#options.add_argument('--window-size=1920,1080')  # Opcional: tamaño de la ventana

# Establecer el directorio de descarga
script_dir = os.path.dirname(os.path.abspath(__file__))
download_dir = os.path.abspath(os.path.join(script_dir,'..' ,'data', 'WebScrap_CSVs'))

# Crear el directorio si no existe
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

prefs = {
    'download.default_directory': download_dir,
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'plugins.always_open_pdf_externally': True,
    'plugins.plugins_disabled': ['Chrome PDF Viewer'],
    'profile.default_content_setting_values.automatic_downloads': 1,
    'profile.default_content_settings.popups': 0,
}
options.add_experimental_option('prefs', prefs)

# Inicializar el WebDriver (en este caso, Chrome) con las opciones configuradas
driver = webdriver.Chrome(options=options)


# Define the base URL
base_url = "https://www.dripcapital.com/hts-code/"

# Initialize an empty list to store data
data = []

# Loop over sections
for section in range(1, 100):
    section_str = str(section).rjust(2, '0')
    section_url = base_url + section_str
    print(f"Scraping Chapters of Section {section_str} from URL: {section_url}")
    driver.get(section_url)

    # Wait for the chapters to load
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, f"//a[contains(@href, '/hts-code/{section_str}/')]")
            )
        )
    except Exception as e:
        print(f"Error loading section page {section_url}: {e}")
        continue

    # Extract chapter numbers from links
    chapter_links = driver.find_elements(
        By.XPATH, f"//a[contains(@href, '/hts-code/{section_str}/')]"
    )
    chapter_numbers = set()
    for link in chapter_links:
        href = link.get_attribute('href')
        parts = href.strip('/').split('/')
        if len(parts) >= 5 and parts[-1].isdigit():
            chapter_numbers.add(parts[-1])

    # Loop over chapters
    for chapter in sorted(chapter_numbers):
        chapter_str = str(chapter).rjust(2, '0')
        chapter_url = f"{base_url}{section_str}/{chapter_str}"
        print(
            f"Scraping Parts and Subparts of Section: {section_str}, Chapter: {chapter_str} from URL: {chapter_url}"
        )
        driver.get(chapter_url)

        # Wait for the content to load
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//h5[@class='MuiTypography-root MuiTypography-h5']")
                )
            )
        except Exception as e:
            print(f"Error loading chapter page {chapter_url}: {e}")
            continue

        # Extract HTS codes and descriptions
        h5_elements = driver.find_elements(
            By.XPATH, "//h5[@class='MuiTypography-root MuiTypography-h5']"
        )
        if not h5_elements:
            print(f"No items found on {chapter_url}")
            continue

        for h5 in h5_elements:
            try:
                parent_element = h5.find_element(By.XPATH, "..")
                text = parent_element.text.strip()
                lines = text.split('\n')

                if len(lines) >= 2:
                    #hts_code = lines[0].strip()
                    #Remove the prefix 'HTS Code' fro every row
                    hts_code = lines[0].replace('HTS Code ', '').strip()
                    description = ' '.join(lines[1:]).strip()
                    data.append({'HTS code': hts_code, 'Description': description})
                else:
                    print(f"Unexpected format at {chapter_url}: {text}")
            except Exception as e:
                print(f"Error extracting data from item on {chapter_url}: {e}")

        print("\n")  # Add a newline for better readability between chapters

# Close the browser
driver.quit()

# Create a pandas DataFrame from the data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv(os.path.join(download_dir, 'hts_codes_WebScrapped.csv'), index=False)

print("Data has been saved to {download_dir}/hts_codes_WebScrapped.csv")