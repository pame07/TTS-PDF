import pyttsx3 # Initialize the library


engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(f"Voice: {voice.name}")

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

engine.setProperty("voice", voices[1].id) # 2 is the 3rd item index
engine.say("Esta es una prueba de texto")

engine.runAndWait()

