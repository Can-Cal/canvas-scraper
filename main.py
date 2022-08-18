import scraper
from scraper import assignment_link
import api
from playwright.sync_api import sync_playwright
import create_json
import requests
import learning_curve
import scores_comparison

def can_cal():
    with sync_playwright() as playwright:
        scraper.welcome()
        scraper.run(playwright)
        response = requests.get(scraper.assignment_link)
        create_json.create_json(response.content.decode('utf-8'))
        api.main()


        user_choice = None
        graph_choice = None
        print("Would you like to have your data visualized? (y/n)")
        visualize_data = input("> ")
        if visualize_data == 'y':
            while graph_choice != "quit":
                print("""
                Would you like to see Learning Curve Graphs or Mean comparison graphs?
                ****              Enter 'Learning Curve' or 'Mean'                ****
                """)
                graph_choice = input("> ")
                if graph_choice == 'Mean':
                    while user_choice != "quit":
                        print("""
                            Welcome to our Data Visualization Center, please choose which data you would like to see:
                            * Enter 'Code Challenge' to see a graph comparing your Code Challenge grades with the rest 
                            of your class.
                            * Enter 'Lab' to see a graph comparing your Labs grades with the rest of your class.
                            * Enter 'Read' to see a graph comparing your Reading grades with the rest of your class.
                            * Enter 'Career' to see a graph comparing your Career grades with the rest of your class.
                            ***                 Enter 'quit' to go back to graph type selection                    ***
                            """)
                        user_choice = input("> ")
                        if user_choice == "Code Challenge" or user_choice == "Lab" or user_choice == "Read" or user_choice == "Career":
                            scores_comparison.scores_compared_with_mean(user_choice)
                        elif user_choice == "quit":
                            user_choice = None
                            break
                        else:
                            print("""
                            Sorry our Data Visualization Center is still working on generating graphs for that. Please
                            try selecting something from the list.
                            """)
                elif graph_choice == "Learning Curve":
                    while user_choice != "quit":
                        print("""
                            Welcome to our Data Visualization Center, please choose which data you would like to see:
                            * Enter 'Code Challenge' to see a comparing your scores on all Code Challenge assignments.
                            * Enter 'Lab' to see a comparing your scores on all Lab assignments.
                            * Enter 'Read' to see a comparing your scores on all Reading assignments.
                            * Enter 'Career' to see a comparing your scores on all Career assignments.
                            * Enter 'All' to see a graph comparing your score on all assignments with grades.
                            ***                 Enter 'quit' to go back to graph type selection                    ***
                            """)
                        user_choice = input("> ")
                        if user_choice == "All":
                            learning_curve.learn_curve()
                        elif user_choice == "Code Challenge" or user_choice == "Lab" or user_choice == "Read" or user_choice == "Career":
                            learning_curve.each_learn_curve(user_choice)
                        elif user_choice == "quit":
                            user_choice = None
                            break
                        else:
                            print("""
                            Sorry our Data Visualization Center is still working on generating graphs for that. Please
                            try selecting something from the list.
                            """)
                elif graph_choice == "quit":
                    print("Thank you for using our application!")

        elif visualize_data == 'n':
            print("Thank you for using our application!")


if __name__ == '__main__':
    can_cal()
