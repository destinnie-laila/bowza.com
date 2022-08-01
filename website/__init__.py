from flask import Flask
#Setting up the flask application

#create a app function
def create_app():
    app = Flask(__name__) #represents name for file. Initilizes the app
    app.config['SECRET_KEY'] = 'Nicholas21' #initializes secret key / config variable to secure cookies data
    
    return app # returns the created app function 