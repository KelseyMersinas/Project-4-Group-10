from flask import Flask, request, jsonify, render_template
import sklearn
import numpy as np
import pickle

app = Flask(__name__)

# load the model
with open('mushroom_model.h5', 'rb') as file:
    model = pickle.load(file)

# Attempt to make the prediction page - havn't figured it out yet just slapped this together- will work on over weekend
@app.route('/predict', methods=['POST'])
def predict():
    features_input = request.form['features']  
    features = np.array(features_input.split(',')).reshape(1, -1)  
    prediction = model.predict(features)
    return jsonify({'edible': prediction[0]})

# home page
@app.route('/')
def home():
    return render_template('landing.html')

# write up
@app.route('/writeup')
def writeup():
    return render_template('writeup.html')

# about us 
@app.route('/aboutus', methods=['GET'])
def aboutus():
    return render_template('aboutus.html')

# work cited
@app.route('/workscited', methods=['GET'])
def workscited():
    return render_template('workscited.html')

if __name__ == '__main__':
    app.run(debug=True)