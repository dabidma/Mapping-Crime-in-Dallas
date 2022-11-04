import json
import sqlite3
import collections
import psycopg2
import datetime
import api_data

today = datetime.date.today()
week = today - datetime.timedelta(days=7)
month = today - datetime.timedelta(days=30)
year = (today - datetime.timedelta(days=365))

def json_data():

    
    conn =sqlite3.connect('data/crime_data')
    c = conn.cursor()

    c.execute(f"select * from crime_data where ararrestdate >= '{year}'")
    rows = c.fetchall()
    data_list = []

    for row in rows:
        d = collections.OrderedDict()
        d['incidentnum'] = row[0]
        d['arrestnumber'] = row[1]
        d['ararrestdate'] = row[2]
        d['ararresttime'] = row[3]
        d['arpremises'] = row[4]
        d['arladdress'] = row[5]
        d['arlzip'] = row[6]
        d['sex'] = row[7]
        d['drugrelated'] = row[8]
        d['drugtype'] = row[9]
        d['age'] = row[-1]
        data_list.append(d)

    j = json.dumps(data_list)
    with open('js\year_data.js', 'w') as f:
        f.write(j)
    
    c.execute(f'''select * from crime_data''')

    c.execute(f"select * from crime_data where ararrestdate >= '{month}'")

    rows = c.fetchall()
    month_list = []

    for row in rows:
        a = collections.OrderedDict()
        a['incidentnum'] = row[0]
        a['arrestnumber'] = row[1]
        a['ararrestdate'] = row[2]
        a['ararresttime'] = row[3]
        a['arpremises'] = row[4]
        a['arladdress'] = row[5]
        a['arlzip'] = row[6]
        a['sex'] = row[7]
        a['drugrelated'] = row[8]
        a['drugtype'] = row[9]
        a['age'] = row[-1]
        month_list.append(a)

    x = json.dumps(month_list)
    with open('js\month_data.js', 'w') as f:
        f.write(x)

   

    c.execute(f"select * from crime_data where ararrestdate >= '{week}'")

    rows = c.fetchall()
    data_list = []

    for row in rows:
        d = collections.OrderedDict()
        d['incidentnum'] = row[0]
        d['arrestnumber'] = row[1]
        d['ararrestdate'] = row[2]
        d['ararresttime'] = row[3]
        d['arpremises'] = row[4]
        d['arladdress'] = row[5]
        d['arlzip'] = row[6]
        d['sex'] = row[7]
        d['drugrelated'] = row[8]
        d['drugtype'] = row[9]
        d['age'] = row[-1]
        data_list.append(d)

    j = json.dumps(data_list)
    with open('js\week_data.js', 'w') as f:
        f.write(j)

   

    c.execute(f"select * from crime_data where ararrestdate >= '{today}'")

    rows = c.fetchall()
    data_list = []

    for row in rows:
        d = collections.OrderedDict()
        d['incidentnum'] = row[0]
        d['arrestnumber'] = row[1]
        d['ararrestdate'] = row[2]
        d['ararresttime'] = row[3]
        d['arpremises'] = row[4]
        d['arladdress'] = row[5]
        d['arlzip'] = row[6]
        d['sex'] = row[7]
        d['drugrelated'] = row[8]
        d['drugtype'] = row[9]
        d['age'] = row[-1]
        data_list.append(d)

    j = json.dumps(data_list)
    with open('js/today_data.js', 'w') as f:
        f.write(j)
