def test_register_user(test_client, init_database):
    response = test_client.post('/auth/register',
        data={
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'password',
            'password2': 'password'
        },
        follow_redirects=True)
    assert response.status_code == 200
    assert b'Account created' in response.data

def test_login_user(test_client, init_database):
    response = test_client.post('/auth/login',
        data={
            'email': 'test@example.com',
            'password': 'password'
        },
        follow_redirects=True)
    assert response.status_code == 200
    assert b'Logout' in response.data