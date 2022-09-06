import pandas as pd

df = pd.read_csv('./cities.csv', usecols=['City','Lat','Lng','Max Temp','Humidity','Cloudiness','Wind Speed','Country','Date'])
df.to_html('./cities.html')
