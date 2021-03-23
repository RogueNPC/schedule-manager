"""Import packages and modules."""
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, datetime
from scheduling_app.models import Load, User
from scheduling_app.main.forms import LoadForm
from scheduling_app import bcrypt

# Import app and db from events_app package so that we can run app
from scheduling_app import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    return render_template('home.html')

@main.route('/new_load', methods=['GET', 'POST'])
@login_required
def new_load():
    # Creates a LoadForm
    form = LoadForm()

    # If form was submitted and was valid:
    if form.validate_on_submit():
        new_load = Load(
            load_number=form.load_number.data,
            date_and_time=form.date_and_time.data,
            shipping_order_number=form.shipping_order_number.data,
            customer=form.customer.data,
            trucker=form.trucker.data,
            pallet_amount=form.pallet_amount.data,
            pickup=form.pickup.data
        )
        db.session.add(new_load)
        db.session.commit()

        flash('New load was successfully entered.')
        return redirect(url_for('main.load_detail', load_id=new_load.id))
    return render_template('create_load.html', form=form)
    # load_number = IntegerField('Load Number', validators=[DataRequired()])
    # date_and_time = DateTimeField('Date and Time Scheduled', validators=[DataRequired()])
    # shipping_order_number = IntegerField('Shipping Order Number', validators=[DataRequired()])
    # customer = StringField('Customer', validators=[DataRequired(), Length(min=3, max=80)])
    # trucker = StringField('Trucker', validators=[DataRequired(), Length(min=3, max=80)])
    # pallet_amount = IntegerField('Pallet Amount', validators=[DataRequired()])
    # pickup = BooleanField('Pickup?')
    # submit = SubmitField('Submit')

@main.route('/load/<load_id>', methods=['GET', 'POST'])
@login_required
def load_detail(load_id):
    """Load description"""
    load = Load.query.get(load_id)
    form = LoadForm(obj=load)

    # if form was submitted and contained no errors
    if form.validate_on_submit():
        # Populates the attributes of the passed obj with data from the form's fields
        form.populate_obj(load)
        db.session.add(load)
        db.session.commit()

        flash('Load was edited successfully.')
        return redirect(url_for('main.load_detail', load_id=load.id))
    load = Load.query.get(load_id)
    return render_template('load_detail.html', load=load, form=form)

@main.route('/delete/<load_id>', methods=['POST'])
@login_required
def delete(load_id):
    """Deletes load"""
    load = Load.query.get(load_id)
    db.session.delete(load)
    db.session.commit()
    # redirects to schedule.html (our user's database)
    return redirect(url_for("main.schedule"))