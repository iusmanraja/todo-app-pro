import os
from flask import Flask, jsonify
from flask_cors import CORS
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/tasks')
def get_tasks():
    token = os.getenv("TODOIST_API_TOKEN")
    url = "https://api.todoist.com/rest/v2/tasks"
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=3000)