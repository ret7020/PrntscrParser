from flask import Flask, render_template
import random
import os

def get_random_images(path="./images_png"):
    images = [f for f in os.listdir(path) if not f.startswith('.')]
    return random.choices(images, k=3)


app = Flask(__name__, static_url_path="/static", static_folder="./images_png")

@app.route("/")
def index():
    return render_template("index.html", images=get_random_images())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
