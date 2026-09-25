from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/market")
def market():
    return render_template("market.html")

@app.route("/events")
def events():
    return render_template("events.html")

@app.route("/jobs")
def jobs():
    return render_template("jobs.html")

@app.route("/weather")
def weather():
    return render_template("weather.html")

@app.route("/health")
def health():
    return render_template("health.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html")


if __name__ == "__main__":
    app.run(debug=True)
