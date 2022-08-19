import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
def learn_curve():
    df = pd.read_csv("./current_graded_scores.csv")
    df['percent'] = df.graded_score.div(df.total_score) * 100
    ypoints = df['percent']
    plt.figure(figsize=(15, 10))
    plt.title('Student Learning Curve')
    plt.xlabel("Assignment numbers")
    plt.ylabel("Your score")
    plt.plot(ypoints, linestyle='dotted')
    plt.savefig('./visualization/learn-curve.png')
    plt.show()

def each_learn_curve(choice):
    df = pd.read_csv("./current_graded_scores.csv")
    g_ = df.loc[df['assignment_title'].str.contains(f"{choice}"), ['graded_score', 'total_score']]
    ypoints = g_.graded_score.div(g_.total_score) * 100
    plt.figure(figsize=(15, 10))
    plt.title(f'Student Learning Curve For {choice}')
    plt.xlabel("Assignment numbers")
    plt.ylabel("Your score")
    plt.plot(ypoints, linestyle='dotted')
    if not os.path.isdir('visualization'):
        os.mkdir('./visualization')
    plt.savefig(f'./visualization/learning-curve-{choice}.png')
    plt.show()

if __name__ == '__main__':
    each_learn_curve("Lab")
    each_learn_curve("Code Challenge")
    each_learn_curve("Career")
    each_learn_curve("Read")
