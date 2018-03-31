from flask import Flask
import scipy
import numpy
application = Flask(__name__)

@application.route("/")
def hello():
    test = numpy.arange(15).reshape(3, 5)
    return 'hello'

if __name__ == "__main__":
    application.run(host='0.0.0.0')