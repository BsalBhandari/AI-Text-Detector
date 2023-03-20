from flask import Flask, render_template, request
from dataHandler import DataHandler
from apiHandler import *

app = Flask(__name__, template_folder="templates")

api = ApiHandler()
data_handler = DataHandler()
# index is the first webpage that should be render in this webpage

@app.route('/')
def index():
    return render_template('index.html')

'''
this route handles the data from the user and if the response data is not none it render another html page result.html
it also passes arguments that contain the data from the api and the other three data that should be seen by users
which is avg_perplexity_score, highest_perplexity_score and finally the burstiness_score
'''

# @app.route('/process_form', methods=['POST'])
@app.route('/process_form', methods=['POST'])
def process_form():
    document = request.form['parameter']
    # return document
    payload = {'document': document}
    # return payload
    response_data = api.send_data(payload)
    return response_data
    # if response_data is not None:

    #     return response_data
    # else:
    #     return "Failed to send dat"
    if response_data is not None:
        avg_perplexity_score, perplexity_score, burstiness_score = data_handler.extract_scores(
            response_data)
        return render_template(
            'templates/index.html',
            result=response_data,
            avg_perplexity_score=avg_perplexity_score,
            highest_perplexity_score=perplexity_score,
            burstiness_score=burstiness_score
        )
    else:
        return "Failed to send data"
