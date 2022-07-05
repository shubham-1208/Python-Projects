#import library
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable

with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        # using google speech recognition
        file = open("speech1.txt", "w")
        l = "Text: "+r.recognize_google(audio_text, language = "en-EN")
        file.write("HELLO \n")
        file.writelines(l)
        file.close()
        print("speech is saved in speech1.txt")
        print("Text: "+r.recognize_google(audio_text, language = "en-EN"))
    except:
         print("Sorry, I did not get that")

#print(“Text: “+r.recognize_google(audio_text, language = “fr-FR”))