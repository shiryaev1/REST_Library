import json

import pytest


def create_user(client):
    response = client.post('/api/', {
        "username": "Alex2000",
        "first_name": "Alex",
        "last_name": "Vandurov",
        "password": "123123"
    })

    return response.data[0].get('id'), response.status_code


def create_book(client, user_id):
    response = client.post(f'/api/lib/{user_id}/', {
        "owner": user_id,
        "title": "Python",
        "content": "best language",
        "author": "Test Author"
    })
    return response.data[0].get('id'), response.status_code


def update_book(client, user_id, book_id):
    response = client.put(f'/api/book/{book_id}/edit/', json.dumps({
        "owner": user_id,
        "title": "Python",
        "content": "best language!!!",
        "author": "Test other Author"
    }), content_type='application/json')
    return response.data['id'], response.status_code


@pytest.mark.django_db
def test_create_user(client):
    user_id, status_code = create_user(client)
    assert user_id is not None
    assert status_code == 201


@pytest.mark.django_db
def test_create_book(client):
    user_id, status_code = create_user(client)
    assert user_id is not None
    assert status_code == 201
    book_id, status_code = create_book(client, user_id)
    assert book_id is not None
    assert status_code == 201


@pytest.mark.django_db
def test_update_book(client):
    user_id, status_code = create_user(client)
    assert user_id is not None
    assert status_code == 201
    book_id, status_code = create_book(client, user_id)
    assert book_id is not None
    assert status_code == 201
    book_id, status_code = update_book(client, user_id, book_id)
    assert book_id is not None
    assert status_code == 200
