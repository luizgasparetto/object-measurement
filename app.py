from flask import Flask, request, jsonify, Response
from scripts.measure_object_size import *

app = Flask(__name__)

@app.route("/measurement", methods=["POST"])
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


app.run()
