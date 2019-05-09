import azure.cognitiveservices.speech as speechsdk
import time
"""
import yaml
import io

try:
    config = yaml.safe_load(open("config.yaml","r"))
except yaml.YAMLError as error:
        print(error)
"""

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "f930f892f1284edba0671f94d784807b", "JapanEast"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region, speech_recognition_language = "jp-JP")


# Creates a recognizer with the given settings
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

print("Say something...")


# Starts speech recognition, and returns after a single utterance is recognized. The end of a
# single utterance is determined by listening for silence at the end or until a maximum of 15
# seconds of audio is processed.  The task returns the recognition text as result. 
# Note: Since recognize_once() returns only a single utterance, it is suitable only for single
# shot recognition like command or query. 
# For long-running multi-utterance recognition, use start_continuous_recognition() instead.
speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
speech_recognizer.session_stopped.connect(lambda evt: print('\nSESSION STOPPED {}'.format(evt)))
speech_recognizer.recognized.connect(lambda evt: print('\n{}'.format(evt.result.text)))

speech_recognizer.start_continuous_recognition_async()
time.sleep(20)
speech_recognizer.stop_continuous_recognition_async()

speech_recognizer.session_started.disconnect_all()
speech_recognizer.recognized.disconnect_all()
speech_recognizer.session_stopped.disconnect_all()