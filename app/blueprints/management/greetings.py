import json
import random

from flask import Blueprint, current_app, request
from app.database.models import Greeting

greetings_management = Blueprint('greetings_management', __name__)



@greetings_management.route('/random', methods=['GET'])
def get_random_greeting():
    greet_query = Greeting.query
    query_rows = int(greet_query.count())
    random_greeting = greet_query.offset(int(query_rows * random.random())).first()

    if random_greeting:
        response_greet = {'id': random_greeting.id, 'response': random_greeting.response}
        return json.dumps(response_greet), 200, {'Content-Type': 'application/json'}
    else:
        return json.dumps({'status': 'Greeting not found.'}), 400, {'Content-Type': 'application/json'}


@greetings_management.route('/new', methods=['POST'])
def add_greeting():
    content = request.json
    if content and content['greeting']:
        greeting_response = content['greeting']
        greeting = Greeting.query.filter(Greeting.response == greeting_response).first()

        if greeting:
            return json.dumps({'status': 'Greeting already exists.'}), 400, {'Content-Type': 'application/json'}
        else:
            greeting = Greeting()
            greeting.response = greeting_response
            current_app.db.session.add(greeting)
            current_app.db.session.commit()

            return '', 204
    else:
        return json.dumps({'status': 'Bad request'}), 400, {'Content-Type': 'application/json'}

