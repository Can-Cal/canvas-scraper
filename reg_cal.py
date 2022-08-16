import re


regex_front = r"(?:calendar\?include_contexts=course_\/\r?\n|\r/)"
regex_new_line = r"/\r?\n|\r/"
regex_back = r"(?:\s&month=\d{2}&year=\d{4}#assignment_)"

with open("updated_text.ics") as f:
    x = f.readlines()


for count, string in enumerate(x):
    if "URL" in string:
        x[count] = re.sub(regex_front, "", string)
        x[count] += x[count+1]
        del x[count+1]

print(x)

# new_string = ""
#
# for string in x:
#     new_string += string

# print(x)
# for string in x:
#     if regex_front in string:
        # combine url string and next list index


# y = re.sub(regex_front, "courses/", x)
#
# z = re.sub(regex_back, "/assignments/", y)
# # a = re.sub("\s", "", z)
# print(z)
# #
# with open("./updated_text.ics", 'w') as file:
#     file.write(new_string)