from flask import Flask, render_template, redirect, url_for, session, request
from flask_session import Session
import msal
import config

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Define constants
SCOPE = ['User.ReadBasic.All']

# Define tenant configuration directly in app.py
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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    session["flow"] = _build_auth_code_flow(scopes=tenants['sebastian']['scope'])
    return render_template("login.html", auth_url=session["flow"]["auth_uri"])

@app.route('/getAToken')
def authorized():
    try:
        cache = _load_cache()
        result = _build_msal_app(cache=cache).acquire_token_by_auth_code_flow(session.get("flow", {}), request.args)
        if "error" in result:
            return render_template("auth_error.html", result=result)
        session["user"] = result.get("id_token_claims")
        _save_cache(cache)
    except ValueError:
        pass  # Usually caused by CSRF, simply ignore
    return redirect(url_for("home"))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(
        tenants['sebastian']['authority'] + "/oauth2/v2.0/logout" +
        "?post_logout_redirect_uri=" + url_for("home", _external=True))

def _build_msal_app(cache=None):
    return msal.ConfidentialClientApplication(
        tenants['sebastian']['client_id'], 
        authority=tenants['sebastian']['authority'],
        client_credential=tenants['sebastian']['client_secret'], 
        token_cache=cache
    )

def _build_auth_code_flow(**kwargs):
    return _build_msal_app().initiate_auth_code_flow(**kwargs)

def _load_cache():
    cache = msal.SerializableTokenCache()
    if session.get("token_cache"):
        cache.deserialize(session["token_cache"])
    return cache

def _save_cache(cache):
    if cache.has_state_changed:
        session["token_cache"] = cache.serialize()

if __name__ == "__main__":
    app.run(debug=True)

    





