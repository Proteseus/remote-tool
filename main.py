from flask import Flask, render_template, Response, request, redirect, url_for
import BookResp as bk

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def search():
    FormData = request.form
    bk.get_book_opt(FormData['book_name'])
    result = bk.data
    length = len(result['files_found'])
    print(length)
    print(FormData['book_name'])
    return render_template('results.html', form_data=FormData, books = result, length = length)

@app.route('/api/data/')
def get_data():
    return app.send_static_file("data.json")