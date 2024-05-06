from flask import Flask, request, jsonify
import unicodedata
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='*')

@app.route('/normalize', methods=['POST'])
def normalize():
    texts = request.get_json().get('texts', [])
    normalized_texts = [unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8').lower() for text in texts]
    return jsonify(normalized_texts)

if __name__ == '__main__':
    app.run(port=5005)
