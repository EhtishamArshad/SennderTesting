from flask import Flask, render_template
from flask_apscheduler import APScheduler
import api

films = {}
cast = {}

app = Flask(__name__)

scheduler = APScheduler()


@app.route('/')
# default Route
def default_route():
    return '<a href=/movies>Get Movies List</a>', 200


@app.route('/movies')
# route for movies list
def get_movies():
    results = []

    # check if the param of films contains valid data
    if isinstance(films, list) and films:
        for film in films:
            # declaration of dict containing information of movie name and cast properties
            result = {'movie': '', 'cast': []}
            movie_url = film['url']
            result['movie'] = film['title']
            # looping through people list to get the cast names for each movie
            for person in cast:
                if movie_url in person['films']:
                    result['cast'].append(person['name'])
            if not result['cast']:
                result['cast'].append('No cast information found')
            results.append(result)
        # rendering template with results
        return render_template('index.html', results=list(results)), 200
    else:
        # rendering result in case of failed API response
        return '<h1>No valid information available</h1>', 301


@app.errorhandler(404)
# managing 404 cases
def page_not_found(e):
    return render_template('404.html'), 404


# scheduler function that is being triggered every minute by a backend running scheduler
def scheduled_task():
    global films
    global cast

    if films != api.get_films_list():
        films = api.get_films_list()
    if cast != api.get_people_list():
        cast = api.get_people_list()


if __name__ == '__main__':
    # scheduler job to trigger while running as a backend service
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
