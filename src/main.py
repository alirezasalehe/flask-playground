from flask import Flask, request, redirect
from environs import Env

from db_service import db_service, UrlNotFoundException
from utils import random_string_generator

app = Flask("Url Shortener")


@app.route('/<path:path>', methods=['GET'])
def redirect_short_url(path):
    print(request.args, path)
    try:
        return redirect(db_service.get_url(path), code=302)
    except UrlNotFoundException:
        return "Not Found"


@app.route('/shorten', methods=['POST'])
def short_url():
    print(request.headers, request.get_json())
    url = request.get_json().get("url", None)
    if not url:
        return "No URL"
    shorten = random_string_generator(4)
    db_service.set_url(url, shorten, expire_time=120)
    return shorten


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=Env().str('FLASK_PORT'))
