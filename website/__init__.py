from flask import Flask
#Setting up the flask application

#create a app function
def create_app():
    app = Flask(__name__) #represents name for file. Initilizes the app
    app.config['SECRET_KEY'] = 'ChaChaDu' #initializes secret key / config variable to secure cookies data
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app # returns the created app function 