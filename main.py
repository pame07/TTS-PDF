import pyttsx3 # Initialize the library



#pdf_file = open('C:/Users/Seba/Downloads/test.pdf', 'rb')
book = open('C:/Users/Seba/Downloads/test.txt', 'r', encoding="utf-8").read()\
        .replace('\n\n', '*newline*')\
        .replace('\n', ' ')\
        .replace('*newline*', '\n\n')


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id) 

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)


engine.save_to_file(book, "test.mp3")
# run and wait method to processes the voice commands.  
engine.runAndWait()

