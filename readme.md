###Group 4 - Project 3###
 (David Ma, Yonas Michael, Kyle Admire, Michel Gnancalo)

###Intro - Drug Related Crimes###
 DFW has always been a large city. It ranks #3, behind Houston and San Antonio, for population size in Texas. With multiple airports, sports teams, and great social settings, it provides for approximately 7.6 million people as of 2020. With that said there are certain areas that you may want to inform yourself about when cosidering living arrangements and entertainment. 
 
 Did you know that you can gather quite a bit of knowledge (i.e.: Address, Sex, Age, Arrest Time, Charge Type, Drug Type, etc.) made readily available right here online? Using the City of Dallas crime database, our group analyzed the details of the recent arrest reports in the city.

###Recap###

 #Find Data#
  Dallas Open Data - Police Arrests

 #Filter, Clean, Reduce Data#
  Using Jupyter Notebook​
  Data filter for only drug arrests​
  Began with 65 columns reduced to 11​
  Certain columns formatted for easier manipulation​
  Retrieved the latitude and longitude with GeoPy library​
  Created a function called json_data to create a JavaScript file from data based on daily, weekly, monthly, and yearly timeframes

#SQLite Database Connection#

#Python | Flask#

#Begin Web-Design#
  Created buttons for users to choose between the different timeframes ​
  Created a button to access the raw data ​

#JS Manipulation#
  Plotly​
  Created bar graph based on drugs​
  Created pie based on gender​
  Leaflet ​Heatmap plugin​
  Markercluster plugin​
