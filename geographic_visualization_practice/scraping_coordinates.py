from bs4 import BeautifulSoup as bs 
import requests as r
import pandas as pd 

page = r.get('http://www.csgnetwork.com/llinfotable.html').content
soup = bs(page,'html.parser')

table = soup.find('table',{'bgcolor':"#FFFFFF"})
entries = table.find_all('tr')

country = []
capital = []
lat = []
lon = []
storage = [country,capital,lat,lon]

for i in entries[1:]:
    values = i.find_all('td')

    for k,v in zip(values,storage):
        v.append(k.contents[0])

data = pd.DataFrame({'country':country,'lat':lat,'lon':lon})
data.to_csv('country_lat_lon.csv',index=False)