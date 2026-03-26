import requests 
    



def sentiment_analyzer(text_to_analyse): # Define a function named sentiment_analyzer that takes a string as input (text_to_analyse)
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict' # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } } # Create a dictionary with the text to analyze
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"} # Define the required headers for the API request
    response = requests.post(url, json = myobj, headers=header) # Send a POST request to the API with the text and headers
    return response.text # Return the text of the API response

