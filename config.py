# config.py

SCOPE = ['User.ReadBasic.All']

tenants = {
    'tenant1': {
        'client_id': 'YOUR_CLIENT_ID_1',
        'client_secret': 'YOUR_CLIENT_SECRET_1',
        'tenant_id': 'YOUR_TENANT_ID_1',
        'authority': 'https://login.microsoftonline.com/YOUR_TENANT_ID_1',
        'redirect_uri': 'http://localhost:5000/tenant1/getAToken',
        'scope': SCOPE,
        'session_type': 'filesystem'
    },
    'tenant2': {
        'client_id': 'YOUR_CLIENT_ID_2',
        'client_secret': 'YOUR_CLIENT_SECRET_2',
        'tenant_id': 'YOUR_TENANT_ID_2',
        'authority': 'https://login.microsoftonline.com/YOUR_TENANT_ID_2',
        'redirect_uri': 'http://localhost:5000/tenant2/getAToken',
        'scope': SCOPE,
        'session_type': 'filesystem'
    },
    'sebastian': {
        'client_id': 'YOUR_CLIENT_ID_SEBASTIAN',
        'client_secret': 'YOUR_CLIENT_SECRET_SEBASTIAN',
        'tenant_id': '30f0c31a-ea3a-431d-970e-1356adb6123c',
        'authority': 'https://login.microsoftonline.com/30f0c31a-ea3a-431d-970e-1356adb6123c',
        'redirect_uri': 'http://localhost:5000/sebastian/getAToken',
        'scope': SCOPE,
        'session_type': 'filesystem'
    }
}

app_globals = tenants['sebastian']  # Or choose another tenant if needed




