from flask import Blueprint

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return "Login successful"

@auth.route('/logout')
def logout():
    return "Logout successful"

@auth.route('/sign-up')
def sign_up():
    return "Sign up successful"