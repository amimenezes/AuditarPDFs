import os
import sys
from PyPDF2 import PdfFileReader as Reader
from datetime import date

def research_pdfs(path):
    arquivos = ["Nome, Paginas"]
    for root, dirs, files in os.walk(os.path.normpath(path)):
        for f in files:
            if f.endswith(".pdf"):
                try:
                    pdf = Reader(open(os.path.join(root,f), 'rb'))
                    arquivos.append(f+", "+str(pdf.getNumPages()))
                    print(f,':',pdf.getNumPages())
                except:
                    print("Erro ao ler o arquivo", f)
    return arquivos


def main(argv):
    path = os.getcwd()
    csv = research_pdfs(path)
    filename = "relatorio_pdf_"+str(date.today())+".csv"
    with open(filename, "w") as f:
        for item in csv:
            f.write("%s\n" % item)

if __name__ == '__main__':
    main(sys.argv[1:])