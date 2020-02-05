from flask import json
from random import randrange

def test_home(client):
    r=client.get('/')
    r.status == '200'

def test_get(client):
    r=client.get('/api/v1.0/users')
    r.status == '200'

def test_get1(client):
    r=client.get('/api/v1.0/users/1')
    r.status == '200'

def test_post(client):
    n = randrange(0,100)
    n_string = str(n)
    name = 'tzaza'
    j = {
        'name':'tzaza',
        'email': n_string + 'cailzaza@mail.com',
        'description': 'zzzzzzzzzz',
        'avatar': 'https://images.unsplash.com/photo-1558981359-219d6364c9c8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60'
    }
    r=client.post('/api/v1.0/users', data=json.dumps(j), content_type='application/json')
    assert r.status_code == 200
    assert r.json['id'] is not None
    assert type(r.json['id']) is int
    assert r.json['email'] is not None
    assert r.json['name'] is not None
    assert type(r.json['name']) is str
    assert r.json['name'] == name

def test_put(client):
    j = {
        'name':'tizia',
        'email':'prova46@mail.com',
        'description': 'prova',
        'avatar': 'https://images.unsplash.com/photo-1558981359-219d6364c9c8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60'
    }
    r=client.put('/api/v1.0/users/4', data=json.dumps(j), content_type='application/json')
    assert r.status_code == 200

def test_get2(client):
    r=client.get('/api/v1.0/users/?user_id=4')
    r.status == '200'

def test_get7(client):
    r=client.get('/api/v1.0/users/?user_id=1')
    r.status == '404'


def test_delete(client):
    r=client.delete('/api/v1.0/users/?user_id=30')
    r.status == '200'