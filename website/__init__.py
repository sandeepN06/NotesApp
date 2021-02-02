from flask import Flask 

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Ssshh This is secret' #Import like for encryption and cookies thing

    from .views import views
                              #Importing the BluePrints for regestering them
    from .auth import auth

    app.register_blueprint(views , url_prefix='/')
    app.register_blueprint(auth , url_prefix='/') #No prefix as now (19.20)



    return app
