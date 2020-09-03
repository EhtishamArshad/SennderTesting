from flask import Flask, render_template
from flask_apscheduler import APScheduler
import api

films = {}
cast = {}

app = Flask(__name__)

scheduler = APScheduler()


@app.route('/')
def default_route():
    return '<a href=/movies>Get Movies List</a>', 200


@app.route('/movies')
def get_movies():
    results = []

    if isinstance(films, list) and films:
        for film in films:
            result = {'movie': '', 'cast': []}
            movie_url = film['url']
            result['movie'] = film['title']
            for person in cast:
                if movie_url in person['films']:
                    result['cast'].append(person['name'])
            if not result['cast']:
                result['cast'].append('No cast information found')
            results.append(result)
        return render_template('index.html', results=list(results)), 200
    else:
        return '<h1>No valid information available</h1>', 301


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


def scheduled_task():
    global films
    global cast
    if films != api.get_films_list():
        films = api.get_films_list()
    if cast != api.get_people_list():
        cast = api.get_people_list()


if __name__ == '__main__':
    scheduler.add_job(
        id='Scheduled Task',
        func=scheduled_task,
        trigger='interval',
        seconds=59)
    scheduler.start()
    if not films:
        films = api.get_films_list()

    if not cast:
        cast = api.get_people_list()

    app.run(host='localhost', port=8000)
    app.run(debug=True)
