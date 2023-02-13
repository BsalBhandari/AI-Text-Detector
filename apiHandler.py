from flask import Flask, render_template, request
import requests

app = Flask(__name__)


class ApiHandler:
    def send_data(self, payload):
        response = requests.post(
            "https://api.gptzero.me/v2/predict/text", json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def send_file(self, file_path):
        file_endpoint = "https://api.gptzero.me/v2/predict/files"
        file = {'file': open(file_path, 'rb')}
        response = requests.post(file_endpoint, files=file)
        if response.status_code == 200:
            return response.json()
        else:
            return None


api = ApiHandler()

## index is the first webpage that should be render in this webpage


@app.route('/')
def index():
    return render_template('index.html')


# this route handles the data from the user and if the response data is not none it return another html page result.html and the passes the result
@app.route('/process_form', methods=['POST'])
def process_form():
    document = request.form['document']
    payload = {'document': document}
    response_data = api.send_data(payload)
    if response_data is not None:
        return render_template('result.html', result=response_data)
    else:
        return "Failed to send data"


if __name__ == '__main__':
    app.run(debug=True)
