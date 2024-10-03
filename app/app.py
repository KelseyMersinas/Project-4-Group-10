from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import pickle
from helper import convert_to_index

app = Flask(__name__)


# enter in the valid features for the search form
valid_features = {
    'cap_shape': ['Bell', 'Conical', 'Convex', 'Flat', 'Sunken', 'Spherical'],
    'gill_attachment': ['Adnate', 'Adnexed', 'Decurrent', 'Free', 'Sinuate', 'Pores'],
    'gill_color': ['Brown', 'Buff', 'Gray', 'Green', 'Pink', 'Purple', 'Red', 'White', 'Yellow', 'Blue', 'Orange', 'Black'],
    'stem_color': ['Brown', 'Buff', 'Gray', 'Green', 'Pink', 'Purple', 'Red', 'White', 'Yellow', 'Blue', 'Orange', 'Black'],
    'season': ['Spring', 'Summer', 'Fall', 'Winter'],
    'cap_diameter': {'min': 0, 'max': 1891}, 
    'stem_height': {'min': 0.04, 'max': 383.54},
    'stem_width': {'min': 0, 'max': 356}
}

#########################################################

# Load the model
with open('mushroom_model.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/makePredictions', methods=['POST'])
def make_predictions():
    try:
        content = request.json["data"]
        print('content', content)
        
        # Create DataFrame from form values for model to use
        df = pd.DataFrame({
            'cap-diameter': [float(content['cap_diameter'])],
            'cap-shape': [convert_to_index('cap_shape', content['cap_shape'])],
            'gill-attachment': [convert_to_index('gill_attachment', content['gill_attachment'])],
            'gill-color': [convert_to_index('gill_color', content['gill_color'])],
            'stem-height': [float(content['stem_height'])],
            'stem-width': [float(content['stem_width'])],
            'stem-color': [convert_to_index('stem_color', content['stem_color'])],
            'season': [convert_to_index('season', content['season'])],
        }, columns=['cap-diameter', 'cap-shape', 'gill-attachment', 'gill-color', 'stem-height', 'stem-width', 'stem-color', 'season'])

        # print the data to the console for debugging 
        print("DataFrame for prediction:", df)  

        # get predicitons from the model
        predictions = model.predict(df)
        print('predictions', predictions)

        # change results to be user friendly 
        prediction_labels = ['Edible', 'Not Edible']
        predicted_labels = [prediction_labels[int(pred)] for pred in predictions]

        return jsonify({"ok": True, "predictions": predicted_labels})

        
        # return jsonify({"ok": True, "predictions": predictions.tolist()})
    
    except Exception as e:
        print(f"Error: {e}")  # Log the error to console
        return jsonify({"ok": False, "error": str(e)})

# set up the page for the predictions
@app.route('/predict')
def predict():
    return render_template('predict.html', valid_features=valid_features)

for rule in app.url_map.iter_rules():
    print(rule)

##########################################################

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