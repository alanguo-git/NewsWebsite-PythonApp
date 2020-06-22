from flask import Flask, request
from newsapi import NewsApiClient
from collections import Counter
import re
import json

application = Flask(__name__, static_url_path="")
newsapi = NewsApiClient(api_key='acd3355df047493f9fabfcb0fbaf6ebe')

#the url which shows the web page
@application.route("/index")
def index():
    return application.send_static_file('index.html')

#get top news
@application.route("/top_headlines")
def top_headlines():
    try:
        top_headlines = newsapi.get_top_headlines(language='en', page_size=30)
        return json.dumps(top_headlines)
    except Exception as e:
        s = str(e)
        return s;

#get top cnn news
@application.route("/top_cnn")
def top_cnn():
    try:
        top_headlines = newsapi.get_top_headlines(sources='cnn',
                                              language='en')
        return json.dumps(top_headlines)
    except Exception as e:
        s = str(e)
        return s;

#get top fox news
@application.route("/top_fox")
def top_fox():
    try:
        top_headlines = newsapi.get_top_headlines(sources='fox-news',
                                              language='en')
        return json.dumps(top_headlines)
    except Exception as e:
        s = str(e)
        return s;

#get words frequency
@application.route("/cloud_words")
def cloud_words():
    file = open('stopwords_en.txt', 'r')
    stop_words = set()
    lines = file.readlines()

    #add all stop words to set
    for line in lines:
        stop_words.add(line.strip())

    words = []
    top_head = newsapi.get_top_headlines(language='en', page_size=100)
    articles = top_head["articles"]
    for article in articles:
        spl = article["title"] #get article titles
        spl = re.sub('[,:;!@#\u2019\u2018\'\"\|\-]', '', spl) #remove special characters with regular expression
        spl = spl.split()
        for s in spl:
            if s.lower() not in stop_words:
                words.append(s.lower());
    frequency = Counter(words).most_common(30) #get top 30 frequent words

    #put words into a dictionary
    freq_list = []
    for fre in frequency:
        #add word and its count to freq_list
        freq_list.append({
            "word": fre[0],
            "count": str(fre[1])
        })
    freq = {"frequency": freq_list}
    return json.dumps(freq)

#get search result
@application.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        try:
            result = newsapi.get_everything(q=request.args.get("keyword"),
                                              sources=request.args.get("source"),
                                              from_param=request.args.get("from"),
                                              to=request.args.get("to"),
                                              language='en',
                                              page_size=30,
                                              sort_by="publishedAt"
                                              )
            return json.dumps(result)
        except Exception as e:
            s = str(e)
            return s;

#get available news source for a certain category
@application.route("/source", methods=["GET", "POST"])
def source():
    if request.method == "GET":
        try:
            source = newsapi.get_sources(
                category=request.args.get("category"),
                language='en',
                country='us'
            )
            return json.dumps(source)
        except Exception as e:
            s = str(e)
            return s;

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()