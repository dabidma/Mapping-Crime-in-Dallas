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
        d['age'] = row[10]
        d['lat'] = row[11]
        d['lon'] = row[12]
        data_list.append(d)
        j = json.dumps(data_list)

    with open('static\js\year_data.js', 'w') as f:
        f.write('let year_data=' +j) #tweaked the this so it starts off in a variable in the js file
    
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
        a['age'] = row[10]
        a['lat'] = row[11]
        a['lon'] = row[12]
        month_list.append(a)
        x = json.dumps(month_list)

    with open('static\js\month_data.js', 'w') as f:
        f.write('let month_data='+x) #tweaked the this so it starts off in a variable in the js file

    c.execute(f'''select * from crime_data''')

    c.execute(f"select * from crime_data where ararrestdate >= '{week}'")

    rows = c.fetchall()
    data_list = []

    for row in rows:
        b = collections.OrderedDict()
        b['incidentnum'] = row[0]
        b['arrestnumber'] = row[1]
        b['ararrestdate'] = row[2]
        b['ararresttime'] = row[3]
        b['arpremises'] = row[4]
        b['arladdress'] = row[5]
        b['arlzip'] = row[6]
        b['sex'] = row[7]
        b['drugrelated'] = row[8]
        b['drugtype'] = row[9]
        b['age'] = row[10]
        b['lat'] = row[11]
        b['lon'] = row[12]
        data_list.append(b)
        week_dump = json.dumps(data_list)

    with open('static\js\week_data.js', 'w') as f:
        f.write('let week_data='+week_dump) #tweaked the this so it starts off in a variable in the js file

    c.execute(f'''select * from crime_data''')

    c.execute(f"select * from crime_data where ararrestdate >= '{today}'")

    rows = c.fetchall()
    data_list = []

    for row in rows:
        c = collections.OrderedDict()
        c['incidentnum'] = row[0]
        c['arrestnumber'] = row[1]
        c['ararrestdate'] = row[2]
        c['ararresttime'] = row[3]
        c['arpremises'] = row[4]
        c['arladdress'] = row[5]
        c['arlzip'] = row[6]
        c['sex'] = row[7]
        c['drugrelated'] = row[8]
        c['drugtype'] = row[9]
        c['age'] = row[10]
        c['lat'] = row[11]
        c['lon'] = row[12]
        data_list.append(c)
        today_json = json.dumps(data_list)
    
    with open('static/js/today_data.js', 'w') as f:
        try:
            f.write('let today_data='+today_json)  #tweaked the this so it starts off in a variable in the js file
        except:
            f.write('let today_data=[]')