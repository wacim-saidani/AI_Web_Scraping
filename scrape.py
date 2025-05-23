from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
AUTH = 'brd-customer-hl_6b1e5a77-zone-ai_scraper_1:v255q2g39440'
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'


def scrape_website(website):
    
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print('Connected! Navigating...')
        driver.get(website)
        driver.get_screenshot_as_file('./page.png')
        html = driver.page_source
        return(html)

def get_body(html):
    soup=BeautifulSoup(html,"html.parser")
    body=soup.body
    if body:
        return str(body)
    return ""

def clean_body(body):
    soup=BeautifulSoup(body,"html.parser")
    for style_script in soup(["style","script"]):
        style_script.extract()
    cleaned_content=soup.get_text(separator="\n")
    cleaned_content="\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    return cleaned_content

def split_cleaned_content(cleaned_content,max_length=6000):
    return[ cleaned_content[i:i+max_length] for i in range(0,len(cleaned_content),max_length)
        
    ]
    