import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests
from openai import OpenAI
# from gtts import gTTS
# import pygame
# import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
news_api = "2589f17d5274400a8e681f0a7fba6259"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(api_key="sk-proj-EXEkntSbzKxPMX1qyHfRT3BlbkFJtssOOOzr4WHuMBHiRuqX",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )
    return completion.choices[0].message.content

def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music_library.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])

            for article in articles:
                speak(article['title'])

    else:
        #let openai handle it
        output = aiProcess(c)
        speak(output) 

if __name__ == "__main__":
    speak("Initializing Alexa")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            print("Recognizing...")
            word = r.recognize_google(audio)
            if("alexa" in word.lower()):
                speak("yes boss")

                with sr.Microphone() as source:
                    print("Alexa Active...")
                    audio = r.listen(source, timeout=2, phrase_time_limit=1)
                    c = r.recognize_google(audio)
                    process_command(c)

        except Exception as e:
            print("Error; {0}".format(e))