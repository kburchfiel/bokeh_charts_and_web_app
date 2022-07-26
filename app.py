# Example Flask app
# Based on: https://flask.palletsprojects.com/en/2.1.x/quickstart/

# There's also a Flask tutorial available at:
# https://flask.palletsprojects.com/en/2.1.x/tutorial/

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def print_sample_text():
    return "<p>This Flask app displays a couple Bokeh charts. Each chart currently has its own page.</p>"\

# Follow the instructions on the Quickstart page to run the app:
# https://flask.palletsprojects.com/en/2.1.x/quickstart/

# For Heroku deployment notes, see setup_notes.md.


@app.route('/t10_airports_by_pax')
def retrieve_t10_airports_by_pax_chart(name=None):
    return render_template('t10_airports_by_pax.html', name = name)

@app.route('/t20_airports_by_avg_dist')
def retrieve_t20_airports_by_avg_dist_chart(name=None):
    return render_template('t20_airports_by_avg_dist.html', name = name)


