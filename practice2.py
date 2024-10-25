from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv


url = "https://www.naver.com/"

try : 

        p = sync_playwright().start()
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        content = page.content()
        soup = BeautifulSoup(content, "html.parser")
        time.sleep(3)

        
        items = soup.find_all("li", class_="shortcut_item")
        print(items)

        items_db = []
        
        for item in items : 
            print("start")
            title = item.find("span",class_="service_name")
            link = item.find("a")["href"]
            print(title, link)
            item = {
                "title" : title,
                "link" : link
            }

            items_db.append(item)

        print(len(items_db))
   




except Exception as e :

    print(f"error occured {e}")

    