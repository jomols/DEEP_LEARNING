import pyttsx3
txt_sp=pyttsx3.init()
voices = txt_sp.getProperty('voices')

# On most Windows systems, index 0 is male (David) and index 1 is female (Zira)
txt_sp.setProperty('voice', voices[1].id)
text=input("Enter text: ")
txt_sp.setProperty('volume', 1.0)
txt_sp.setProperty('rate', 50)
txt_sp.say(text)
txt_sp.runAndWait()