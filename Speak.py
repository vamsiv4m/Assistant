import pyttsx3
import sys
import torch
from Listen import takeCommand
import Sketch as sk
import random
import User_Requests as rq
from Automation import notepad,close_notepad
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 170)

FILE="Responses.pth"
data=torch.load(FILE)
print(data)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def again():
    speak("Tell me what to note")
    mytxt=takeCommand()
    speak("please see the preview")
    print(mytxt)
    return mytxt

if __name__ == '__main__':
    speak(rq.wishme())
    speak("I am virtual sketch assistant!")
    while True:
        query = takeCommand().lower()
        speaker = ['hello', 'hi', 'hey', 'hai','are you there', 'wake up']
        responses=data['hello_response']
        sketch=data['sketch_response']
        bye=data['bye_response']
        if query in speaker:
            speak(random.choices(responses[0]))

        elif "sketch" in query or "draw" in query:
            speak(random.choices(sketch[0]))
            speak("please select a file...")
            sk.sketch()

        elif 'note' in query:
            mytxt=again()
            speak("Would you like to save the text?")
            save_or_not=takeCommand().lower()
            if "save" in save_or_not or "perfect" in save_or_not:
                notepad(mytxt)
            else:
                again()

        elif "day" in query:
            speak(rq.tellDay())
        
        elif "day tomorrow" in query:
            speak(rq.tell_Tomorrow_Day())

        elif "time" in query:
            speak(rq.tellTime())

        elif "bye" in query or "shutdown" in query:
            speak(random.choices(bye[0]))
            sys.exit()