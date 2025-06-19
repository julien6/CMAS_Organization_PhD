import time
import random
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from rapidfuzz import fuzz
import bibtexparser

def extract_titles_from_bib(bib_file_path):
    with open(bib_file_path, 'r') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    titles = []
    for entry in bib_database.entries:
        if 'title' in entry:
            # Remove curly braces sometimes present in BibTeX titles
            clean_title = re.sub(r'[{}]', '', entry['title'])
            titles.append(clean_title.strip())
    return titles

def search_title_on_scholar(title, driver, threshold=98):
    base_url = "https://scholar.google.com/"
    driver.get(base_url)
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()
    search_box.send_keys(title)
    search_box.send_keys(Keys.RETURN)
    time.sleep(random.uniform(2, 4))  # Random delay to avoid blocking

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results = soup.find_all('h3', class_='gs_rt')
    for res in results:
        res_title = res.text
        similarity = fuzz.token_set_ratio(title.lower(), res_title.lower())
        if similarity >= threshold:
            return True  # Match found
    return False

def check_references(bib_file_path, chrome_driver_path):
    options = Options()
    options.add_argument("--headless")  # run in headless mode
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    bad_references = []
    titles = extract_titles_from_bib(bib_file_path)
    for idx, title in enumerate(titles):
        print(f"Checking ({idx+1}/{len(titles)}): {title}")
        try:
            found = search_title_on_scholar(title, driver)
            if not found:
                print(f'"{title}" was not found')
                bad_references.append(title)
        except Exception as e:
            print(f"Error while checking '{title}': {e}")
            bad_references.append(title)
        time.sleep(random.uniform(5, 10))  # Large delay between queries to be safe
    driver.quit()
    return bad_references

# Example usage:
bad_refs = check_references("./references.bib", "/usr/bin/chromedriver")
print("Bad references found:")
for ref in bad_refs:
    print(ref)
