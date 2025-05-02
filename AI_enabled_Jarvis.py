import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio
from openai import OpenAI

# Configure OpenAI client to use Groq
client = OpenAI(
    api_key="your_api_goes_here",
    base_url="https://api.groq.com/openai/v1"
)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except:
            return None
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-pk')
        print(f"User said: {query}")
    except Exception as e:
        print("Say that again please...")
        return None
    return query

def greet():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How may I help you?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YOUR_EMAIL@gmail.com', 'YOUR_APP_PASSWORD')  # App Password is safer
    server.sendmail('YOUR_EMAIL@gmail.com', to, content)
    server.close()

def get_ai_response(prompt):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are Jarvis, a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    greet()
    while True:
        query = takecommand()
        if not query:
            continue
        query = query.lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

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
            # speak("Let me think...")         
            ai_reply = get_ai_response(query)
            speak(ai_reply)
