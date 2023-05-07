from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'

@app.route("/<int:number_1>/<int:number_2>", methods=['POST', 'GET'])
def subtract(number_1,number_2):
    return str(float(number_1)-float(number_2))
if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )