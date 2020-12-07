import flask
from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
import pandas as pd
from keras.models import load_model

#Load in the pre-trained model--------------
def getModel():
    global model 
    model = load_model('my_model.h5')
    print("Model loaded")

application = app= flask.Flask(__name__, template_folder='templates')
#Main function---------------------------------------
@app.route('/', methods=['GET', 'POST'])
def main():
    getModel()
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    
    if flask.request.method == 'POST':
        nationality = flask.request.form['nationality']
        sex = flask.request.form['sex']
        age = flask.request.form['age']
        height = flask.request.form['height']
        weight = flask.request.form['weight']
        sport = flask.request.form['sport']

        from sklearn.preprocessing import LabelEncoder
        import numpy as np
        lb_make = LabelEncoder()
        #new_sex = lb_make.fit_transform(np.array([sex]))
        #new_sport = lb_make.fit_transform(np.array([sport]))
        #new_nationality = lb_make.fit_transform(np.array([nationality]))
        
        input_variables = np.array([[int(nationality), int(sex), int(age), float(height), int(weight), int(sport)]])
        
        #input_variables = np.array([[new_nationality[0], new_sex[0], int(age), float(height), int(weight), new_sport[0]]])
                                       #columns=['nationality', 'sex', 'dob', 'height', 'weight', 'sport'],
                                       #dtype=float)
        #prediction = model.predict_classes(input_variables)[0]
        
        prediction = np.argmax(model.predict(input_variables), axis=-1)[0]
        print(prediction)
        st = ''
        if prediction == 0:
            st = 'no medal'
        elif prediction == 1:
            st = 'gold medal'
        elif prediction == 2:
            st = 'silver medal'
        else:
            st = 'bronze medal'
        return (flask.render_template('main.html',
                                     original_input={'nationality':nationality,
                                                     'sex':sex,
                                                     'age':age,
                                                     'height':height,
                                                     'weight':weight,
                                                     'sport':sport,
                                                     },
                                     result=st
                                     ))
if __name__ == '__main__':
    app.run()
