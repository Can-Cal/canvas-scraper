import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import re, os

def scores_compared_with_mean(choice):
    df = pd.read_csv('current_graded_scores.csv')

    g_s = df.loc[df['assignment_title'].str.contains(f"{choice}"), ['graded_score']]
    g_m = df.loc[df['assignment_title'].str.contains(f"{choice}"), ['assignment_mean']]

    index = df.loc[df['assignment_title'].str.contains(f"{choice}"), ['assignment_title']]

    GS = g_s['graded_score'][0:]
    GM = g_m['assignment_mean'][0:]

    labels = [ re.sub(r'\D+', "", i) if re.search(r'\d', i) else re.sub(r"(?:\w+:)", "", i) for i in index['assignment_title'][0:] ]

    x = np.arange(len(labels))
    width= 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, GS, width, label='score')
    rects2 = ax.bar(x + width/2, GM, width, label='mean')

    ax.set_ylabel('Scores')
    ax.set_title(f'{choice} - each score compared with mean score')
    ax.set_xticks(x, labels)
    ax.legend()

    fig.set_size_inches(20.0, 10.5)

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    if not os.path.isdir('visualization'):
        os.mkdir('./visualization')
    plt.savefig(f'./visualization/comparison-{choice}.png')
    plt.show()

if __name__ == '__main__':
    scores_compared_with_mean('Code Challenge')
    scores_compared_with_mean('Read')
    scores_compared_with_mean('Career')
    scores_compared_with_mean('Lab')