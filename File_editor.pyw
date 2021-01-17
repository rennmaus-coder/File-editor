import os, tkinter, sys
from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import filedialog, messagebox
import os.path
from PIL import Image
import comtypes
from comtypes.client import CreateObject
from comtypes.persist import IPersistFile
from comtypes.shelllink import ShellLink

def pdf_1():

    pdf_writer=PdfFileWriter()
    app=tkinter.Tk()
    app.title("Pdf editor")
    app.geometry("400x220")

    def add_files():
        box.delete('0', 'end')
        files = tkinter.filedialog.askopenfilenames(parent=app, title='Bitte PDFs auswählen',
                                                    filetypes=[("PDF", ".pdf")])
        for file in files:
            box.insert('end', file)
        return files

    def merge(name='mergedPDF'):
        work=workflow.get()
        if work==0:
            files=box.get('0', 'end')
            for file in app.tk.splitlist(files):
                pdf_reader=PdfFileReader(file)
                for page in range(pdf_reader.getNumPages()):
                    pdf_writer.addPage(pdf_reader.getPage(page))
            bilder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')
            bilder += "/converted_files/"
            with open(bilder+name+".pdf", 'wb') as out:
                pdf_writer.write(out)
                messagebox.showinfo(title="Erfolgreich", message="Dateien erfolgreich verbunden")

        if work==1:
            files=box.get('0', 'end')
            files=app.tk.splitlist(files)
            e=ein.get()
            e=e.split("-")
            for num in e:
                num=int(num)
                pdf_reader=PdfFileReader(files[num-1])
                for page in range(pdf_reader.getNumPages()):
                    pdf_writer.addPage(pdf_reader.getPage(page))

            bilder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')
            bilder += "/converted_files/"
            with open(bilder + name + ".pdf", 'wb') as out:
                pdf_writer.write(out)
                messagebox.showinfo(title="Erfolgreich", message="Dateien erfolgreich verbunden")

    def encrypt_pdf():

        def get():
            password = e.get()
            for file in app.tk.splitlist(nam):
                pdf_reader = PdfFileReader(file)
                pdf_writer = PdfFileWriter()
                for page in range(pdf_reader.getNumPages()):
                    pdf_writer.addPage(pdf_reader.getPage(page))
                pdf_writer.encrypt(user_pwd=password, use_128bit=True)
                bilder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')
                bilder += "/converted_files/"
                with open(bilder+file.split("/")[-1]+"-verschlüsselt.pdf", "wb") as out:
                    pdf_writer.write(out)
            messagebox.showinfo(title="Erfolgreich", message="Die verschlüsselung war erfolgreich!")

        nam = box.get('0', 'end')
        eingabefeld_wert = tkinter.StringVar()
        e = tkinter.Entry(app, textvariable=eingabefeld_wert)
        e.place(x=100, y=0)
        tkinter.Button(app, text="confirm", command=get).place(x=100, y=20)


    def beenden():
        app.destroy()

    tkinter.Button(app, text="add files", command=add_files).grid()
    tkinter.Button(app, text="verbinden", command=merge).grid()
    tkinter.Button(app, text="verschlüsseln", command=encrypt_pdf).grid()
    tkinter.Button(app, text="beenden", command=beenden).grid()
    box=tkinter.Listbox(app, selectmode='browse')
    box.place(width=400, height=80, y=100)
    workflow = tkinter.IntVar()
    workflow.set(0)
    tkinter.Checkbutton(app, variable=workflow, onvalue=1, offvalue=0).place(x=0, y=200)
    workflow.set(1)
    ein=tkinter.Entry(app)
    ein.place(x=20, y=200)
    app.mainloop()


def pic():
    applic = tkinter.Tk()
    applic.title("File converter")
    bilder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')
    bilder+="/converted_files"

    listboxfile = tkinter.Listbox(applic, selectmode='browse')
    listboxfile.place(x=100, y=250, width=250, height=100)
    types= r" *.png  *.tiff  *.gif  *.jpg  *.ico"

    def new_img():
        input = tkinter.filedialog.askopenfilenames(parent=applic, title="Dateien auswählen", filetypes=[("Bilder:", types)])
        listboxfile.delete('0', 'end')
        for file in applic.tk.splitlist(input):
            listboxfile.insert('end', file)
        return input

    def add_img():
        input = tkinter.filedialog.askopenfilenames(parent=applic, title="Dateien auswählen", filetypes=[("Bilder:", types)])
        for file in applic.tk.splitlist(input):
            listboxfile.insert('end', file)

    applic.geometry("350x350")
    Options=['.png', '.tiff', '.pdf', '.gif', '.TIF', '.ico', '.jpg']
    variable = tkinter.StringVar(applic)
    variable.set(Options[0])
    opt = tkinter.OptionMenu(applic, variable, *Options)
    opt.config(width=90, font=('Helvetica', 12))
    opt.pack()

    def conv():
        messagebox.showwarning(title='Wichtig!', message='Dateien gleicher Endung werden überschrieben!!')
        input = listboxfile.get('0', 'end')
        i=0
        puffer = os.path.dirname(os.path.abspath(sys.argv[0]))
        for file in applic.tk.splitlist(input):
            try:
                os.remove(puffer+"/conv.gif")
            except:
                pass
            f=bilder
            _, e = os.path.splitext(file)
            i+=1
            im = Image.open(file)
            output = f+"/_"+str(i)+variable.get()

            if e == '.tiff' or e == '.png' or e == '.TIF':
                im.save(puffer + '/conv.gif')
                im = Image.open(puffer + '/conv.gif')
            if im.mode != 'RGB' and variable.get() == '.jpg':
                im = im.convert('RGB')
            if variable.get() == '.jpg':
                im.save(output, "JPEG")

            else:
                pass
            im.save(output)

        if check == 1:
            listboxfile.delete('0', 'end')

        else:
            pass

        messagebox.showinfo(title="Konvertierung erfolgreich", message="Konvertierung erfolgreich!")
    but=tkinter.Button(applic, text="select new files", command=new_img)
    but.place(y=300)
    but.pack()
    tkinter.Button(applic, text="select more files", command=add_img).pack()
    tkinter.Button(applic, text="convert", command=conv).pack()
    check = tkinter.IntVar()
    tkinter.Checkbutton(applic, text="Dateiliste danach verwerfen", variable=check, onvalue=1, offvalue=0).place(y=210, x=100)
    check.set(1)

    def beende():
        applic.destroy()
    tkinter.Button(applic, text="beenden", command=beende).pack()
    applic.mainloop()

def main():
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    bilder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')
    def create_folder():

        os.makedirs(bilder+"\\converted_files")

    def create_shortcut():
        datei = os.path.abspath(sys.argv[0])

        s = CreateObject(ShellLink)
        s.SetPath(datei)

        p = s.QueryInterface(IPersistFile)
        p.Save(desktop + "\\File editor.lnk", True)

        s = CreateObject(ShellLink)
        p = s.QueryInterface(IPersistFile)
        p.Load(desktop + "\\File editor.lnk", True)

    def pdf():
        pdf_1()
    def cov():
        pic()


    var1=os.path.isdir(bilder+"\\converted_files")

    if var1 is not True:
        create_folder()

    root=tkinter.Tk()
    root.title("File editor")
    tkinter.Label(root, text="Was möchtest du machen?").pack()
    tkinter.Button(root, text="Pdf editor", command=pdf).pack()
    tkinter.Button(root, text="Picture convert", command=cov).pack()
    tkinter.Button(root, text="Create shortcut", command=create_shortcut).pack()
    root.mainloop()

if __name__ == '__main__':
    main()