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

'''
this route handles the data from the user and if the response data is not none it render another html page result.html
it also passes arguments that contain the data from the api and the other three data that should be seen by users
which is avg_perplexity_score, highest_perplexity_score and finally the burstiness_score
'''
@app.route('/process_form', methods=['POST'])
def process_form():
    document = request.form['document']
    payload = {'document': document}
    response_data = api.send_data(payload)
    if response_data is not None:
        avg_perplexity_score, perplexity_score, burstiness_score = extract_scores(response_data)
        return render_template(
            'result.html',
            result=response_data, 
            avg_perplexity_score=avg_perplexity_score, 
            highest_perplexity_score=perplexity_score, 
            burstiness_score=burstiness_score
            )
    else:
        return "Failed to send data"


def calculate_avg_perplexity(data):
    total_perplexity = 0
    total_sentences = 0
    for document in data:
        sentences = document['sentences']
        for sentence in sentences:
            perplexity = sentence['perplexity']
            total_perplexity += perplexity
            total_sentences += 1
    if total_sentences > 0:
        return total_perplexity / total_sentences
    else:
        return 0


def get_highest_perplexity(data):
    perplexities = [sentence['perplexity']
                    for sentence in data[0]['sentences']]
    return max(perplexities)


def extract_scores(data):
    avg_perplexity_score = calculate_avg_perplexity(data)
    perplexity_score = get_highest_perplexity(data)
    burstiness_score = data[0]['overall_burstiness']
    return avg_perplexity_score, perplexity_score, burstiness_score


if __name__ == '__main__':
    app.run(debug=True)
