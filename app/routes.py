from flask import render_template, jsonify
from app import app, db
from .forms import AddSnackForm, AddALocation
from .models import Snacks

def delete_snacks():
    snacks = Snacks.query.all()
    for snack in snacks:
        db.session.delete(snack)
    db.session.commit()

@app.route('/')
def home():
    snacks_to_disp = Snacks.query.filter_by(out=False).all()
    return render_template('home.html', welcome='Welcome to SnackOverflow!', snacks=snacks_to_disp)

@app.route('/wereout/<snackname>')
def outofsnack(snackname):
    snack=Snacks.query.filter_by(snackname=snackname).first()
    snack.out=True
    db.session.commit()
    return home()

@app.route('/moresnacks', methods=['GET', 'POST'])
def moresnacks():
    myform = AddSnackForm()
    message = ""
    #add stuff to database
    if myform.validate_on_submit():
        newsnack_name = myform.question.data
        duplicates = Snacks.query.filter_by(snackname=newsnack_name).all()
        if not duplicates:
            newsnack = Snacks(newsnack_name)
            db.session.add(newsnack)
            db.session.commit()
            myform.question.data=""
        else:
            message = "Cannot duplicate snack"

    return render_template('moresnacks.html', form=myform, message=message)

@app.route('/shoppinglist')
def shoppinglist():
    snacks_to_disp = Snacks.query.filter_by(out=True).order_by(Snacks.bumps.desc()).all()
    locationform = AddALocation()
    return render_template('shoppinglist.html', snacks=snacks_to_disp, form=locationform)

@app.route('/restock/<snackname>', methods=['GET', 'POST'])
def restock(snackname):
    snack = Snacks.query.filter_by(snackname=snackname).first()
    locationform = AddALocation()

    if locationform.validate_on_submit():
        snack.out = False
        snack.bumps = 0
        snacklocation = locationform.location.data
        snack.location = snacklocation
        db.session.commit()
        locationform.location.data=""

    return shoppinglist()



@app.route('/addlocation/<snackname>', methods=['GET', 'POST'])
def addlocation(snackname):
    snack = Snacks.query.filter_by(snackname=snackname).first()
    locationform = AddALocation()

    if locationform.validate_on_submit():
        snacklocation = locationform.location.data
        snack.location = snacklocation
        db.session.commit()
        locationform.location.data=""
        return shoppinglist()

    return render_template('addlocation.html', form=locationform, snack=snack.snackname)

@app.route('/bump/<snackname>')
def bump(snackname):
    snack = Snacks.query.filter_by(snackname=snackname).first()
    snack.bumps+=1
    db.session.commit()
    return jsonify({'bumps': snack.bumps})

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
