import datetime
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

events = [
    {"title": "event1", "date": "2025-9-15"},
    {"title": "event2", "date": "2025-9-20"},
    # {"title": "t", "date": "d"}
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calendar", methods=["GET", "POST"])
def calendar():

    # for t, d in zip(text, datetime):
    #     events.append({"text : t," "datetime : d"})

    # return render_template("calendar.html", events=events)
    if request.method == "GET":
        print( events)
        return render_template("calendar.html", events=events)
    elif request.method == "POST":

        datetime = request.form["datetime"]
        title = request.form["text"]
        # return render_template("show.html", date=date, text=text)

        new_event = {"title": title, "date": datetime}
        text = request.form["text"]
    
    events.append(new_event)

    # @app.route("/caleder/vi", methods=["GET","POST"])
    return redirect(url_for("calendar"))


# def input_view():
#     value = request.form"text"

#     return render_template("show.html", value=value)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
