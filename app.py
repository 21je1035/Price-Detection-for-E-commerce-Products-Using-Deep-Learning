from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# Load the NLP model from the pickle file
model = pickle.load(open('model_deploy.pkl', 'rb'))

# Load the tokenizer
tokenizer = pickle.load(open('tokenizer.pkl', 'rb'))

# Define the maximum sequence lengths
MAX_NAME_SEQ = 100
MAX_ITEM_DESC_SEQ = 200

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    name = data['name']
    item_description = data['item_description']
    brand_name = data['brand_name']
    category_name = data['category_name']
    item_condition = data['item_condition']
    num_vars = int(data['num_vars'])

    # Create a Pandas dataframe with one row and 6 columns
    input_data = pd.DataFrame({'name': [name], 'item_description': [item_description], 'brand_name': [brand_name], 'category_name': [category_name], 'item_condition_id': [item_condition], 'shipping': [num_vars]})

    # Handle missing values
    input_data = handle_missing(input_data)

    # Handle categorical variables
    le = LabelEncoder()
    input_data['category_name'] = le.transform(input_data['category_name'])
    input_data['brand_name'] = le.transform(input_data['brand_name'])

    # Text to seq process
    input_data["seq_item_description"] = tokenizer.texts_to_sequences(input_data.item_description.str.lower())
    input_data["seq_name"] = tokenizer.texts_to_sequences(input_data.name.str.lower())

    # Pad sequences
    input_data["seq_item_description"] = pad_sequences(input_data.seq_item_description, maxlen=MAX_ITEM_DESC_SEQ)
    input_data["seq_name"] = pad_sequences(input_data.seq_name, maxlen=MAX_NAME_SEQ)

    # Create the input data for the model
    X_input = {
        'name': input_data.seq_name.values,
        'item_desc': input_data.seq_item_description.values,
        'brand_name': input_data.brand_name.values,
        'category_name': input_data.category_name.values,
        'item_condition': input_data.item_condition_id.values,
        'num_vars': input_data.shipping.values
    }

    # Make predictions using the NLP model
    prediction = model.predict(X_input)
    price = prediction[0]

    return jsonify({'price': price})

def handle_missing(dataset):
    dataset.category_name.fillna(value="missing", inplace=True)
    dataset.brand_name.fillna(value="missing", inplace=True)
    dataset.item_description.fillna(value="missing", inplace=True)
    return dataset

if __name__ == '__main__':
    app.run(debug=True)