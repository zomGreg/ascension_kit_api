from app import db

class Game(db.Model):
    gid = db.Column(db.INT, primary_key=True, autoincrement=True)
    align0 = db.Column(db.VARCHAR(length=3), primary_key=False, nullable=True)
    deathlev = db.Column(db.INT)
    uid = db.Column(db.INT)
    deaths = db.Column(db.INT)
    turns = db.Column(db.INT)
    points = db.Column(db.INT)
    death = db.Column(db.VARCHAR(length=250))
    realtime = db.Column(db.INT)
    version = db.Column(db.VARCHAR(length=7))
    role = db.Column(db.VARCHAR(length=3))
    conduct = db.Column(db.INT, nullable=True)
    gender0 = db.Column(db.VARCHAR(length=3))
    deathdate = db.Column(db.DATETIME)
    hp = db.Column(db.INT)
    achieve = db.Column(db.INT)
    gamedelta = db.Column(db.INT)
    maxlvl = db.Column(db.INT)
    maxhp = db.Column(db.INT)
    endtime = db.Column(db.DATETIME)
    nachieves = db.Column(db.INT)
    nconducts = db.Column(db.INT)
    name = db.Column(db.VARCHAR(length=64))
    gender = db.Column(db.VARCHAR(length=3))
    align = db.Column(db.VARCHAR(length=3))
    birthdate = db.Column(db.DATETIME)
    race = db.Column(db.VARCHAR(length=3))
    flags = db.Column(db.INT)
    starttime = db.Column(db.DATETIME, nullable=True)
    deathdnum = db.Column(db.INT)