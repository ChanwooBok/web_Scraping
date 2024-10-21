from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup


try:
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.wanted.co.kr/search")
    page.get_by_placeholder("검색어를 입력해 주세요.").fill("devops")
    page.keyboard.down("Enter")
    
    page.click("a#search_tab_position")

    for x in range(4):
        page.keyboard.down("End")
        time.sleep(3)
    content = page.content()
    
    soup = BeautifulSoup(content, "html.parser")

except Exception as e:
    print(f"An error occurred: {e}")

