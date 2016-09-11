# import the Flask class from the flask module
from flask import Flask, render_template, request, jsonify, flash, redirect
from flask.ext.mongoengine import MongoEngine
from forms import FormGeneral

import estimates

import sys
sys.path.insert(0, 'rides-python-sdk/example')
from find_dest import main_function

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/', methods=['GET', 'POST'])
def home():
	form = FormGeneral(request.form, csrf_enabled = False)
	if request.method == 'POST' and form.validate():
		meters = 1609 * int(form.distanceHigh.data)
		destination = main_function(40.8075, -73.9626, form.oneDollar.data, form.twoDollar.data, form.threeDollar.data, form.fourDollar.data, meters)
		return redirect('lyft')
	return render_template('main.html', form=form)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

@app.route('/lyft')
def lyft():
    return render_template('lyft.html', myeta=estimates.get_eta)  # render a template

@app.route('/uber')
def uber():
    return render_template('uber.html', myfunction=request_a_ride.get_time_estimate)  # render a template

@app.route('/uber/request')
def requestUber():
	ride_details = request_a_ride.get_ride_details()
  	return ride_details

@app.route('/_location_data')
def get_loc_data():
	a = request.args.get('a')
	b = request.args.get('b')
	estimates.set_eta(a,b)
	return jsonify(result=a)

    
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)