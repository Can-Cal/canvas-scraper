from playwright.sync_api import sync_playwright
import getpass

assignment_link = ""

def run(playwright):
    browser = playwright.chromium.launch(headless=False, channel='chrome')
    # context = browser.new_context()
    user_email = input('Please input your Canvas account email:')
    password = getpass.getpass('Please input your Canvas password:')
    page = browser.new_page()
    page.goto("https://canvas.instructure.com/calendar")
    # page.goto("https://canvas.instructure.com/calendar#view_name=agenda&view_start=2022-07-18")
    page.fill('input#pseudonym_session_unique_id.ic-Input.text', user_email)
    page.fill('input#pseudonym_session_password.ic-Input.text', password)
    page.click('button[class="Button Button--login"]')

    page.click('button[class="dialog_opener Button Button--link"]')
    page.wait_for_timeout(2000)

    global assignment_link
    assignment_link = page.query_selector('//p[@id="calendar-feed-box-lower"]/a')
    print(assignment_link.get_attribute("href"))

    #Dictionary: key: title, value: score
    dic={}

    page.goto("https://canvas.instructure.com/courses/4916427/grades")
    with page.expect_navigation():
        page.wait_for_timeout(15000)
        graded_titles = page.query_selector_all("//tr[@class='student_assignment assignment_graded editable']/th[@class='title']/a")

        graded_actual_scores = page.query_selector_all("//span[@class='original_score']")
        graded_total_scores = page.query_selector_all("//tr[@class='student_assignment assignment_graded editable']//td[@class='possible points_possible']")

        not_graded_titles = page.query_selector_all("//tr[@class='student_assignment editable']/th[@class='title']/a")
        not_graded_total_scores = page.query_selector_all("//tr[@class='student_assignment editable']//td[@class='possible points_possible']")


        #Statistics for score data
        #stats = page.query_selector_all("//tr[@class='comments grade_details assignment_graded']//tbody")

        for index in range(len(graded_titles)):
            print("Title: ", graded_titles[index].text_content())
            print(f"actual scores: {graded_actual_scores[index].text_content()}")
            print(f"total scores: {graded_total_scores[index].text_content()}")

        for index in range(len(not_graded_titles)):
            print("title: ", not_graded_titles[index].text_content())
            print("actual scores: 0")
            print("total scores:", not_graded_total_scores[index].text_content())

    page.close()
    browser.close()

#For future reference
# def export_data(dic):
#     with open("scores.txt", "w") as f:
#         for k, v in dic:
#             f.write(f"{k}, {v}")

if __name__ == '__main__':
    with sync_playwright() as playwright:
        run(playwright)