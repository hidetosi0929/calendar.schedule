from flask import Flask, render_template, request

app = Flask(__name__)

events = [{"title": "event1", "date": "2025-9-15"}, {"title": "event2", "date": "2025-9-20"}]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calendar", methods=["GET", "POST"])
def calendar():
    if request.method == "GET":

        return render_template("calendar.html", events=events)
    elif request.method == "POST":
        date = request.form['datetime']
        text = request.form['text']
        return render_template("show.html", date=date, text=text)

# @app.route("/caleder/vi", methods=["GET","POST"])
# def input_view():
#     value = request.form"text"

#     return render_template("show.html", value=value)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
