from playwright.sync_api import sync_playwright

try:
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://google.com")
    page.screenshot(path="screenshot.png")

except Exception as e:
    print(f"An error occurred: {e}")

