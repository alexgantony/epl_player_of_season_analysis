import random
import time

from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth

url = "https://fbref.com/en/comps/9/stats/Premier-League-Stats"


def run(playwright, url):
    browser = playwright.chromium.launch(
        headless=False,
    )
    context = browser.new_context()
    page = context.new_page()

    page.goto(url)

    page.wait_for_load_state("load")
    time.sleep(random.uniform(2, 7))
    title = page.title()
    page_content = page.content()
    print(title)

    browser.close()


with Stealth().use_sync(sync_playwright()) as pw:
    run(pw, url)
