from flask import Flask, Blueprint, render_template, redirect, url_for, flash
from file_server.file_server import file_server

app = Flask(__name__)
app.register_blueprint(file_server)

@app.route('/')
def hello():
    return render_template("index.html")
@app.route('/file_server')
def serve():
    return redirect(url_for(file_server.index))