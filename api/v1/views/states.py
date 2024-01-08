#!/usr/bin/python3
""" state view """
from api.v1.views import app_views
from flask import jsonify, make_response, abort, request
from models import storage
from models.state import State


@app_views.route('/states', methods=["GET", "POST"], strict_slashes=False)
def get_states_post_states():
    """ retrieves all state objects """
    if request.method == 'GET':
        output = []
        states = storage.all(State).values()
        for state in states:
            output.append(state.to_dict())
        return (jsonify(output))
    if request.method == 'POST':
        data = request.get_json()
        if not request.is_json:
            abort(400, description="Not a JSON")
        if 'name' not in request.json:
            abort(400, description="Missing name")
        state = State(**data)
        state.save()
        return (jsonify(state.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=["GET", "PUT"],
                 strict_slashes=False)
def get_state(state_id):
    """ retrieves one unique state object """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if request.method == "GET":
        output = state.to_dict()
        return (jsonify(output))
    if request.method == "PUT":
        print("test\n")
        data = request.get_json()
        if not request.is_json:
            abort(400, description="Not a JSON")
        for key, value in data.items():
            setattr(state, key, value)
        state.save()
        return (jsonify(state.to_dict()), 200)


@app_views.route('/states/<state_id>', methods=["GET", "DELETE"],
                 strict_slashes=False)
def delete_state(state_id):
    """ deletes one unique state object """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    result = make_response(jsonify({}), 200)
    return result
