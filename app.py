from flask import Flask, render_template, send_from_directory, request
import os   
import pandas as pd
import pickle
import sys
import numpy as np
from werkzeug.utils import secure_filename, send_file

app = Flask(__name__)

@app.route("/assets/<path:path>")
def static_dir(path):
    return send_from_directory("static/assets", path)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")

@app.route("/about")
def about():
    return "<h1>About</h1>"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 33507))
    app.run(host="0.0.0", debug=True,port=port)