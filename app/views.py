from app import app, models
from flask import request, jsonify
from flask import render_template

@app.route('/')
def index():
#    return "Hello, World!"
    return render_template("index.html")

@app.route('/test/')
def test():
    return "Hello, there!"

@app.route('/users/', methods=['GET'])
def users():
    if request.method == 'GET':
        #results = models.Game.query.limit(10).offset(0).all()
        # results = models.Game.query.all()
        zomgreg = models.Game.query.filter_by(name='zomgreg', death='ascended').all()

        json_results = [z.points for z in zomgreg]

        # for result in zomgreg:
            # u={'name': result.points}

            # json_results.append(u)

        return jsonify(points=json_results)
