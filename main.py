from crypt import methods
from readline import append_history_file
from aiohttp import FormData
from flask import Flask, render_template, Response, request, redirect, url_for
import BookResp as bk

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def search():
    FormData = request.form
    result = bk.get_book_opt(FormData['book_name'])
    print(FormData['book_name'])
    return render_template('results.html', form_data=FormData)

@app.route('/api/data/')
def get_data():
    return app.send_static_file("data.json")