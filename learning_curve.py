import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory
#
# import os
#
# for dirname, _, filenames in os.walk('/kaggle/input'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))
def learn_curve():
    df = pd.read_csv("./current_graded_scores.csv")
    df['percent'] = df.graded_score.div(df.total_score) * 100
    ypoints = df['percent']
    plt.figure(figsize=(15, 10))
    plt.title('Student Learning Curve')
    plt.xlabel("Assignment numbers")
    plt.ylabel("Your score")
    plt.plot(ypoints, linestyle='dotted')
    plt.show()


if __name__ == '__main__':
    learn_curve()
