import speech_recognition as sr
def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        r.dynamic_energy_ratio=2.5
        audio = r.listen(source,0,3)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except Exception:
        query=input("Enter user command : ")
    return query