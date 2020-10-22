import numpy as np
import pandas as pd
import time
import datetime
import os
from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, configure_uploads, DATA, ALL
app = Flask(__name__)
Bootstrap(app)

files = UploadSet('files', ALL)
app.config["UPLOAD_FILES_DESTINATION"] = 'static/uploadstorage'
configure_uploads(app, files)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/datauploads', methods=['GET', 'POST'])
def datauploads():
    if request.method == 'POST' and 'csv_data' in request.files:
        file = request.files['csv_data']
        filename = file.filename

    return render_template('details.html', filename=filename)
