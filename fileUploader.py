import requests
class Fileuploader:
    def __init__(self, api_url):
        self.api_url = api_url

    def upload_file(self, file_path):
        file = {'file': open(file_path, 'rb')}
        response = requests.post(self.api_url, files=file)
        if response.status_code == 200:
            print("File uploaded successfully")
        else:
            print("File upload failed")

    def upload_text(self, text):
        data = {'text': text}
        response = requests.post(self.api_url, data=data)
        if response.status_code == 200:
            print("Text uploaded successfully")
        else:
            print("Text upload failed")
