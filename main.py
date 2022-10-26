from flask import Flask, request
import json
from trata_dados import trata_dados

app = Flask(__name__)

@app.route('/', methods=['POST'])
def recebe_dados():
    data_json = request.json
    trata_dados(data_json)

app.run(host='127.0.0.1', port=130, debug=True)