import requests

# This succesfully get the documents from the API


class ApiHandler:

    def send_data(self, payload):
        response = requests.post(
            "https://api.gptzero.me/v2/predict/text", json=payload)
        if response.status_code == 200:
            print("Data sent successfully")
            return response.json()
        else:
            print("Failed to send data")
            print(response.status_code)
            return None

    def send_file(self, file_path):
        file_endpoint = "https://api.gptzero.me/v2/predict/files"
        file = {'file': open(file_path, 'rb')}
        response = requests.post(self.url + file_endpoint, files=file)
        if response.status_code == 200:
            print("File sent successfully")
            return response.json()
        else:
            print("Failed to send file")
            return None


api = ApiHandler()

payload = {
    "document": "No, this code will not work as a standalone application. It will only make API requests and print the results to the console. To integrate it with a Flask application and make it accessible through HTML and JavaScript, you need to make additional modifications.",
}

response_data = api.send_data(payload)
if response_data is not None:
    print(response_data)

#response_file = api.send_file("file.txt")
# if response_file is not None:
 #   print(response_file)
