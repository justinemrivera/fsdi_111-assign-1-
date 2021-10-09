from flask import Flask  # From the flask package import the Flask class

# instaniate the Flask class into app(which is now an obj)
app = Flask(__name__)


@app.route("/")  # decorater that maps the path to a view function
def index():               # a view function called index
    return "<h1> Hello, world!</h1>"  # return statement for index

# comment


@app.route("/about")
def about_me():
    me = {
        "first_name": "Justine",
        "last_name": "Rivera",
        "hobbies": "DIY STUFF",
        "active": True,
    }
    return me
# testing
