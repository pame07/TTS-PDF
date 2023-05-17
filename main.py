import pyttsx3 # Initialize the library
import PyPDF2


#pdf_file = open('C:/Users/Seba/Downloads/test.pdf', 'rb')
book = open('C:/Users/Seba/Downloads/test.txt', 'r', encoding="utf-8").read()\
        .replace('\n\n', '*newline*')\
        .replace('\n', ' ')\
        .replace('*newline*', '\n\n')

#read_pdf = PyPDF2.PdfReader(book, strict=False)


#number_of_pages = len(read_pdf.pages)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id) # 2 is the 3rd item index

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)


engine.save_to_file(book, "test.mp3")
# run and wait method to processes the voice commands.  
engine.runAndWait()

