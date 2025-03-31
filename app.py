import requests
from flask import Flask, render_template, request

app = Flask('Titan_task')

towns = [
    {'town': 'Moscow',
     'visit_date':'12.12.2012',
     'id':0},
    {'town': 'Beijing',
     'visit_date':'07.07.2007',
     'id':1},
    {'town': 'Washington',
     'visit_date':'02.02.2002',
     'id':1},

]

@app.route('/') # обработчик, что то возвращающий на главную страницу
def main():
    return render_template('index.html',
                           cities =  towns)

@app.route('/ready/<int:task_id>')
def modify_city(city_id):
    global towns
    ready = requests.json["ready"]
    for city in towns:
        if city['id'] == task_id
    return ''



if __name__ == '__main__':
    app.run(debug=True)