# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 07:19:30 2022

@author: nites
"""

import requests 
from bs4 import BeautifulSoup
import json
import pandas as pd 
import matplotlib as plt


base_url = 'https://understat.com/match/'
match = str(input('Please enter the match id: '))
url = base_url + match 

url

res = requests.get(url)
soup = BeautifulSoup(res.content, 'lxml')
scripts = soup.find_all('script')

strings = scripts[1].string

#%%
# strip unnecessary symbols and get only JSON data 
ind_start = strings.index("('")+2 
ind_end = strings.index("')") 
json_data = strings[ind_start:ind_end] 
json_data = json_data.encode('utf8').decode('unicode_escape')

#convert string to json format
data = json.loads(json_data)
#%%
data
#%%
#coordinates
x = []
y = []
#expected goals 
xG = []
#result of the shot taken
result = []

team = []
#data from away matches
data_away = data['a']
#data from home matches
data_home = data['h']

#appending the data to the lists for home matches 
for index in range(len(data_home)):
    for key in data_home[index]:
        if key == 'X':
            x.append(data_home[index][key])
        if key == 'Y':
            y.append(data_home[index][key])
        if key == 'h_team':
            team.append(data_home[index][key])
        if key == 'xG':
            xG.append(data_home[index][key])
        if key == 'result':
            result.append(data_home[index][key])

#appending the data to the lists for away matches 
for index in range(len(data_away)):
    for key in data_away[index]:
        if key == 'X':
            x.append(data_away[index][key])
        if key == 'Y':
            y.append(data_away[index][key])
        if key == 'a_team':
            team.append(data_away[index][key])
        if key == 'xG':
            xG.append(data_away[index][key])
        if key == 'result':
            result.append(data_away[index][key])

#%%
#dataframe creation 
col_names = ['x','y','xG','result','team']
df = pd.DataFrame([x,y,xG,result,team],index=col_names)
#transposing the dataframe 
df = df.T
#%%
df
#%%
#saving scrapped data to csv
to_csv = df.to_csv('I:\mlProject\scrappedData.csv')
#%%
#converting the string to float for analysis 
df['x'] = pd.to_numeric(df['x'], downcast="float")
df['y'] = pd.to_numeric(df['y'], downcast="float")
df['xG'] = pd.to_numeric(df['xG'], downcast="float")

#analysis for the x coordinates
df['x'].mode()
df['x'].mean()
df['x'].median()

#analysis for the x coordinates
df['y'].mode()
df['y'].mean()
df['y'].median()

#analysis for the expected goal
df['xG'].mode()
df['xG'].mean()
df['xG'].median()
stdGoal = df['xG'].std()
print(stdGoal)

#%%
#graph plotting

#relation between x and y coordinate
df.plot(kind='line', x = 'x', y = 'y', xlabel = 'X-Coordinate', ylabel = 'Y-Coordinate', title='Relation between X & Y')


df.groupby('team')['result'].count().plot(kind='bar', xlabel = 'Teams', ylabel = 'No. of Attempts Made', title='Shots Taken by Each Team')
plt.show()

df.groupby('result')['result'].count().plot(kind='bar', xlabel = 'Result of Shot taken', ylabel = 'No. of Shots', title='Shot Categories')
plt.show()

df.groupby('result')['team'].count().plot(kind='bar', xlabel = 'Result of Shot taken', ylabel = 'No. of Shots', title='Shot Categories')
plt.show()

df.groupby('result', 'team')['team'].count().plot(kind='bar', xlabel = 'Result of Shot taken', ylabel = 'No. of Shots', title='Shot Categories')
plt.show()
