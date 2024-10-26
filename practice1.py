from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
from file import save_to_file


def scraping(keyword):

    try:
        # keyword = input("what do you want to search for?")

        p = sync_playwright().start()
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"https://www.wanted.co.kr/search?query={keyword}&tab=position")
        # page.goto("https://www.wanted.co.kr/search")
        
        # page.get_by_placeholder("검색어를 입력해 주세요.").fill("devops")
        # page.keyboard.down("Enter")
        
        # page.click("a#search_tab_position")

        for x in range(3):
            page.keyboard.down("End")
            # time.sleep(2)

        content = page.content()
        
        soup = BeautifulSoup(content, "html.parser")

        jobs = soup.find_all("div", class_="JobCard_container__REty8")
        jobs_list = []
        for job in jobs :
            link = f"https://www.wanted.co.kr{job.find('a')['href']}"
            title = job.find("strong",class_="JobCard_title__HBpZf").text
            company_name = job.find("span",class_="JobCard_companyName__N1YrF").text

            job = {
                "title" : title,
                "company_name" : company_name,
                "link" : link
            }
            jobs_list.append(job)

        # with open("jobs.csv", "w", newline="", encoding="utf-8") as file:  # Use 'with' for better file handling
        #     writer = csv.writer(file)
        #     writer.writerow(["Title", "Company"])  # Header

        #     for job in jobs_list:
        #         writer.writerow(job.values())

        # save_to_file(keyword, jobs_list)
        return jobs_list

    except Exception as e:
        print(f"An error occurred: {e}")

