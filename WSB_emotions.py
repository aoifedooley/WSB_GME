import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import text2emotion as te
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from IPython.display import clear_output
import matplotlib.pyplot as plt
from raceplotly.plots import barplot

data = pd.read_csv(r"reddit_wsb.csv")

df=pd.DataFrame()
dn=data[data['weekday']=='Friday']
df['Emotion']=dn['dominant emotion']
df['Hour']=dn['hour']
df['Count']=[1]*len(df)
grouped_data=df.groupby(['Hour','Emotion']).sum()
ind=np.array(list(grouped_data.index))
df2=pd.DataFrame()
df2['Hour']=ind[:,0]
df2['Emotion']=ind[:,1]
df2['Count']=grouped_data.values
df2['Hour']=df2['Hour'].apply(lambda x : int(x))
df2.sort_values('Hour',inplace=True)
my_raceplot = barplot(df2,
                      item_column='Emotion',
                      value_column='Count',
                      time_column='Hour')

my_raceplot.plot(title = 'Emotion in the sub reddit section on Friday as the day continued',
                 item_label = 'Emotions',
                 value_label = 'Count (Total Count On That Day)',
                 frame_duration = 800)