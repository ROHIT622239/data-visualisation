import pandas as pd 
import ploty.express as px 
df = pd.read_csv('line chart.csv ')
fig = px.line(df,x='date',y='number of cases',color='country')
fig.show()
#px.bar
#px.scatter