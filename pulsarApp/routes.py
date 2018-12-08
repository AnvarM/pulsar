from flask import render_template, request, jsonify, url_for, redirect, flash
from pulsarApp import app
from pulsarApp.forms import PulsarFeedbackForm, GetUserByIdForm, AddUserForm, LoginForm
from time import time, ctime
from pulsarApp import db
from pulsarApp.models import Users, Observations, Admin
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

@app.route("/")
def index():
    form = PulsarFeedbackForm()
    return render_template('index.html', title='Pulsar Form', form=form)

@app.route("/", methods=['POST'])
def post_data():
    form = PulsarFeedbackForm()
    if form.validate_on_submit():
        if (Users.query.filter_by(oneid=request.form['oneviewid']).first()):
            observation = Observations(
            timest = str(ctime(time())),
            date_of_observation = str(request.form['date']),
            oneviewid = str(request.form['oneviewid']),
            shift = str(request.form['shift']),
            department = str(request.form['department']),
            area = str(request.form['area']),
            employee_exam = str(request.form['employee_exam']),
            activity = str(request.form['activity']),
            attention_work = str(request.form['attention_work']),
            attention_road = str(request.form['attention_road']),
            appropriate_tools = str(request.form['appropriate_tools']),
            tools_is_ok = str(request.form['tools_is_ok']),
            ppe = str(request.form['ppe']),
            ppe_special = str(request.form['ppe_special']),
            capture = str(request.form['capture']),
            comment = str(request.form['comments']))

            db.session.add(observation)
            db.session.commit()

            return render_template('thanks.html', msg = "Спасибо за наблюдение, запись сохранена")
        else:
            return render_template('thanks.html', msg="Такого пользователя нет в базе данных, обратитесь к администратору")

    return (render_template('index.html', title='Pulsar Form', form=form))

@app.route("/checkUserObservations")
def checkUserObservations():
    form = GetUserByIdForm()
    return render_template("check_user_observations_form.html", form=form)

@app.route("/addUser")
@login_required
def addUser():
    form = AddUserForm()
    return render_template("add_user.html", form=form)

@app.route("/addUser", methods=['POST'])
def PostUser():
    form = AddUserForm()
    if form.validate_on_submit():
        if (Users.query.filter_by(oneid=request.form['oneviewid']).first()):
            return render_template("thanks.html", msg = "Такой пользователь уже есть в базе данных")
        else:
            user = Users(name = request.form['name'],
                         department = request.form['department'],
                         oneid = request.form['oneviewid'])

            db.session.add(user)
            db.session.commit()

        return render_template('thanks.html', msg = "Пользователь добавлен")

    return render_template("add_user.html", form=form)

@app.route("/getUserObservations")
def getUserObservations():
    oneviewid = str(request.args.get('oneviewid'))
    if (Users.query.filter_by(oneid=oneviewid).first()):
        user = Users.query.filter_by(oneid=oneviewid).first()
        observations = user.observations.order_by(Observations.id.desc()).all()
        amount_of_observations = len(observations)
        return render_template("get_user_observations.html", observations=observations, user = user, amount_of_observations=amount_of_observations )
    else:
        msg = "Такого пользователя нет в базе данных, обратитесь к администратору"
        return render_template('thanks.html', msg=msg)

@app.route("/last50")
def last50():
    last_50_observations = Observations.query.order_by(Observations.id.desc()).limit(50).all()
    return render_template("get_user_observations.html", observations=last_50_observations)


#API
@app.route("/getobservationsbyuserid/<int:oneviewid>")
def getObservationsById(oneviewid):
    if (Users.query.filter_by(oneid=oneviewid).first()):
        return jsonify(Users.getObservationsById(oneviewid))
    else:
        return '{Нет такого пользователя}'

@app.route("/getAllUsers")
def getAllUsers():
    return jsonify(Users.getAllUsers())

@app.route("/getuser/<int:oneid>")
def getuser(oneid):
    if (Users.query.filter_by(oneid=oneid).first()):
        return jsonify(Users.getUser(oneid))
    else:
        return "Такого пользователя не существует"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Admin.query.filter_by(name=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

