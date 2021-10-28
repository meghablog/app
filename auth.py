from flask import Blueprint, render_template

auth = Blueprint('auth',__name__)

@auth.route('/signup')
def signup():
    return "this page will sign up users"

@auth.route('/login')
def login():
    return "this page will login user"