import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data_GME = pd.read_csv(r"GME_stock.csv")
data_WSB = pd.read_csv(r"reddit_wsb.csv")
# INFO
print("INFO")
print(data_WSB.info())
print("")
# COLUMNS
print("COLUMNS")
print(data_WSB.columns)
print("")
# INDEX
print("INDEX")
print(data_WSB.index)
print("")
# HEADER
print("HEADER")
print(data_WSB.head())
print("")
# SHAPE
print("SHAPE")
print(data_WSB.shape)
print("")
# DESCRIPTION
print("DESCRIPTION")
print(data_WSB.describe())
# VALUES
print("VALUES")
print(data_WSB.values)

x = data_GME['date'].head(5)
y1 = data_GME['high_price'].head(5)
y2 = data_GME['low_price'].head(5)

plt.gca().invert_xaxis() # REF: https://stackoverflow.com/questions/2051744/reverse-y-axis-in-pyplot

plt.plot(x,y1, marker="o", linestyle="-", color="r", label="high price")
plt.plot(x,y2,marker="*", linestyle="-.", color="b", label='low price')
plt.title("Plot of GME Stock Price")
plt.xlabel("Date")
plt.ylabel("Share Price")
plt.legend()
plt.tight_layout()
plt.show()