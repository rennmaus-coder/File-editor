import tkinter, os, sys, time
from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import filedialog

pdf_writer=PdfFileWriter()
root=tkinter.Tk()
root.geometry("200x100")


def merge(name='mergedPDF'):
    files=tkinter.filedialog.askopenfilenames(parent=root, title='Bitte PDFs auswählen', filetypes=[("PDF", ".pdf")])
    for file in root.tk.splitlist(files):
        pdf_reader=PdfFileReader(file)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    pfad=os.path.dirname(os.path.abspath(sys.argv[0]))
    with open(pfad+"\\"+name+".pdf", 'wb') as out:
        pdf_writer.write(out)
    time.sleep(1.5)


def encrypt_pdf():
    import pikepdf

    def get():
        password=e.get()
        pdf.save(name + "-verschlüsselt.pdf", encryption=pikepdf.Encryption(owner=password, user=password))
        # you can change the R from 4 to 6 for 256 aes encryption
        pdf.close()
    name = tkinter.filedialog.askopenfile(filetypes=[("PDF", ".pdf")]).name
    pdf=pikepdf.Pdf.open(name)
    eingabefeld_wert = tkinter.StringVar()
    e=tkinter.Entry(root, textvariable=eingabefeld_wert)
    e.pack()
    tkinter.Button(root, text="confirm", command=get).pack()


def beenden():
    root.destroy()

tkinter.Button(root, text="verbinden", command=merge).pack()
tkinter.Button(root, text="verschlüsseln", command=encrypt_pdf).pack()
tkinter.Button(root, text="beenden", command=beenden).pack()
root.mainloop()