from flask import Flask,jsonify,request
from flask_cors import CORS
import util1
import sys
app=Flask(__name__)
CORS(app)
@app.route("/get_symptoms_names")
def get_symptoms_names():
    response = jsonify({
        "symptoms": util1.get_symptoms_names()
    })
    print(response)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
@app.route("/predict", methods=['POST', 'GET'])
def predict():
    age=request.form['age']
    gender = request.form['gender']
    symptoms = request.form.getlist('symptoms[]')

    response = jsonify({
        "disease": util1.predict(symptoms)
    })
    print(response)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
@app.route("/predict_drug", methods=['POST', 'GET'])
def predict_drug():
    age=request.form['age']
    gender = request.form['gender']


    response = jsonify({
        "drug": util1.predict_drug(gender, age).to_dict()
    })

    print(response)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if (__name__ == "__main__"):
    print("starting flask server")
    app.run()