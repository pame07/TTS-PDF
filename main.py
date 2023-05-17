import pyttsx3 # Initialize the library
import PyPDF2


pdf_file = open('C:/Users/Seba/Downloads/Howls_of_Zelania_removed.pdf', 'rb')
read_pdf = PyPDF2.PdfReader(pdf_file, strict=False)


number_of_pages = len(read_pdf.pages)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id) # 2 is the 3rd item index

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

for i in range(0, number_of_pages ):
    # Read the PDF page 
    page = read_pdf.pages[i]
    
    # Extract the text of the PDF page 
    page_content = page.extract_text()
        
    # say method on the engine that passing input text to be spoken 
    engine.say(page_content) 
    
    # run and wait method to processes the voice commands.  
    engine.runAndWait()

engine.runAndWait()

