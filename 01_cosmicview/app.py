# Import Flask from flask package
from flask import Flask, render_template

# Create new app from flask object
app = Flask(__name__)


# Define routes and the function that will run when that route is called.
@app.route('/')
def index():
    title = 'CosmicView'
    # Display html template using render_template and send it to the page, and we can place the title value
    return render_template('index.html', title=title)


@app.route('/buy')
def buy():
    return 'Buy'


@app.route('/sell')
def sell():
    return 'Sell'


@app.route('/settings')
def settings():
    return 'Settings'
