
from flask import Flask, request, jsonify

app= Flask(__name__)


@app.route('/', methods=['GET'])
def index():

	response = jsonify({'response_text': 'Hola'})

	response.headers.add("Access-Control-Allow-Origin", "*")
	return response 

