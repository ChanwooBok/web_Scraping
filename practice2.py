import cloudscraper
from bs4 import BeautifulSoup



all_jobs=[]
url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

def scrape(url):
  print(f"scraping {url}")
  scraper = cloudscraper.create_scraper()

  response = scraper.get(url)

  potato = BeautifulSoup(response.content, "html.parser")
  jobs = potato.find("section", class_="jobs").find_all("li")[1:-1]

  for job in jobs:     
    title = job.find("span",class_="title").text
    company,position,region = job.find_all("span",class_="company")
    url = job.find("div",class_="tooltip--flag-logo").next_sibling["href"]
    job_data = {
      "title":title,
      "company":company.text,
      "position":position.text,
      "region":region.text,
      "url":f"https://weworkremotely.com{url}"
    }
    all_jobs.append(job_data)

def get_pages(url):
  
  scraper = cloudscraper.create_scraper()
  response = scraper.get("https://weworkremotely.com/remote-full-time-jobs?page=1")
  potato = BeautifulSoup(response.content, "html.parser")
  return len(potato.find("div",class_="pagination").find_all("span",class_="page"))

total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")

for x in range(total_pages):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
    scrape(url)

print(len(all_jobs))



