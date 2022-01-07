import base64
from flask import Flask, send_file, jsonify
import os
import random

IMGS_PER_MENU_PAGE = 3

app = Flask(__name__)

def random_image():
    """
    Return a random image from the ones in the media/ directory
    """
    img_dir = "./media"
    img_list = os.listdir(img_dir)
    img_path = os.path.join(img_dir, random.choice(img_list))
    return img_path

def get_n_images(n):
    img_dir = "./media"
    img_list = os.listdir(img_dir)
    if len(img_list) > n:
        return img_list[:n]
    else:
        return img_list

def get_images_of_page(page):

    img_dir = "./media"
    img_list = os.listdir(img_dir)
    print(img_list)
    max_page = len(img_list) / IMGS_PER_MENU_PAGE

    if max_page > page:
        return img_list[page * IMGS_PER_MENU_PAGE : page * IMGS_PER_MENU_PAGE + IMGS_PER_MENU_PAGE]
    else:
        return img_list[page * IMGS_PER_MENU_PAGE:]


@app.route('/')
def myapp():
    """
    Returns a random image directly through send_file
    """
    image = random_image()
    return send_file(image, mimetype='image/gif')

@app.route('/menu/<int:page>')
def send_menu(page):
    """
    This function send the set of files that make the menu
    """
    menu_list = get_images_of_page(page)
    print(menu_list)
    return jsonify(menu_list)

@app.route('/media/<name>')
def send_gif(name):
    """
    Returns the requested image directly through send_file
    """
    return send_file("./media/" + name, mimetype='image/gif')

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response
