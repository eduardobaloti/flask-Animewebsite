from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/anime', methods=['POST'])
# def anime():
#    zipcode = request.form['zip']
#    r = requests.get("https://jikan1.p.rapidapi.com/search/anime")
#    json_object = r.json()
#    anime = float(json_object['main']['temp'])
#    return render_template('anime.html', temp=temp_k)
def anime():
    headers = {
    'x-rapidapi-key': "3d90e7b795mshdcbf95b0e658220p15126fjsn6bec6924f199",
    'x-rapidapi-host': "jikan1.p.rapidapi.com"
    }
    url = "https://jikan1.p.rapidapi.com/search/anime"
    anime = request.form['animename']
    querystring = {"q":{anime}}
    response = requests.request("GET", url, headers=headers, params=querystring)
    json_object = response.json()
    animereq = str(json_object['title'])
    return render_template('anime.html', animere=animereq)


if __name__ == '__main__':
    app.run(debug=True)
