from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
results = pickle.load(open('results.pkl', 'rb'))
class_names = ['Setosa', 'Versicolor', 'Virginica']
emojis = {
    'Setosa': '🌸',
    'Versicolor': '🌺',
    'Virginica': '🌼'
}


@app.route('/')
def index():
    return render_template('index.html', results=results)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Missing JSON body'}), 400

    required = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    for field in required:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400

    sepal_length = float(data['sepal_length'])
    sepal_width = float(data['sepal_width'])
    petal_length = float(data['petal_length'])
    petal_width = float(data['petal_width'])

    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    scaled = scaler.transform(features)
    prediction = model.predict(scaled)[0]
    species = class_names[prediction]

    return jsonify({
        'species': species,
        'emoji': emojis[species],
        'confidence': 'KNN K=5 Majority Vote',
        'input': {
            'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width
        }
    })


@app.route('/results')
def get_results():
    return jsonify(results)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
