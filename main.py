#main.py
import re
from flask import Flask, render_template, Response, request, redirect, url_for
import json
import BookResp as bk
import current_weather as wr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def search():
    FormData = request.form
    bk.get_book_opt(FormData['book_name'])
    result = bk.data
    
    if result == -1:
        return redirect('index.html', data='Book not found')
    else:
        length = len(result['files_found'])
        print(length)
        print(FormData['book_name'])
        return render_template('results.html', form_data=FormData, books = result, length = length)

@app.route('/weather')
def get_weather_data():
    return render_template('weather_main.html')

@app.route('/weather/results', methods=['POST'])
def get_weather_results():
    FormData = request.form
    wr.Weather.fetch_weather(wr.Weather)#, FormData['city_name'])
    result = wr.Weather().fetch_status()
    if result == -1:
        return redirect('weather_main.html', data='Weather data not found')
    else:
        wrs = wr.Weather.get_weather(wr.Weather)
        tmp = wr.Weather.get_temp(wr.Weather)
        inf = wr.Weather.get_info(wr.Weather)

        col = {'weather': wrs, 'temperature': tmp, 'information': inf}
        return render_template('weather_child.html', col=col)
    
@app.route('/news')
def get_news():
    return render_template('news.html')
    
@app.route('/data/books', methods=['GET'])
def get_data_books():
    with open("./static/results.json", "r") as js:
        jData = json.load(js)
    print (jData)
    return jData

@app.route('/data/weather', methods=['GET'])
def get_data_weather():
    with open("./static/weather_results.json", "r") as js:
        jData = json.load(js)
    print (jData)
    return jData