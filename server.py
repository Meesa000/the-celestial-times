from flask import Flask, render_template
from get_data import get_latest_articles


app = Flask(__name__)

@app.route("/")
def display_homepage():
    
    articles_list = get_latest_articles()
    
    return render_template('index.html', articles_list=articles_list)