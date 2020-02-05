def test_home(client):
    r=client.get('/')
    r.status == '200'

def test_get(client):
    a=client.get('/api/v1.0/users')
    a.status == '200'

def test_get1(client):
    b=client.get('/api/v1.0/users/1')
    b.status == '200'

def test_get2(client):
    c=client.get('/api/v1.0/users/?user_id=1')
    c.status == '200'