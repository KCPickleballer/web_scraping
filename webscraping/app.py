# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

mongo.db.collection.drop()




# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")


# create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():

    # Find data
    forecasts = mongo.db.collection.find() 

    # return template and data
    return render_template("index.html", forecasts=forecasts)



# Route that will trigger scrape functions
@app.route("/scrape")
def scrape():

    # Run scraped functions
    weather = scrape_mars.scrape()
    
    # Store results into a dictionary
    # forecast = {
    #     "time": weather["time"],
    #     "location": weather["name"],
    #     "min_temp": weather["min_temp"],
    #     "max_temp": weather["max_temp"],
    #     "surf_location": surf["location"],
    #     "height": surf["height"],
    # }
    forecasts = {
        "weather": weather["mars_weather"],
        "mars_news_title": weather["mars_news_title"],
        "mars_news_para": weather["mars_news_para"],
        "featured_img": weather['featured_img'],
        "featured_img_title": weather['featured_img_title'],
        "fact_tbl":  weather["marsFacts_table"],

         "hem1_img": weather['hem1_img'],
         "hem2_img": weather['hem2_img'],
         "hem3_img": weather['hem3_img'],
         "hem4_img": weather['hem4_img'],
         "hem1_title": weather['hem1_title'],
         "hem2_title": weather['hem2_title'],
         "hem3_title": weather['hem3_title'],
         "hem4_title": weather['hem4_title']
    }
    print(f'forecast is: {forecasts}')

    


    # Insert forecast into database
    mongo.db.collection.insert_one(forecasts)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
