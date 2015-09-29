import logging
import logging.handlers
from flask import Flask, render_template
from pymongo import MongoClient


app = Flask(__name__)
app.secret_key = 'something-secure'

# Logging
file_handler = logging.handlers.RotatingFileHandler(
    '/var/log/app/app.log', mode='a+',
    maxBytes=20480,
    backupCount=5)

formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s",
                              "%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)

app.logger.addHandler(file_handler)

@app.route('/')
def hello_world():
    return 'Hello World!'

# When linking between containers is setup
# comment previous route and uncomment the one below.
# @app.route('/')
# def index():
#     client = MongoClient('database_instance', 27017)
#     db = client.test_database
#     app_data = db.test_data.find()
#
#     return render_template('index.html', app_data=app_data)

if __name__ == '__main__':
    logging.getLogger().addHandler(logging.StreamHandler())
    app.run(host='0.0.0.0')
