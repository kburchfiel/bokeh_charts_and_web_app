# Example Flask app
# Source: https://flask.palletsprojects.com/en/2.1.x/quickstart/
# Changed name to 'main' according to the directions shown in:
# https://www.geeksforgeeks.org/deploy-python-flask-app-on-heroku/

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def print_sample_text():
    return "<p>Here is some sample text within a Flask app.</p>"\

# Follow the instructions on the Quickstart page to run the app:
# https://flask.palletsprojects.com/en/2.1.x/quickstart/


@app.route('/charts')
def show_charts():
    return 'Charts will go here.'

@app.route('/t10_airports_by_pax')
def retrieve_t10_airport_by_pax_chart(name=None):
    return render_template('t10_airports_by_pax.html', name = name)

# Flask tutorial:
# https://flask.palletsprojects.com/en/2.1.x/tutorial/
