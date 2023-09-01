from flask import jsonify, redirect, render_template, request, url_for
from app.models.user import db, User
from app import app

@app.route("/", methods=["GET"])
def home():
    vals = User.query.all()
    return render_template("index.html", students=vals)

@app.route("/user/", methods=["POST"])
def create():
    if request.method == 'POST':
        firstname = request.form['first_name']
        lastname = request.form['last_name']
        middlename = request.form['middle_name']

        user = User(first_name=firstname, last_name=lastname, middle_name=middlename)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template("index.html")

@app.route('/<int:id>/edit/', methods=['POST'])
def edit(id):
    user = User.query.get_or_404(id)
    
    if request.method == 'POST':
        firstname = request.form['first_name']
        print("xfirstname->", firstname)
        lastname = request.form['last_name']
        middlename = request.form['middle_name']

        user.first_name = firstname
        user.lastname = lastname
        user.middle_name = middlename
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('home'))
    
@app.route('/user/edit/', methods=['POST', 'GET'])
def user_edit():

    if request.method == 'POST':
        id = request.form['id']
        user = User.query.get_or_404(id)
        print("user->", user)
        return jsonify({'htmlresponse': render_template('response.html', student=user)})
        pass
