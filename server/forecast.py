#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask.json import jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route("/forecast/<period>")
def pred(period):

    time = list(range(10))
    total_events = list(range(10))

    y_fun = list(range(int(period)))

    result = jsonify({"x": time, "y": total_events, "y_fun": y_fun, "period": str(period)})

    return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8886')