from playwright.sync_api import sync_playwright

def scrape_first_thirty_characters(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        content = page.content()
        browser.close()
    
    # Extract text content
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text()
    
    # Return only the first 30 characters
    return text[:30]
