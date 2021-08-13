from app import app
from flask import render_template
from app.controllers.functions import get_distance, validations_mkad
from app.models.forms import GetCoordinates


@app.route('/index', methods=["GET", "POST"])
@app.route('/', methods=["GET", "POST"])
def index():
    form = GetCoordinates()
    destinations = form.destiny.data
    if destinations is None:
        return render_template('index.html',
                               form=form)
    else:
        result = get_distance(destinations)
        return render_template('index.html',
                               form=form, result=result)
