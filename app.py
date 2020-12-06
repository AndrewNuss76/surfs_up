##Adding dependencies

from flask import Flask

##Creating a new Flask app instance
app = Flask(__name__)

##Creating a flask routes
@app.route('/')
def hello_world():
    return 'Hello World'