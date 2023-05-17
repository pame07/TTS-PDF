import pyttsx3 # Initialize the library
import PyPDF2


pdf_file = open('C:/Users/Seba/Downloads/test.pdf', 'rb')

pdfReader = PyPDF2.PdfReader(pdf_file)

print("Pages Number:", len(pdfReader.pages))

file1=open(r"C:/Users/Seba/Downloads/convertedtext.txt","a")

for i in range(0, len(pdfReader.pages)):
        pageObj = pdfReader.pages[i]
        text = pageObj.extract_text()
        file1.writelines(text)

file1.close()

book = open('C:/Users/Seba/Downloads/convertedtext.txt', 'r', encoding='latin-1').read()\
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

