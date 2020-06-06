import requests
from bs4 import BeautifulSoup
import urllib.request
import itertools
from flask import Flask, request, Response, render_template, redirect
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import Regexp
import re
import zipfile
import glob
import os
import RecoverPlaysTVClips

csrf = CSRFProtect()
app = Flask(__name__)
app.config["SECRET_KEY"] = "row the boat"
csrf.init_app(app)

@app.route('/')
def main():
    return redirect("/index")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/proxy/download')
def proxydownload():
    RecoverPlaysTVClips.create_zip()
    d = {}
    d[0] =  ["Hello lol"]
    return d




