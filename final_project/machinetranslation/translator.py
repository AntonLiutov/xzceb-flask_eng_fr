"""
This module is intended to translate english text to french and 
vice versa
"""

import json
import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
translator_instance = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
translator_instance.set_service_url(url)

def english_to_french(english_text):
    """
    This function translates english text into french
    """
    if len(english_text) != 0: 
        french_text = translator_instance.translate(
            text=english_text,
            model_id='en-fr').get_result()["translations"][0]["translation"]
    else:
        french_text = ""

    return french_text

def french_to_english(french_text):
    """
    This function translates french text into english
    """
    if len(french_text) != 0:
        english_text = translator_instance.translate(
            text=french_text,
            model_id='fr-en').get_result()["translations"][0]["translation"]
    else:
        english_text = ""

    return english_text
