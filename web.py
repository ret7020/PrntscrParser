from flask import Flask, render_template
import random
import os
from config import *

def get_random_images(path=IMAGES_PATH):
    images = [f for f in os.listdir(path) if not f.startswith('.')]
    return random.choices(images, k=3)


app = Flask(__name__, static_url_path="/static", static_folder=IMAGES_PATH)

@app.route("/")
def index():
    return render_template("index.html", images=get_random_images())

if __name__ == "__main__":
    app.run(host=FLASK_HOST, port=FLASK_PORT)
