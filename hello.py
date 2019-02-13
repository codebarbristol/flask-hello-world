# bring flask into our application so that we can use it
from flask import Flask

# create a flask app so that we can
# use to run the application
app = Flask(__name__)

# when the route matches the / route
# run the below function
@app.route("/")
def hello():
    return "Hello World!"

# if this file is executed with `python hello.py`
# run app.run()
if __name__ == "__main__":
    app.run()
