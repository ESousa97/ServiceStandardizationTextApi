from flask import Flask, request, jsonify
import unicodedata
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='*')

@app.route('/normalize', methods=['POST'])
def normalize():
    # Obter os textos do corpo da requisição JSON
    texts = request.get_json().get('texts', [])
    
    # Normalizar os textos
    normalized_texts = [
        unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8').lower()
        for text in texts
    ]
    
    # Retornar os textos normalizados
    return jsonify(normalized_texts)

if __name__ == '__main__':
    app.run(debug=True, port=5005)
