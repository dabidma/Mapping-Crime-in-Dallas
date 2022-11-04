from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import api_data
import data_json

app = Flask(__name__)

@app.route('/')
def echo():
    pull = data_json.json_data()
    render_template('index.html', test = pull)


#debugger to edit while running
if __name__ == "__main__":
    app.run(debug=True)