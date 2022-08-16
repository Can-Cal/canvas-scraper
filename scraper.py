from playwright.sync_api import sync_playwright


# with sync_playwright() as p:
#     browser = p.webkit.launch()
#     page = browser.new_page()
#     page.goto("https://www.google.co.jp")
#     page.screenshot(path="pyout.png")
#     browser.close()

def run(playwright):
    browser = playwright.chromium.launch(headless=False, channel='chrome')
    # context = browser.new_context()

    page = browser.new_page()
    page.goto("https://canvas.instructure.com/courses/4916427/assignments")

    with page.expect_navigation():
        # page.click("//div/span[@class='ht_title']")
        titles = page.query_selector_all("//div/a['@class=ig-title']")
        for i in titles:
            print(i.text_content())
        page.wait_for_timeout(1000)
    page.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
