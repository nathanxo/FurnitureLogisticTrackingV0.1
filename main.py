from flask import Flask, render_template, url_for, jsonify, request

from gen_track_url import genTrackURL

#import getTrackingURL

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv90


def randomString(stringLength=10):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(stringLength))

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
	#print("AHAHHAHA")
	return render_template('index.html')

@app.route('/get_track_url', methods=['POST'])
def get_track_url():
    print("AHAHHAHA")
    print("GOT THINGS: ", request.form['tracking_input'])
    trackurl_dict = genTrackURL(request.form['tracking_input']) #TOBS22272
    print("ReturnStuff: ", trackurl_dict)
    if trackurl_dict['status_code'] != 200:
        print("Internal Error: ", trackurl_dict)
        raise InvalidUsage("Error: Either Not Found or Server Error", status_code=404)
    else:
        return jsonify(tracking_url=trackurl_dict['tracking_url'], tracking_input_recieved=request.form['tracking_input'])

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
# @app.route('/ajax.js')
# def index():
# 	url_for('static', filename='ajax.js')

@app.route('/static/<path:path>')
def send_js(path):
	print("AHASSSS")
	return send_from_directory('static', path)

if __name__ == '__main__':
	app.run(host='127.0.0.1', port='8080')


