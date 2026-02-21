import speech_recognition as sr
def speech_text():
    r=sr.Recognizer()
    while True:
        with sr.Microphone() as source: #source is the object  microphone is the class
            print("speek.........")
            audio=r.listen(source)
            try:
                text=r.recognize_google(audio) #google api for converting audio to text
                print("your speech is recorded ",text)
            except:
                print("you are not audible")
            break
                
speech_text()