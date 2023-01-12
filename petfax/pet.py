from flask import ( Blueprint, render_template ) 
import json 

pets = json.load(open('pets.json'))
print(pets)



bp = Blueprint('pet', __name__, url_prefix="/pets")

""" @bp.route('/')
def index(): 
    return 'This is the pets index' """

@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)

@bp.route("/<int:id>")
def fact(id):
    pet = pets[id - 1]
    return render_template('fact.html', pet=pet)