from application import app
from flask import render_template
from application.controllers.functions import get_distance, validations_mkad, get_location_destiny
from application.models.forms import GetCoordinates


@app.route('/index', methods=["GET", "POST"])
@app.route('/', methods=["GET", "POST"])
def index():
    form = GetCoordinates()
    destination = form.destiny.data
    if destination is None or destination.isspace():
        return render_template('index.html',
                               form=form)
    else:
        coordinates = get_location_destiny(destination)
        if coordinates == 'ERROR: Address not find ':
            result = 'ERROR: Address not find'
        elif validations_mkad(coordinates) != 0:
            result = "The specified address is located inside the MKAD"
        else:
            result = get_distance(coordinates)

        return render_template('index.html',
                               form=form, result=result)
