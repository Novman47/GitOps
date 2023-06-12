from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Triggering deployment from git webhook and in sysn with Argo-CD!!!'
