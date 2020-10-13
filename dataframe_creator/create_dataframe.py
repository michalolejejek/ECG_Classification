import pandas as pd

train_df = pd.read_csv('train.csv', header = None)
test_df = pd.read_csv('test.csv', header = None)

train_df.to_pickle("train.pkl")
test_df.to_pickle("test.pkl")
