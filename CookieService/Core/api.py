import json
from config import *
from CookiePool import RedisDB
from flask import Flask,g
app = Flask(__name__)
app.debug = True
@app.route("/")
def index():
    return "<h2>Welcome to cookie system</h2>"

def get_conn():
    for website in GENERATOR_MAP:
        if not hasattr(g,website):
            setattr(g,website+"_cookies",eval("RedisDB"+"('cookies','"+website+"')"))
    return g
@app.route('/<website>/random')
def random(website):
    g = get_conn()
    cookies = getattr(g,website+"_cookies").random()
    cookies = json.loads(cookies)
    com_cookie = {}
    for cookie in cookies:
        print(cookie)
        com_cookie.update(cookie)

    return com_cookie


if __name__ == "__main__":
    app.run()