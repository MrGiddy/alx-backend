#!/usr/bin/env python3
"""A Basic Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel
from typing import Union


class Config:
    """Configuration class for the app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


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


@app.route('/')
def get_index() -> str:
    """The home or index page"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
