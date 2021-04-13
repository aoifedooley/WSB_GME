import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data_WSB = pd.read_csv(r"reddit_wsb.csv")

# FILL NA
print(data_WSB.isnull().sum())
fill_body = data_WSB.fillna("n/a")
print(fill_body.isnull().sum())
print(fill_body["body"])

# DROP DUPLICATES
unique_posts = data_WSB.drop_duplicates(subset=["title"])
print(data_WSB.shape, unique_posts.shape)

# COLUMNS
print("COLUMNS")
print(data_WSB.columns)
print("")

# SEPARATE TIMESTAMP COLUMN TO DATE AND TIME
data_WSB["date"] = pd.to_datetime(data_WSB["timestamp"]).dt.date
data_WSB["time"] = pd.to_datetime(data_WSB["timestamp"]).dt.time

print(data_WSB.columns)

pd.set_option('display.max_columns', None)
print(data_WSB.head())
print(data_WSB.shape)


