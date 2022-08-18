import scraper
from scraper import assignment_link
import api
from playwright.sync_api import sync_playwright
import create_json
import requests

def can_cal():
    with sync_playwright() as playwright:
        scraper.welcome()
        scraper.run(playwright)
        response = requests.get(scraper.assignment_link)
        create_json.create_json(response.content.decode('utf-8'))
        api.main()

if __name__ == '__main__':
    can_cal()
