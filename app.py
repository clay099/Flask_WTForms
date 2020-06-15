from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///pet_adoption"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.config['SECRET_KEY'] = 'Secret'
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def home():
    """
    show alls pets in database
    """
    available_pets = Pet.query.filter_by(available=True).all()
    adopted_pets = Pet.query.filter_by(available=False).all()

    return render_template('home.html', available_pets=available_pets, adopted_pets=adopted_pets)


@app.route('/add', methods=["GET", 'POST'])
def new_pet():
    """
    form to add new pet & validation to add to database
    """

    form = PetForm()

    if form.validate_on_submit():
        # ===original method below====
        # name = form.name.data
        # species = form.species.data
        # photo_url = form.photo_url.data
        # age = form.age.data
        # notes = form.notes.data
        # available = form.available.data
        # pet = Pet(name=name, species=species, photo_url=photo_url, age = age, notes = notes, available = available)

        # method to loop over dictionary so that it updates if new fields get added
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        # the input data looks like === new_pet = Pet(name=form.name.data, age=form.age.data, ...)

        db.session.add(new_pet)
        db.session.commit()

        flash(f'{new_pet.name} added', 'alert alert-success')

        return redirect('/')
    else:
        return render_template('new_pet_form.html', form=form)


@ app.route('/<int:pet_id>')
def pet_details(pet_id):
    """
    show all pet details
    """

    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet_details.html', pet=pet)


@ app.route('/<int:pet_id>/edit', methods=["GET", "POST"])
def edit_pet_details(pet_id):
    """
    edit the pets details with form pre-filled
    validates form before submitting to database
    """

    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        flash(f'{pet.name} edited', 'alert alert-success')

        return redirect('/')
    else:
        return render_template('edit_pet_details.html', form=form)
