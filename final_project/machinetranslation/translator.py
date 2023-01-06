import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url(url)
# language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    """translates english to french"""
    try:
        french_text = language_translator.translate(
            text=english_text,
            model_id='en-fr'
        ).get_result()
    except:
        english_text == ""

    return french_text['translations'][0]['translation']

def french_to_english(french_text):
    """translates french to english"""
    try:
        english_text = language_translator.translate(
            text=french_text,
            model_id='fr-en'
        ).get_result()
    except:
        french_text == ""
    return english_text['translations'][0]['translation']

def eng_to_hebrew(text):
    try:
        english_text = language_translator.translate(
            text=text,
            model_id='en-he'
        ).get_result()
    except:
        text == ""
    return english_text['translations'][0]['translation']

def eng_to_spanish(text):
    try:
        english_text = language_translator.translate(
            text=text,
            model_id='en-es'
        ).get_result()
    except:
        text == ""
    return english_text['translations'][0]['translation']

def eng_to_chinese(text):
    try:
        english_text = language_translator.translate(
            text=text,
            model_id='en-zh'
        ).get_result()
    except:
        text == ""
    return english_text['translations'][0]['translation']




















# translation = language_translator.translate(text="hello can i have some money please", model_id='en-he').get_result()

# print(f"Translating: Hello can I have some money please: {translation['translations'][0]['translation']}")
