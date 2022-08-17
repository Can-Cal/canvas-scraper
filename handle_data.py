import pandas as pd

def handle_data(dic):
    """
    Takes in a dictionary that contains assignments data and handles data for analysis.

    :param dic: dictionary, key: assignments name; value: a list of scores, total scores, stats strings
    :return: None
    """
    lab_scores = []
    cha_scores = []
    for title, score in dic.items():
        if title[0:3] == "Lab":
            lab_scores.append(int(score[0]))
        elif title[0:4] == "Code":
            cha_scores.append(int(score[0]))
        x = split_digits(score[2])

    a = pd.DataFrame(lab_scores)
    b = pd.DataFrame(cha_scores)
    print(a.describe())
    print(b.describe())

def split_digits(words):
    """
    This method splits the strings(Mean, Median...) and statics data

    :param words: String that contains stats data for whole class
    :return: list, [ Mean, Median, High, UpperQuartile, Low, LowerQuartile]
    """
    result = []
    temp = ""
    for w in words:
        if w.isdigit() or w == ".":
            temp += w
        else:
            if len(temp) > 0:
                result.append(temp)
            temp = ""
    return result[0:6]


if __name__ == '__main__':
    #Sample data for testing.
    dic = {
        'Code Challenge: Class 1': ['5', '5', 'Mean:3.65Median:4.5High:5UpperQuartile:5Low:0LowerQuartile:2.75Median4.5,High5.0,Low0.0YourScore:5.0outof5'],
        'Code Challenge: Class 2': ['3', '5', 'Mean:3.7Median:5High:5UpperQuartile:5Low:0LowerQuartile:2.88Median5.0,High5.0,Low0.0YourScore:3.0outof5'],
        'Lab: 3': ['5', '5', 'Mean:4.95Median:5High:5UpperQuartile:5Low:4LowerQuartile:5Median5.0,High5.0,Low4.0YourScore:5.0outof5'],
        'Lab: 4': ['8', '10', 'Mean:8.65Median:10High:10UpperQuartile:10Low:2LowerQuartile:8Median10.0,High10.0,Low2.0YourScore:8.0outof10'],
        'Learning Journal: Class 5': ['2', '2', 'Mean:1.5Median:2High:2UpperQuartile:2Low:0LowerQuartile:1.5Median2.0,High2.0,Low0.0YourScore:2.0outof2'],
        'Code Challenge: Class 6': ['5', '5', 'Mean:4.55Median:5High:5UpperQuartile:5Low:0LowerQuartile:5Median5.0,High5.0,Low0.0YourScore:5.0outof5'],
        'Code Challenge: Class 7': ['4', '5', 'Mean:3.58Median:4High:5UpperQuartile:4.63Low:0LowerQuartile:3Median4.0,High5.0,Low0.0YourScore:4.0outof5'],
        'Lab: 8': ['9', '10', 'Mean:7.6Median:9High:10UpperQuartile:10Low:0LowerQuartile:7Median9.0,High10.0,Low0.0YourScore:9.0outof10'],
        'Code Challenge: Class 9': ['2', '5', 'Mean:4.75Median:5High:5UpperQuartile:5Low:0LowerQuartile:5Median5.0,High5.0,Low0.0YourScore:2.0outof5'],
        'Lab: 10': ['7', '10', 'Mean:5.13Median:5High:10UpperQuartile:9Low:0LowerQuartile:2Median5.0,High10.0,Low0.0YourScore:7.0outof10'],
    }

    handle_data(dic)

    ###Run this test to see the result###
    #print(split_digits('Mean:5.13Median:5High:10UpperQuartile:9Low:0LowerQuartile:2Median5.0,High10.0,Low0.0YourScore:9.0outof10'))