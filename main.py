from flask import Blueprint, render_template


main = Blueprint('main',__name__)

@main.route('/')
def index():
    return"hello,world"

@main.route('/profile')
def profile():
    return "profile Here"