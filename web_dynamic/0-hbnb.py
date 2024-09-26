#!/usr/bin/python3
""" App that integrates with AirBnB static HTML Template"""


from flask import Flask, render_template, url_for
from models import storage
import uuid



app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


@app.teardown_appcontext
def teardown_db(exception):
    """
    call close() after each rewquest in SQLAlchemy session
    """
    storage.close()


@app.route('/0-hbnb/')
def hbnb_filters(the_id=None):
    """
    handles custom template requests with states, cities & amentities
    """
    state_objects = storage.all('State').values()
    states = dict([state.name, state] for state in state_objects)
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    cache_id = (str(uuid.uuid4()))
    return render_template('1-hbnb.html',
                           states=states,
                           amens=amens,
                           places=places,
                           users=users,
                           cache_id=cache_id)


if __name__ == "__main__":
    app.run(host=host, port=port)
