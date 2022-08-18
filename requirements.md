
# Software Requirements

## Vision

- The speed of Canvas, a web-based learning management system, has constantly been complained about in our time at 
Code Fellows. The need to login and wait for Canvas to load everything dynamically has become exhausting which is 
why we decided to allow users to have a faster, more personalized experience that takes Canvas information and 
delivers it to the user free from the restraints of Canvas.
- we will create a visualized, real-time score report also gives our students an ease to understand the study progress 
and standing status.

## User stories

- As a user I want to automatically log into my canvas account so to scrape my own data
- As a user I want to automatically import my assignment details to google calendar
- As a user I want to visualize my score as report for all my assignments
- As a user I want to choose any of my score category to display
- As a user I want all my info is always up-to-date


## Scope

- IN: Canvas pages (calendar page, assignment page and grades page)

- OUT: score data, assignment data


## Minimum Viable Product

- Scrape score data and assignment data from canvas website

- reconstruct assignment data to the right json format  for the calendar to use

- format grade data to csv file, so to use for data visualization

## Stretch Goal

- Add student's corresponding grades to calendar events
- Use pyscript to set up a HTML frontend

## Functional Requirements

1. scraper.py to scrape data
2. api.py to set up google calendar api
3. creat_json.py to reconstruct assignment data
4. learn_curve.py and comparison.py to do data visualization
5. test.py to test our code


## Data Flow
![](./DOM.png)

