from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_boxoffice

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/craigslist_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    movie_data = mongo.db.movie_data.find_one()
    return render_template("index.html", movie_data=movie_data)


@app.route("/scrape")
def scraper():
    movie_data = mongo.db.movie_data
    listings_data = scrape_boxoffice.scrape()
    movie_data.update({}, listings_data, upsert=True)
    return redirect("/", code=302)



if __name__ == "__main__":
    app.run(debug=True)
