import requests
import json

def emotion_detector(text_to_analyze ):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_data= { "raw_document": { "text": text_to_analyze } }

    response= requests.post(url=url,headers=headers,json=json_data)
    response_text=json.loads(response.text)
    format_json={
        'anger': response_text['emotionPredictions'][0]['emotion']['anger'],
        'disgust': response_text['emotionPredictions'][0]['emotion']['disgust'],
        'fear': response_text['emotionPredictions'][0]['emotion']['fear'],
        'joy': response_text['emotionPredictions'][0]['emotion']['joy'],
        'sadness': response_text['emotionPredictions'][0]['emotion']['sadness'],
        'dominant_emotion': response_text['producerId']['name']
    }

    return format_json


