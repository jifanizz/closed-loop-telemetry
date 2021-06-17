from flask import Flask
#from flask_api import FlaskAPI
from flask import request, Flask
app = Flask(__name__)
import json
import subprocess


@app.route('/acl-on')
def acl_on():
    subprocess.call("./acl-on.sh", shell=True)
    return("okay")

@app.route('/acl-off')
def acl_off():
    subprocess.call("./acl-off.sh", shell=True)
    return("okay")

@app.route('/post-acl-on', methods=['POST'])
def post_acl_on():
    subprocess.call("./acl-on.sh", shell=True)
    return("okay")

@app.route('/post-acl-off', methods=['POST'])
def post_acl_off():
    subprocess.call("./acl-off.sh", shell=True)
    return("okay")

@app.route('/')
def jimtestt():
    return "Welcome to the site!!"


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)