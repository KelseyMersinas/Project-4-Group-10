from flask import Flask, request, jsonify, render_template
import sklearn
import numpy as np
import pickle

app = Flask(__name__)

# Load the model
with open('mushroom_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    content = request.json['data']
    print(content)
    return(jsonify({'ok': True}))

# home page
@app.route('/')
def home():
    return render_template('landing.html')

# dashboard 1
@app.route('/tableauOne')
def tableauOne():
    return render_template('tableauOne.html')

# dashboard 2
@app.route('/tableauTwo')
def tableauTwo():
    return render_template('tableauTwo.html')

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

##################################################

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

if __name__ == '__main__':
    app.run(debug=True)