from flask import Flask

from helpers.get_random_car import get_random_car

app = Flask(__name__)


@app.route("/")
def give_me_a_car():
    car = get_random_car()

    return {
        "car": car
    }, 200
