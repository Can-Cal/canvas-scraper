from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False, channel='chrome')
    # context = browser.new_context()
    user_email = input('Please input your Canvas account email:')
    password = input('Please input your Canvas password:')
    page = browser.new_page()
    page.goto("https://canvas.instructure.com/courses/4916427/assignments")
    # page.goto("https://canvas.instructure.com/calendar#view_name=agenda&view_start=2022-07-18")
    page.fill('input#pseudonym_session_unique_id.ic-Input.text', user_email)
    page.fill('input#pseudonym_session_password.ic-Input.text', password)
    page.click('button[class="Button Button--login"]')

    page.goto("https://canvas.instructure.com/calendar#view_name=agenda&view_start=2022-07-18")
    with page.expect_navigation():
        titles = page.query_selector_all("//div[@class='agenda-event__time']")
        # print(titles)
        for i in titles:
            # print(i.text_content())
            i = i.text_content()
        with open('./output.txt', 'w') as f:
            for i in titles:
                f.write(str(i) + "\n")

        page.wait_for_timeout(1000000)
    page.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
