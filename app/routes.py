from flask import current_app as app, jsonify, request
from app import db
from app.models import Divvy
import csv
import pandas as pd

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    divvy = pd.read_csv('../DivvyChallenge.csv')
    print(divvy.head())
    # if request.method == 'POST':
    #     with open('../DivvyChallenge.csv') as csv_file:
    #         data = csv.reader(csv_file, delimiter=',')
    #         db.session.add(data)
    #         db.session.commit()
        
    return jsonify({"message":"yo"})