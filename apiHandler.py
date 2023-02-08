import requests

class ApiHandler:
    def __init__(self, url, path):
        self.url = url
        self.path = path

    def send_data(self, payload):
        response = requests.post(self.url, json=payload)
        if response.status_code == 200:
            print("Data sent successfully")
            return response.json()
        else:
            print("Failed to send data")
            return None

    def send_file(self, file_path):
        file = {'file': open(file_path, 'rb')}
        response = requests.post(self.url, files=file)
        if response.status_code == 200:
            print("File sent successfully")
            return response.json()
        else:
            print("Failed to send file")
            return None


api = API("https://gptzero.me/open_api.json")

payload = {
    "key1": "value1",
    "key2": "value2"
}

response_data = api.send_data(payload)
if response_data is not None:
    print(response_data)

response_file = api.send_file("file.txt")
if response_file is not None:
    print(response_file)
