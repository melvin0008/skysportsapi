#!venv/bin/python
import requests
import json
import bs4
import re
from flask import Flask, jsonify
from flask import abort
from flask import make_response

from flask import request
from flask import url_for


app = Flask(__name__)

root_url = 'http://www1.skysports.com/'

sports=["football","cricket","golf","rugbyleague","boxing","tennis","f1","darts","snooker","cycling","american-football","motor-racing","ice-hockey","baseball"]

@app.route('/sky/getlatest/v1.0/', methods=['GET'])
def get_latest():
    index_url = root_url + "latest-news"+"/"	
    response = requests.get(index_url)
    latest={}

    soup = bs4.BeautifulSoup(response.text)
    for sport in sports:
    	for a in soup.select('div.site-wrapper a[href^=http://www1.skysports.com/'+sport+'/]'):
    		latest[sport]= {"link":a.attrs.get('href'),"text":a.get_text()} 
    return json.dumps(latest)

@app.route('/')
    return 

@app.route('/sky/getnews/<string:category>/v1.0/', methods=['GET'])
def get_news(category):
    index_url=root_url+ category +"/news/"
    response = requests.get(index_url)
    latest=[]
    item={}
    soup = bs4.BeautifulSoup(response.text)
    allnews=soup.findAll("div" ,{"class":"news-list__item news-list__item--show-thumb-bp30"})
    #soup.select(
    for news in allnews:
        #latest.append(news.noscript.img.attrs.get('src'))
        #latest.append(news.find("div",{"class":"news-list__body"}).p.get_text())
        itemdetail=news.find("div",{"class":"news-list__body"})
        #latest.append(itemdetail.p.get_text())
        #latest.append(re.sub('\s+',' ',itemdetail.h4.get_text()))
        #latest.append(itemdetail.h4.a.attrs.get('href'))
        item={"imgsrc":news.noscript.img.attrs.get('src'),"title":re.sub('\s+',' ',itemdetail.h4.get_text()),"shortdesc":itemdetail.p.get_text(),"link":itemdetail.h4.a.attrs.get('href')}
        latest.append(item)
    return json.dumps(latest)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


#print(get_latest())
#print(get_news('golf'))


if __name__ == '__main__':
    app.run(debug=True)