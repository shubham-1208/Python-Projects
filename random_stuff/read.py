from gtts import gTTS 
import os

text = input("text:")
language = "en"

speech = gTTS(text=text, lang=language, slow=False)
speech.save("test.mp3")