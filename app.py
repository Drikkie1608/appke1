from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    service_name = 'appke2-service'
    api_url = f'http://{service_name}:80'
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.text
        else:
            return 'Error'
    except Exception as e:
        return str(e)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
