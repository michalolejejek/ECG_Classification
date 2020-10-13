import pandas as pd

print("train data filename: ")
filename_train = input()
print("test data filename: ")
filename_test = input()

train_df = pd.read_csv(filename_train, header = None)
test_df = pd.read_csv(filename_test, header = None)

train_df.to_pickle("train.pkl")
test_df.to_pickle("test.pkl")
