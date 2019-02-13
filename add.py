from flask import Flask
app = Flask(__name__)

# declare a global variable that we can use to store
# the current value of our counter
counter = 0

@app.route("/")
def hello():
    return "Hello World!"

# when the route matches the /add route
# run the below function
@app.route("/add")
def add():
    # let the function know that counter is declared globally
    # try removing this line and see what happends when you visit
    # the /add route
    global counter
    # increment the counter by 1
    counter = counter + 1
    # convert the counter value to a string so it is the correct
    # type for our function. Try just returning the raw counter
    # variable and see what happens when you visit this route
    return str(counter)

if __name__ == "__main__":
    app.run()
