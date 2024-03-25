import PyPDF2
import deepl
import config

auth_key = config.auth_key # Change this to your own DeepL API key
translator = deepl.Translator(auth_key) 

FILE_NAME = '1.pdf' # Change this to the name of the PDF file you want to translate

pdfFileObj = open(FILE_NAME,'rb')  
pdfReader = PyPDF2.PdfReader(pdfFileObj)
number_of_pages = len(pdfReader.pages)

with open('output.csv', 'a') as f:
    f.write(f'Page Number, Japanese Sentence, English Sentence\n')

for a in range(0, number_of_pages):
    pageObj = pdfReader.pages[a]     
    text = pageObj.extract_text().replace('\n', '')
    sentences = text.split('。')
    for sentence in sentences:
        if sentence == '':
            continue
        translated_text = translator.translate_text(sentence, target_lang='EN-GB')
        with open('output.csv', 'a') as f:
            f.write(f'{a}, {sentence.strip()}, "{translated_text}"\n')

pdfFileObj.close()