from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """
    """
    return "Hello, Wlecome to Cloud World!"

@app.route('/api/v1.0/collectFacts', methods=['POST'])
def collectFacts():
    """
    """
    inputDataPayload = request.json
    return jsonify(inputDataPayload)
   
if __name__ == '__main__':
    app.run(debug=True)
