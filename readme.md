Team-Members: Nitesh Kumar Vishwakarma, Mansi Dhiman 
Sap Id: 500082879, 500084419
Batch: B6(H), B6(H)

#IMPORTING-MODULES
'requests', 'BeautifulSoup', 'pandas', 'matplotlib' modules are imported for using them in script. 

#SETTING-URL 
a base url is defined i.e., 'https://understat.com/match/' after that the match id is taken from the user. after appending it to the base url. we get a final url from where the data scrapping will be performed in the project 

#REQUESTING-DATA-FROM-WEBSITE
from line 21 to 25 we request the content from the webiste. after requesting from the website we get a script file mixed up with json data. the script that we get after the request will be stored in the string. 

#STRIPING-JSON-DATA FROM THE SCRIPT
the JSON data is the one that we want for the analysis. so from line 29 to 32 JSON data is stripped from the script 

after that the JSON data that has been stipped off is loaded in the variable named data in line 35

#APPENDING DATA TO LISTS 
from line 39 to line 79 we are appending the data for home and away matches to the lists. 
the data which are appended are x and y coordinates and expected goals and the results. we iterate throught the data variable and breaking at the breakpoints and appending them in the respective list under respective columns. 

#DATAFRAME CREATION 
from 83 to 86 the list that are created in the above cell are converted into dataframe using pandas module 
but we need to transpose the dataframe to get in the required form 

#SAVING DATA FRAME IN CSV FILE 
in 91 line the dataframe is save in csv file

#CONVERSION FROM STRING TO NUMERIC
as the columns in the csv stores the data in the form of strings so to perform analysis we need to transform in to numeric fromat
from line 94 to 97 the the data in columns are transfromed into numeric form 

from 93 to 113 analysis is performed. mean mode and median are calculated. 

#GRAPH PLOTTING
in the last cell graphs between different attributes are plotted. 