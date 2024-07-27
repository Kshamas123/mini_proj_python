import pyttsx3 #text to speeech conversion library in python,it works offline
import datetime

engine=pyttsx3.init('sapi5') #to take the voice
voices=engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[1].id)
# print(voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
if __name__=="__main__":
    t=datetime.datetime.now()
    if(t.hour>=0 and t.hour<12):
        speak('good morning,have a good day')
    if(t.hour>=12 and t.hour<=19):
        speak('good after noon')
    if(t.hour>=19 and t.hour<24):
        speak('good night and have a good sleep')
