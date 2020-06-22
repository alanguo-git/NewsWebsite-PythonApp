# NewsWebsite-PythonApp
This is a news website
Frontend is written with HTML CSS and JavaScript, no framework is used.
Backend is build in Python using Flask framework 

## Table of Contents
- [Prerequisites](#Prerequisites)
- [Installation](#Installation)
- [Features](#Features)
- [Reference](#Reference)

## Prerequisites
Python (2.7 or 3.5+) and Flask 

## Installation
1. Download and install Python at <a href="https://www.python.org/downloads/">`https://www.python.org/downloads/`</a>.
2. Create environment and Install Flask by following the instructions at <a href="https://flask.palletsprojects.com/en/1.1.x/installation/#installation">`https://flask.palletsprojects.com/en/1.1.x/installation/#installation`</a>.
Alternative way: do not need to install FLask, install Pycharm instead. Pycharm can build Flask project more easily.
Make sure to activate the environment before doing following steps.
3. Install Python NewsApi
>input this code into your terminal
```shell
pip install newsapi-python
```
4. Clone the project or copy all the files into this directory.
5. Get your API key for NewsAPI at <a href="https://newsapi.org/register">`https://newsapi.org/register`</a>. Then, copy and past your API key into application.py line 8.
6. Run application.py locally with Python on port 5000
>input this code into your terminal
```shell
python application.py
```
7. Open your broswer and input url "http://127.0.0.1:5000/index.html" and you will be able to see the website.

If using Pycharm, just follow the instructions at <a href="https://www.jetbrains.com/help/pycharm/creating-flask-project.html">`https://www.jetbrains.com/help/pycharm/creating-flask-project.html`</a>. It is really easy to build the environment and run the app.

## Features
1. Home Page
- Top headlines are provided by the Google News API in sliding format (change every few seconds).
- Words are sorted by frequency and then generate a Word cloud which is displayed next to the slide.
- Specific headlines from CNN and Fox News are provided below the slides.
2. Search Page
- Can set restrictions for the searching (including keyword, from, to, category, source).
- The dropdown menu for source is updated dynamically when category changes.
- Form validation is performed before submitting.
- Click show more button can show 15 news at most, click show less button display the first 5 articles.
- Every news card have hover effect and is clickable, additional information will be desplayed after clicking.

## Reference
- word cloud is implemented using D3.js <a href="https://www.d3-graph-gallery.com/graph/wordcloud_size.html">`https://www.d3-graph-gallery.com/graph/wordcloud_size.html`</a>
- stop words <a href="https://sites.google.com/site/kevinbouge/stopwords-lists">`https://sites.google.com/site/kevinbouge/stopwords-lists`</a>