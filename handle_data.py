import pandas as pd

def handle_data(dic):
    actual_scores = []
    total_scores = []
    for score in dic.values():
        actual_scores.append(score[0])
        total_scores.append(score[1])
    a = pd.DataFrame(actual_scores)
    print(a.describe())


if __name__ == '__main__':
    dic = {
        'assignment_1': [5, 5],
        'assignment_2': [3, 5],
        'assignment_3': [5, 5],
        'assignment_4': [8, 10],
        'assignment_5': [2, 2],
        'assignment_6': [5, 5],
        'assignment_7': [4, 5],
        'assignment_8': [9, 10],
        'assignment_9': [0, 5],
        'assignment_10': [7, 10],
    }

    handle_data(dic)