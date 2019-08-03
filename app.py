from flask import Flask, render_template, request, jsonify
from utils import minimax
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/play', methods=['POST'])
def play():
    try:
        coluna, score = minimax.get_best_move(request.json['board'])
    except:
        coluna = None
    return jsonify({'coluna': coluna})

if __name__ == '__main__':
  app.run(debug=True)
