from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask('Titan_task')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Решил оставить для наглядности, если в будущем данный проект мне понадобится
# towns = [
#     {'town': 'Moscow',
#      'visit_date':'12.12.2012',
#      'ready': False,
#      'id':0},
#     {'town': 'Beijing',
#      'visit_date':'07.07.2007',
#      'ready':False,
#      'id':1},
#     {'town': 'Washington',
#      'visit_date':'02.02.2002',
#      'ready': False,
#      'id':2}
#
# ]

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    town = db.Column(db.String(500))
    visit_date = db.Column(db.String(20))
    ready = db.Column(db.Boolean, default=False)

    # def __repr__(self):
    #     return f'<City {self.id} / {self.town}> {self.visit_date}'

@app.route('/')
def main():
    towns = City.query.all()
    print(towns)
    return render_template('index.html',
                           cities=towns)

# Для чекбоксов
# @app.route('/ready/<int:city_id>', methods=['PATCH'])
# def modify_city(city_id):
#     towns = City.query.get(city_id)
#     towns.ready = request.json['ready']
#     db.session.commit()
#     # global towns
#     # ready = request.json["ready"]
#     # for city in towns:
#     #     if city['id'] == city_id:
#     #         city.update({'ready':ready})
#     return 'OK'

@app.route('/city', methods=['POST'])
def create_city():
    data = request.get_json()
    town = City(**data)
    db.session.add(town)
    db.session.commit()
    # last_id = towns[-1]['id']
    # new_id = last_id + 1
    # data['id'] = new_id
    # towns.append(data)
    return 'OK'

@app.route('/clear', methods=['DELETE'])
def clear_cities():
    City.query.delete()
    db.session.commit()
    return 'OK'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)