import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data_GME = pd.read_csv(r"GME_stock.csv")

print(data_GME.info())
print(data_GME.columns)
print(data_GME.head())