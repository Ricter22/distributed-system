import base64
from flask import Flask, send_file
import os
import random

app = Flask(__name__)

def random_image():
    """
    Return a random image from the ones in the media/ directory
    """
    img_dir = "./media"
    img_list = os.listdir(img_dir)
    img_path = os.path.join(img_dir, random.choice(img_list))
    return img_path


@app.route('/')
def myapp():
    """
    Returns a random image directly through send_file
    """
    image = random_image()
    return send_file(image, mimetype='image/gif')