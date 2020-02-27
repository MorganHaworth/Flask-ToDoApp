from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import ItemForm
from app.models import ToDoItem

@app.route("/")
@app.route("/index")
def home():
    items = ToDoItem.query.all()
    return render_template('index.html', title='Home', items=items)

@app.route("/addItem", methods=["GET", "POST"])
def add():
    form = ItemForm()
    if form.validate_on_submit():
        flash('Here')
        toDoItem = ToDoItem(item=form.item.data, completed=form.completed.data)
        db.session.add(toDoItem)
        db.session.commit()
        flash('Added item!')
        return redirect(url_for('home'))
    else:
        flash('Bad')
    return render_template('addItem.html', form=form)