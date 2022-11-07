from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import api_data
import data_json
import os

app = Flask(__name__)

#remove files if already exists to upload new data
try:
    os.remove('js\month_data.js')
    os.remove('js/today_data.js')
    os.remove('js\week_data.js')
    os.remove('js\year_data.js')
except:
    print('no files to be removed')
#call function to get all the necessary data
data_json.json_data()

@app.route('/')
def echo():
    return render_template('index.html')


#debugger to edit while running
if __name__ == "__main__":
    app.run(debug=True)