from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)


@app.route("/", methods = ['GET','POST'])
def index():
    try:
        return render_template("index.html")
    except Exception as e:
        return render_template("index.html")


if __name__=="__main__":
    app.run(debug = True)