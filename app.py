import flask
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import pandas as pd
import numpy as np
from tkinter import *
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])

def main(): 
    def calculate_bmi(weight, height):
        # Convert height from centimeters to meters
        height_meters = height / 100

        # Calculate BMI
        bmi = weight / (height_meters ** 2)

        return bmi
    def categorize_bmi(bmi):
        if bmi < 18.5:
            return 'Underweight'
        elif 18.5 <= bmi < 24.9:
            return 'Normal'
        elif 25 <= bmi < 29.9:
            return 'Overweight'
        else:
            return 'Obese'
    def categorize_bmi(bmi):
            if bmi < 18.5:
                return 'Underweight'
            elif 18.5 <= bmi < 24.9:
                return 'Normal'
            elif 25 <= bmi < 29.9:
                return 'Overweight'
            else:
                return 'Obese'
    def Exercise_data(age,veg,height,weight):
        v='non_veg'
        if veg=="Vegetarian":
            v='veg'
        data = {'age': [age],
            'veg_non_veg': [v],
            'height': [height],
            'weight':[weight]}

        df = pd.DataFrame(data)

        # Load exercise dataset from CSV
        exercise_df = pd.read_csv('exercise.csv')

        # Calculate BMI
        df['bmi'] = df['weight'] / ((df['height'] / 100) ** 2)

        # Categorize BMI

        df['bmi_category'] = df['bmi'].apply(categorize_bmi)

        # Merge dataframes
        merged_df = pd.merge(df, exercise_df, how='left', left_on='bmi_category', right_on='bmi_range')

        # Display the recommendations
        data=merged_df[['age', 'veg_non_veg', 'height', 'weight', 'bmi', 'exercise_recommendation']]
        ex=np.unique(data['exercise_recommendation'])
        print("Recommended Exercises : ")
        for k in ex:
            print(k)
        return ex
                
    if flask.request.method == 'GET':
        return(flask.render_template('index.html'))
            
    if flask.request.method == 'POST':
        person=flask.request.form["name"]
        age=int(flask.request.form['age'])
        height=int(flask.request.form['height'])
        weight=int(flask.request.form['weight'])
        Dietary=flask.request.form['Dietary']
        bmi=int(calculate_bmi(weight,height))
        level=categorize_bmi(bmi)
        ex=Exercise_data(Dietary,height,weight,bmi)
        return flask.render_template('found.html',movie_names=age,movie_homepage=height,search_name=person, movie_releaseDate=ex)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
    #app.run()