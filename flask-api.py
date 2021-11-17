import flask
import logging
import os, sys
import socket
import time


###### Python Buffering ######
if sys.version_info[0] == 3:
    os.environ["PYTHONUNBUFFERED"] = "1"

###### App Definition ######
app = flask.Flask(__name__)

###### Python Logging ######
logging.basicConfig(level=logging.INFO)

###### Variables ######
host = socket.gethostname()
ip = socket.gethostbyname(host)
secondsSinceEpoch = time.time()
timeObj = time.localtime(secondsSinceEpoch)
timestamp = '%d.%d.%d %d:%d' % (
timeObj.tm_mday, timeObj.tm_mon, timeObj.tm_year, timeObj.tm_hour, timeObj.tm_min)


###### App Routes ######
@app.route('/')
def index():
    return flask.render_template('index.html', hostname=host, ip=ip, timestamp=timestamp)

###### Run App ######
if __name__ == '__main__':
    app.debug=True
    app.run(port=80,host="0.0.0.0")