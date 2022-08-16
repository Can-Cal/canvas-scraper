import re

regex_front = r"(?:calendar\?include_contexts=course_)"
regex_new_line = r"[\n]"
regex_back = r"(?:\s&month=\d{2}&year=\d{4}#assignment_)"
regex_back2 = r"(?:\s&month=\d{2}&year=\d{4}#calendar_event_)"

assignment_list = []
date_list = []
url_front_list = []
url_back_list = []
complete_url_list = []
updated_date_list = []


def create_json(file):
    with open(file) as f:
        unparsed_data = f.readlines()

    global assignment_list
    global date_list
    global url_front_list
    global url_back_list
    global complete_url_list
    global updated_date_list

    for string in unparsed_data:
        if "SUMMARY" in string:
            string = re.sub("SUMMARY:", "", string)
            string = re.sub(regex_new_line, "", string)
            # print(string + "\n")
            assignment_list.append(string)
        if "DTSTART" in string:
            if "VALUE" in string:
                string = re.sub("DTSTART;VALUE=DATE;VALUE=DATE:", "", string)
            else:
                string = re.sub("DTSTART:", "", string)
            string = re.sub(regex_new_line, "", string)
            # print(string + "\n")
            date_list.append(string)
        if "URL:" in string:
            string = re.sub("URL:", "", string)
            string = re.sub(regex_front, "courses/", string)
            # print(string + "\n")
            url_front_list.append(string)
        if "month" in string:
            string = re.sub(regex_back, "/assignments/", string)
            string = re.sub(regex_back2, "/assignments/", string)
            # print(string + "\n")
            url_back_list.append(string)

    for count, string in enumerate(url_front_list):
        string = url_front_list[count] + url_back_list[count]
        string = re.sub(regex_new_line, "", string)
        complete_url_list.append(string)

    # *** Helper Function ***
    for date in date_list:
        word = ''
        # if len(date) > 14:
        for count, char in enumerate(date):
            if count == 4 or count == 6:
                word += '-'
            if count == 11 or count == 13:
                word += ':'
            if char != 'Z':
                word += char
        if len(date) > 14:
            updated_date_list.append(word)
        else:
            updated_date_list.append(word + "T00:00:00")

    with open("events.json", "w") as file:
        file.write("[")
        for count, event in enumerate(assignment_list):
            file.write("{\n")
            file.write(f"\"summary\": \"{assignment_list[count]}\",\n")
            file.write(f"\"description\": \"{complete_url_list[count]}\",\n")
            file.write("\"start\": {\n")
            file.write(f"\"dateTime\": \"{updated_date_list[count]}\",\n")
            file.write(f"\"timeZone\": \"America/Los_Angeles\"\n")
            file.write("},\n")
            file.write("\"end\": {\n")
            file.write(f"\"dateTime\": \"{updated_date_list[count]}\",\n")
            file.write(f"\"timeZone\": \"America/Los_Angeles\"\n")
            file.write("}\n")
            file.write("},\n")
        file.write("]")

