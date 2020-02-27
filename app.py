from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import html5lib
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/", methods=["POST"])
def form():
    if request.method == "POST":
        link = request.form['link']
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html5lib')
        time = soup.find_all('div', attrs={'class': 'timestamp'})

        i = 0
        j = 0

        for t in time:
            n = t.get_text()
            time_list = n.split(':')
            i = i + int(time_list[0])
            j = j + int(time_list[1])

        minutes = i + j//60
        seconds = j % 60
        hours = minutes // 60
        minutes = minutes % 60

    # return("This will take {} Hours {} Min and {} sec to complete".format(
    #     hours, minutes, seconds))
        return render_template("home.html", hours=hours, minutes=minutes, seconds=seconds)

    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
