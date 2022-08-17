import pandas as pd

read_file = pd.read_csv(r'./output.txt')
read_file.to_csv(r'./output.csv', index=None)

