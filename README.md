# Flask Hello World

## Download and install Python (3)

[Codebar.io provide a tutorial on getting setup with python](http://tutorials.codebar.io/python/lesson0/tutorial.html), follow this guide to get get ready to build your first web server


## Intro to the package manager

Python provides a package manager calle [pip](https//pypi.org/project/pip/). This will allow you to download other software for use in your application.

The below command will install a logger for use in your

```python
pip install logger
```

## Intro to Flask

[Flask](http://flask.pocoo.org/) is package that will allow you to serve data over a webserver, this can be anything from a webpage to a collection of cat pictures.

### Installing Flask

Before you can serve your webpage you will need to install the dependecy by running the below command in your command prompt / terminal.


```
pip install Flask
```

### Hello World

The [`hello.py`](./hello.py) file contains a simple web app that will print `hello world!` when you visit http://localhost:5000/ in a browser

In order to run tha application you now need to run 

```
python hello.py
```

Now update `hello.py` with a new `/goodbye` route that returns the message `goodbye!` to anybody who visits


### Counter

In the next example we are going to be storing some data between requests so that we can update and present the new value to our users.

The [`add.py`](./add.py) introduces a new variable `counter` that we are able to manipulate in any of our functions that are executed when a user visits one of our pages.

To run the `add.py` example run

```
python add.py
```

When you visit http://localhost:5000/add you will now be given the current value of the counter, hit refresh in your browser multiple times to see what happens

Now that you are up and running can you add a `/subtract` route that will take `1` away from the counter

## Links from discussions

Codebar tutorials - http://tutorials.codebar.io/
Sololearn - https://www.sololearn.com/
