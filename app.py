from flask import Flask
from flask import jsonify
import sqlite3

import logging

app = Flask(__name__)


@app.route('/api/v1/info')
def home_index():
    conn = sqlite3.connect('mydb.db')
    logging.info("Opened database successfully!")
    api_list = []
    cursor = conn.execute("SELECT buildtime, version, methods, links from apirelease")
    for row in cursor:
        api = {}
        api['version'] = row[0]
        api['buildtime'] = row[1]
        api['methods'] = row[2]
        api['links'] = row[3]
        api_list.append(api)
    conn.close()
    return jsonify({'api_version': api_list})


if __name__ == '__main__':
    app.run()
