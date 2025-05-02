import pyttsx3  # Text-to-speech conversion library
import speech_recognition as sr  # Recognizes speech from audio input
import datetime  # Provides date and time functionalities
import wikipedia  # Fetches summaries from Wikipedia
import webbrowser  # Opens web pages in a browser
import os  # Interacts with the operating system
import smtplib  # Sends emails via SMTP
import pyaudio  # Captures and plays audio input/output

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    """Function to take voice input from the user."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-pk')
        print(f"User said: {query}")
    except Exception as e:
        print("Say that again, please...")
        return None
    return query

# def greet():
#     """Function to greet the user."""
#     hour = int(datetime.datetime.now().hour)
#     if 0 <= hour < 12:
#         speak("Good Morning!")
#     elif 12 <= hour < 18:
#         speak("Good Afternoon!")
#     elif 18 <= hour < 24:  
#         speak("Good Night!")  
#     else:
#         speak("Good Evening!")
#     speak("I am Jarvis. How may I help you?")

def greet():
    """Function to greet the user."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How may I help you?")

def sendEmail(to, content):
    """Function to send email."""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nk2739668@gmail.com', 'nVeenKuMar32004') #Koi login krne ki takleef na uthaye😒
    server.sendmail('nk2739668@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    greet()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        
        elif 'open google' in query:
            webbrowser.open("google.com")  
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 

        elif "open calendar" in query:
                os.system("start outlookcal:")

        elif "open camera" in query:
                os.system("start microsoft.windows.camera:")

        elif "open notepad" in query:
                os.system("start notepad")

        elif "open calculator" in query:
                os.system("start calculator:") 

        elif 'open code' in query:
            codePath = "C:/Users/ADMIN/Desktop/Python/project.py" 
            os.startfile(codePath)

        elif 'play music' in query:
            music_dir = "C:/Users/ADMIN/Desktop/Python/project.py/songs/"
            songs = os.listdir(music_dir)  
            print(songs)  
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'email to naveen' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "naveen332720@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry! I am not able to send this email")
        else:
            speak("Unable to hear")
