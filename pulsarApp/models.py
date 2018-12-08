from pulsarApp import db, login
from json import dumps
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return Admin.query.get(int(id))

class Observations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timest = db.Column(db.String(50))
    date_of_observation = db.Column(db.String(20))
    oneviewid = db.Column(db.String(8),db.ForeignKey('users.oneid'), index=True )
    shift = db.Column(db.String(20))
    department = db.Column(db.String(50))
    area = db.Column(db.String(100))
    employee_exam = db.Column(db.String(50))
    activity = db.Column(db.String(50))
    attention_work = db.Column(db.String(20))
    attention_road = db.Column(db.String(20))
    appropriate_tools = db.Column(db.String(20))
    tools_is_ok = db.Column(db.String(20))
    ppe = db.Column(db.String(20))
    ppe_special = db.Column(db.String(20))
    capture = db.Column(db.String(20))
    comment = db.Column(db.String(1000))

    #def __repr__(self):
    #    return '(timest={}, oneviewid={},shift={}, department={},area={}, employee_exam={}, activity={})'.format(self.timest,
    #    self.oneviewid, self.shift, self.department,self.area, self.employee_exam,self.activity)
    def json(self):
        return {'timest' : self.timest, 'oneviewid' : self.oneviewid, 'shift' : self.shift, 'department' : self.department, 'area' : self.area, 'employee_exam' : self.employee_exam,
                'activity' : self.activity, 'attention_work' : self.attention_work, 'attention.road' : self.attention_work, 'appropriate_tools' : self.appropriate_tools,
                'tools_is_ok' : self.tools_is_ok, 'ppe' : self.ppe, 'ppe_special' : self.ppe_special, 'capture' : self.capture, 'comment' : self.comment}

    def __repr__(self):
        observationObject = {
            'id' : self.id,
            'timest' : self.timest,
            'date_of_observation' : self.date_of_observation,
            'oneviewid' : self.oneviewid,
            'shift' : self.shift,
            'department' : self.department,
            'area' : self.area,
            'employee_exam' : self.employee_exam,
            'activity' : self.activity,
            'attention_work' : self.attention_work,
            'attention_road': self.attention_road,
           'appropriate_tools' : self.appropriate_tools,
            'tools_is_ok' : self.tools_is_ok,
            'ppe' : self.ppe,
            'ppe_special' : self.ppe_special,
            'capture' : self.capture,
            'comment' : self.comment
       }
        return dumps(observationObject)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    department = db.Column(db.String(50))
    oneid = db.Column(db.String(8), unique=True)
    observations = db.relationship('Observations', backref='user', lazy='dynamic')

    def json(self):
        return {'name' : self.name, 'department' : self.department, 'odeid' : self.oneid}

    def getAllUsers():
        users = Users.query.all()
        return [Users.json(user) for user in users]

    def getUser(oneid):
        user = Users.query.filter_by(oneid=oneid).first()
        return Users.json(user)

    def getObservationsById(oneid):
        user = Users.query.filter_by(oneid=oneid).first()
        observations = user.observations.all()
        return [Observations.json(observation) for observation in observations]

    def __repr__(self):
        userObject = {
            'name' : self.name,
            'department' : self.department,
            'oneid' : self.oneid
        }
        return dumps(userObject)

class Admin(UserMixin,db.Model):
    id = id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

