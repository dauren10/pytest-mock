from urllib import response
from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

def get_age():
    response = requests.get("https://api.agify.io/?name=michael").json()
    return response.get('age')

if __name__ == '__main__':
    app.run()