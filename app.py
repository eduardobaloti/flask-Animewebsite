from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/list', methods=['POST'])
def anime():
    headers = {
    'x-rapidapi-key': "3d90e7b795mshdcbf95b0e658220p15126fjsn6bec6924f199",
    'x-rapidapi-host': "jikan1.p.rapidapi.com"
    }
    url = "https://jikan1.p.rapidapi.com/search/anime"
    anime = request.form['animename']
    querystring = {"q":{anime}}
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    return render_template("list.html", data=data)


if __name__ == '__main__':
    app.run(debug=True)
