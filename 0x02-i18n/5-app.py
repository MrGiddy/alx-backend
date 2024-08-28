#!/usr/bin/env python3
"""A Basic Flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union


class Config:
    """Configuration class for the app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> Union[str, None]:
    """return a users' locale"""
    # Check if 'locale' is in the request args
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    # Fall back to the best match from Accept-Language header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """helper func. to get a user by their id"""
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id), None)
    return None


@app.before_request
def before_request():
    """set a user in the global `g` object before each request"""
    user = get_user()
    if user:
        g.user = user


@app.route('/')
def get_index() -> str:
    """The home or index page"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
