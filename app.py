import requests
from flask import Flask, render_template, request

app = Flask('Titan_task')

towns = [
    {'town': 'Moscow',
     'visit_date':'12.12.2012',
     'ready': False,
     'id':0},
    {'town': 'Beijing',
     'visit_date':'07.07.2007',
     'ready':False,
     'id':1},
    {'town': 'Washington',
     'visit_date':'02.02.2002',
     'ready': False,
     'id':2}

]

@app.route('/') # обработчик, что то возвращающий на главную страницу
def main():
    return render_template('index.html',
                           cities =  towns)

@app.route('/ready/<int:city_id>', methods=['PATCH'])
def modify_city(city_id):
    global towns
    ready = request.json["ready"]
    for city in towns:
        if city['id'] == city_id:
            city.update({'ready':ready})
    return 'OK'

@app.route('/city', method=['POST'])
def create_city():
    data = request.json()
    last_id = towns[-1]['id']
    new_id = last_id + 1
    data['id'] = new_id
    towns.append(data)
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)