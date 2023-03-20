import requests
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
