from flask import request
from pulsarApp import app
from pulsarApp import db
from pulsarApp.models import Users, Observations

@app.route("/getobservationsbyuserid/<int:oneviewid>")
def getuserbyid(oneviewid):
    if (Users.query.filter_by(oneid=oneviewid).first()):
        user =  Users.query.filter_by(oneid=oneviewid).first()
        observations = user.observations.all()
        return observations
    else:
        return '{Нет такого пользлвателя}'