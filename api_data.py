import pandas as pd
from sodapy import Socrata
from api_keys import *
import datetime
import sqlite3


def pull():
    # Unauthenticated client only works with public data sets. Note 'None'
    # in place of application token, and no username or password:
    client = Socrata("www.dallasopendata.com", app_token)

    #grab data from api
    #sdr7-6v3j is the dataset code from sodapy
    all_data = client.get_all("sdr7-6v3j")

    #turn into pandas df
    data_df = pd.DataFrame.from_records(all_data)
    data_df.sort_values(by='ararrestdate',ascending=False, inplace=True)
    
    #looking for only certain columns
    #'incidentnum', 'arrestnumber', 'ararrestdate', 'ararresttime', 'arpremises', 'arladdress', 'arlzip','sex','drugrelated','drugtype','age'
    data_df = data_df[['incidentnum', 'arrestnumber', 'ararrestdate', 'ararresttime', 'arpremises', 'arladdress', 'arlzip','sex','drugrelated','drugtype','age']]
    data_df = data_df.loc[((data_df['drugrelated']=='Yes') | (data_df['drugrelated']=='Uknown'))]

    for index, row in data_df.iterrows():
        split = row['ararrestdate'].split('T')
        row['ararrestdate'] = split[0]

    #create sqlite connection to transfer
    conn =sqlite3.connect('data/crime_data')
    c = conn.cursor()

    #create table
    c.execute('CREATE TABLE IF NOT EXISTS crime_test (incidentnum, arrestnumber, ararrestdate, ararresttime, arpremises, arladdress, arlzip, sex, drugrelated, drugtype, age)')
    conn.commit()

    #send pandas df to sql
    data_df.to_sql('crime_data', conn, if_exists='replace', index = False)


        