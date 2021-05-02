import numpy as np
from flask import Flask, render_template, jsonify, request
import pickle
#from xgboost import XGBRegressor
from sklearn.preprocessing import StandardScaler

app=Flask(__name__)
model=pickle.load(open("NBClassifier.pkl","rb"))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
standatd_to= StandardScaler()

@app.route("/predict", methods=['POST'])
def predict():
    if  request.method=="POST":
        Nitrogen = int(request.form['Nitrogen'])
        Phosphorous=int(request.form['Phosphorous'])
        Pottasium=int(request.form['Pottasium'])
        Temperature=float(request.form['Temperature'])
        Humidity=float(request.form['Humidity'])
        ph_level=float(request.form['ph_level'])
        Rainfall=float(request.form['Rainfall'])
    prediction=model.predict([[Nitrogen,Phosphorous,Pottasium,Temperature,Humidity,ph_level,Rainfall]])
    #output=rou
    #return render_template("index.html",prediction_text="You Should grow {}".format(prediction))
    return render_template('crop-result.html', prediction=prediction, title="test")

if __name__=="__main__":
    app.run(debug=True)
