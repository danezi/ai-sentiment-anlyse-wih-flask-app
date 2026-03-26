import requests
import json

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict' # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } } # Constructing the request payload in the expected format
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"} # Custom header specifying the model ID for the sentiment analysis service
    response = requests.post(url, json=myobj, headers=header) # Sending a POST request to the sentiment analysis API
    formatted_response = json.loads(response.text) # Parsing the JSON response from the API
    label = formatted_response['documentSentiment']['label'] # Extracting sentiment label from the response
    score = formatted_response['documentSentiment']['score'] # Extracting sentiment score from the response
    return {'label': label, 'score': score} # Returning a dictionary containing sentiment analysis results
