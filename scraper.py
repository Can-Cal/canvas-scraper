from playwright.sync_api import sync_playwright

import create_json
import requests
import api
from handle_data import handle_data

import getpass
import re

assignment_link = ""


def welcome():
    print("****************************************")
    print("** @_@ Welcome to Canvas Scraper @_@  **")
    print("****************************************")

def run(playwright):
    browser = playwright.chromium.launch(headless=False, channel='chrome')
    page = browser.new_page()
    user_email = 'guojiarui@gmail.com'  # input('Please input your Canvas account email:')
    password = '699622@Gr'  # getpass.getpass('Please input your Canvas password:')
    page.goto("https://canvas.instructure.com/calendar")
    page.fill('input#pseudonym_session_unique_id.ic-Input.text', user_email)
    page.fill('input#pseudonym_session_password.ic-Input.text', password)
    page.click('button[class="Button Button--login"]')

    page.goto("https://canvas.instructure.com/calendar")
    page.click('button[class="dialog_opener Button Button--link"]')
    page.wait_for_timeout(2000)

    global assignment_link
    assignment_link = page.query_selector('//p[@id="calendar-feed-box-lower"]/a')
    assignment_link = assignment_link.get_attribute("href")
    # response = requests.get(assignment_text)
    # create_json.create_json(response.content)

    # Dictionary: key: title, value: score
    dic = {}

    page.goto("https://canvas.instructure.com/courses/4916427/grades")
    # with page.expect_navigation():
    page.wait_for_timeout(5000)
    graded_titles = page.query_selector_all(
        "//tr[@class='student_assignment assignment_graded editable']/th[@class='title']/a")

    graded_actual_scores = page.query_selector_all(
        "//tr[@class='student_assignment assignment_graded editable']//span[@class='original_score']")
    graded_total_scores = page.query_selector_all(
        "//tr[@class='student_assignment assignment_graded editable']//td[@class='possible points_possible']")

    not_graded_titles = page.query_selector_all("//tr[@class='student_assignment editable']/th[@class='title']/a")
    not_graded_total_scores = page.query_selector_all(
        "//tr[@class='student_assignment editable']//td[@class='possible points_possible']")

    # Statistics for score data
    stats = page.query_selector_all("//tr[@class='comments grade_details assignment_graded']//tbody")

    index_stats = 0
    for index in range(len(graded_titles)):
        gas = re.sub(r"\s+", "", graded_actual_scores[index].text_content())
        gts = re.sub(r"\s+", "", graded_total_scores[index].text_content())
        each_stat = re.sub(r"\s+", "", stats[index_stats].text_content())

        if graded_titles[index].text_content() != "Roll Call Attendance" and gts != '0':
            dic[graded_titles[index].text_content()] = [gas,gts, each_stat]
            index_stats +=1
            print("Title: ", graded_titles[index].text_content(), "actual scores:", gas, "total scores:", gts, "stats:", each_stat)


    for index in range(len(not_graded_titles)):
        ngts = re.sub(r"\s+", "", not_graded_total_scores[index].text_content())
        dic[not_graded_titles[index].text_content()] = [0, ngts]

        print("title: ", not_graded_titles[index].text_content(), "actual scores: 0","total scores:", ngts )

    page.wait_for_timeout(5000)

    page.close()
    browser.close()

    """
    ####### checking lists length #######
    for i, j in dic.items():
        print(i, j)
    print("graded_titles: ", len(graded_titles))
    print("graded_actual_scores: ", len(graded_actual_scores))
    print("not_graded_titles: ", len(not_graded_titles))
    print("graded_total_scores", len(graded_total_scores))
    print("not_graded_total_scores", len(not_graded_total_scores))
    print("dic: ", len(dic))
    print("stats: ",len(stats))
    """

    handle_data(dic)


if __name__ == '__main__':
    welcome()
    with sync_playwright() as playwright:
        run(playwright)
        response = requests.get(assignment_link)
        create_json.create_json(response.content.decode('utf-8'))
