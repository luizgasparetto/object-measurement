from flask import Flask, request, jsonify, Response
from scripts.measure_object_size import *
from flask_cors import CORS, cross_origin

# CORS
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return Response('Welcome to Object Measurement API!')

@app.route("/measurement", methods=["POST"])
@cross_origin()
def get_metrics():
    body = request.get_json()

    try:
        result = measure_object(body["image_url"]) 

        data = {
            "width": result.width,
            "height": result.height
        }

        return jsonify(data)
    except Exception as e:
        return Response(str(e))

if __name__ == '__main__':
    app.run()
