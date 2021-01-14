import os, tkinter, sys
from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import filedialog, messagebox, ttk
import pikepdf
import os.path
from PIL import Image
import comtypes
import subprocess
from comtypes.client import CreateObject
from comtypes.persist import IPersistFile
from comtypes.shelllink import ShellLink



def pdf_1():

    # christian@palm-family.de

    pdf_writer=PdfFileWriter()
    app=tkinter.Tk()
    app.title("Pdf editor")
    app.geometry("200x150")


    def merge(name='mergedPDF'):
        files=tkinter.filedialog.askopenfilenames(parent=app, title='Bitte PDFs auswählen', filetypes=[("PDF", ".pdf")])
        for file in app.tk.splitlist(files):
            pdf_reader=PdfFileReader(file)
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))
        bilder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')
        bilder += "/converted_files/"
        with open(bilder+name+".pdf", 'wb') as out:
            pdf_writer.write(out)
            messagebox.showinfo(title="Erfolgreich", message="Dateien erfolgreich verbunden")



    def encrypt_pdf():

        def get():
            password=e.get()
            bilder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')
            bilder += "/converted_files/"
            pdf.save(bilder+ name.split("/")[-1] + "-verschlüsselt.pdf", encryption=pikepdf.Encryption(owner=password, user=password))
            # you can change the R from 4 to 6 for 256 aes encryption
            pdf.close()
            messagebox.showinfo(title="Erfolgreich", message="Datei erfolgreich verschlüsselt")
        name = tkinter.filedialog.askopenfile(filetypes=[("PDF", ".pdf")]).name
        pdf=pikepdf.Pdf.open(name)
        eingabefeld_wert = tkinter.StringVar()
        e=tkinter.Entry(app, textvariable=eingabefeld_wert)
        e.pack()
        tkinter.Button(app, text="confirm", command=get).pack()


    def beenden():
        app.destroy()

    tkinter.Button(app, text="verbinden", command=merge).pack()
    tkinter.Button(app, text="verschlüsseln", command=encrypt_pdf).pack()
    tkinter.Button(app, text="beenden", command=beenden).pack()
    app.mainloop()


def main():
    # christian@palm-family.de
    applic = tkinter.Tk()
    applic.title("File converter")
    bilder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')
    bilder+="/converted_files"

    listboxfile = tkinter.Listbox(applic, selectmode='browse')
    listboxfile.place(x=100, y=250, width=250, height=100)

    def new_img():
        input = tkinter.filedialog.askopenfilenames(parent=applic, title="Dateien auswählen", filetypes=[("PNG", ".png"), ("tiff", ".tiff"), ("GIF", ".gif")])
        listboxfile.delete('0', 'end')
        for file in applic.tk.splitlist(input):
            listboxfile.insert('end', file)
        return input

    def add_img():
        input = tkinter.filedialog.askopenfilenames(parent=applic, title="Dateien auswählen", filetypes=[("PNG", ".png"), ("tiff", ".tiff"), ("GIF", ".gif")])
        for file in applic.tk.splitlist(input):
            listboxfile.insert('end', file)

    applic.geometry("350x350")
    Options=['.png', '.tiff', '.pdf', '.gif', '.TIF']
    variable = tkinter.StringVar(applic)
    variable.set(Options[0])
    opt = tkinter.OptionMenu(applic, variable, *Options)
    opt.config(width=90, font=('Helvetica', 12))
    opt.pack()

    def conv():
        messagebox.showwarning(title='Wichtig!', message='Dateien gleicher Endung werden überschrieben!!')
        input = listboxfile.get('0', 'end')
        i=0
        puffer=os.path.dirname(os.path.abspath(sys.argv[0]))
        for file in applic.tk.splitlist(input):
            f=bilder
            _, e = os.path.splitext(file)
            i+=1
            im = Image.open(file)
            output = f+"/_"+str(i)+variable.get()

            if e == '.tiff' or e == '.png' or e == '.TIF':
                im.save(puffer+'/conv.gif')
                im=Image.open(puffer+'/conv.gif')
                os.remove(puffer+'/conv.gif')
                listboxfile.delete('0', '1')

            else:
                pass

            im.save(output)
        listboxfile.delete('0', 'end')
        messagebox.showinfo(title="Konvertierung erfolgreich", message="Konvertierung erfolgreich!")
    but=tkinter.Button(applic, text="select new files", command=new_img)
    but.place(y=300)
    but.pack()
    tkinter.Button(applic, text="select more files", command=add_img).pack()
    tkinter.Button(applic, text="convert", command=conv).pack()

    def beende():
        applic.destroy()
    tkinter.Button(applic, text="beenden", command=beende).pack()
    applic.mainloop()



# christian@palm-family.de
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
bilder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')
def create_shortcut():

    datei = os.path.realpath(__file__)

    s = CreateObject(ShellLink)
    s.SetPath(datei)

    p = s.QueryInterface(IPersistFile)
    p.Save(desktop+"\\File editor.lnk", True)

    s = CreateObject(ShellLink)
    p = s.QueryInterface(IPersistFile)
    p.Load(desktop+"\\File editor.lnk", True)

    os.makedirs(bilder+"\\converted_files")

def pdf():
    pdf_1()
def cov():
    main()

def install():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'PyPDF2'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pikepdf'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Pillow'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'comtypes'])


var=os.path.isfile(desktop+"\\output.lnk")
var1=os.path.isdir(bilder+"\\converted_files")
if var is True or var1 is True:
    pass
else:
    create_shortcut()
root=tkinter.Tk()
root.title("File editor")
tkinter.Label(root, text="Was möchtest du machen?").pack()
tkinter.Button(root, text="Install needed packages", command=install).pack()
tkinter.Button(root, text="Pdf Editieren", command=pdf).pack()
tkinter.Button(root, text="Bilder convert", command=cov).pack()
root.mainloop()