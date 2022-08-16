from playwright.sync_api import sync_playwright
# from bs4 import BeautifulSoup

def welcome():
    print("****************************************")
    print("** @_@ Welcome to Canvas Scraper @_@  **")
    print("****************************************")

welcome()

# with sync_playwright() as p:
#     browser = p.webkit.launch()
#     page = browser.new_page()
#     page.goto("https://www.google.co.jp")
#     page.screenshot(path="pyout.png")
#     browser.close()


def run(playwright):
    user_email = 'guojiarui@gmail.com'  # input('Please input your Canvas account email:')
    password = '699622@Gr'  # input('Please input your Canvas password:')
    browser = playwright.chromium.launch(headless=False, channel='chrome')
    page = browser.new_page()

    page.goto("https://canvas.instructure.com/courses/4916427/")
    page.fill('input#pseudonym_session_unique_id.ic-Input.text', user_email)
    page.fill('input#pseudonym_session_password.ic-Input.text', password)
    page.click('button[class="Button Button--login"]')
    # page.goto("https://canvas.instructure.com/calendar#view_name=agenda&view_start=2022-07-18")
    # html = page.inner_html('#calendar-app')
    # print(html)
    # soup = BeautifulSoup(html, 'html.parser')

    page.goto("https://canvas.instructure.com/courses/4916427/grades")
    with page.expect_navigation():
        # page.click("//div/span[@class='ht_title']")

        page.wait_for_timeout(15000)
        titles = page.query_selector_all("//tbody")  # //div['agenda-event__time']
        print(titles)
        # for i in titles:
        #     # print(i.text_content())
        #     i = i.text_content()
        with open('./output.txt', 'w') as f:
            for i in titles:
                f.write(i.text_content() + "\n")

    page.wait_for_timeout(10000)

    page.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
