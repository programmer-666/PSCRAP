import fitz
from os import listdir, mkdir
from functions import saveText
from functions import folders

def start_pdf2txt():
    for folder in folders:
        pdf_files = [i for i in listdir(path = folder) if i[-4:] == ".pdf"]

        folder_path = folder+"/"
        for pdf in pdf_files:
            with fitz.open(folder_path+pdf) as doc:
                text = ""
                for page in doc:
                    text+=page.get_text()
                saveText(pdf[:-4], text, folder)
