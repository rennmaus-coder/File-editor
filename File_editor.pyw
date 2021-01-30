import os, tkinter, sys
from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import filedialog, messagebox
import os.path
from PIL import Image
from comtypes.client import CreateObject
from comtypes.persist import IPersistFile
from comtypes.shelllink import ShellLink
from glob import glob
from random import randint
import webbrowser, math

# christian@palm-family.de


root=tkinter.Tk()

def pdf_1():

    pdf_writer=PdfFileWriter()
    app=tkinter.Toplevel(root)
    app.title("Pdf editor")
    app.geometry("400x220")

    def split_pdf():
        bilder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')
        bilder += "/converted_files/"
        num = 0
        files = box.get('0', 'end')
        for file in app.tk.splitlist(files):
            pdf_reader = PdfFileReader(file)
            for page in range(pdf_reader.getNumPages()):
                num+=1
                pdf_writerr = PdfFileWriter()
                pdf_writerr.addPage(pdf_reader.getPage(page))
                with open(bilder + "splited_page_" +str(num) + ".pdf", 'wb') as out:
                    pdf_writerr.write(out)
        messagebox.showinfo("Erfolgreich", "Das aufteilen der Seiten war erfolgreich!")


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

    tkinter.Button(app, text="add files", command=add_files).grid(column=0, row=2)
    tkinter.Button(app, text="verbinden", command=merge).grid(column=5, row=2)
    tkinter.Button(app, text="verschlüsseln", command=encrypt_pdf).grid(column=10, row=2)
    tkinter.Button(app, text="aufteilen", command=split_pdf).grid(column=15, row=2)
    tkinter.Button(app, text="beenden", command=beenden).grid(column=20, row=2)
    box=tkinter.Listbox(app, selectmode='browse')
    box.place(width=400, height=120, y=70)
    workflow = tkinter.IntVar()
    workflow.set(0)
    tkinter.Checkbutton(app, variable=workflow, onvalue=1, offvalue=0).place(x=0, y=200)
    workflow.set(0)
    ein=tkinter.Entry(app)
    ein.place(x=20, y=200)
    app.mainloop()


def pic():
    applic = tkinter.Toplevel(root)
    applic.title("File converter")
    bilder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')
    bilder+="/converted_files"

    listboxfile = tkinter.Listbox(applic, selectmode='browse')
    listboxfile.place(x=100, y=250, width=250, height=100)
    types = r" *.png  *.tiff  *.gif  *.jpg  *.ico"

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
    qual=tkinter.StringVar()
    tkinter.Entry(applic, textvariable=qual).place(x=5, y=150)

    def conv():
        input = listboxfile.get('0', 'end')
        i=0
        puffer = os.path.dirname(os.path.abspath(sys.argv[0]))
        for file in applic.tk.splitlist(input):
            f=bilder
            name, e = os.path.splitext(file)
            name = name.split("/")[-1]
            i+=1
            im = Image.open(file)
            output = f+"/"+name+"_"+str(i)+variable.get()
            if output in glob(bilder+"/"):
                output = f+"/_"+str(randint(1, 100)*2)+variable.get()

            def save():
                im.save(output, "JPEG", quality=int(qual.get()))

            if e == '.tiff' or e == '.png' or e == '.TIF':
                im.save(puffer + '/conv.gif')
                im = Image.open(puffer + '/conv.gif')
            if im.mode != 'RGB' and variable.get() == '.jpg':
                im = im.convert('RGB')
            if variable.get() == '.jpg' and qual.get() != '':
                save()
            if variable.get() == '.jpg' and qual.get == '':
                im.save(output, "JPEG")


            else:
                pass
            im.save(output)

        if check.get() == 1:
            listboxfile.delete('0', 'end')

        else:
            pass
        try:
            os.remove(puffer + "/conv.gif")
        except:
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

def comp():
    compress = tkinter.Toplevel(root)
    compress.geometry("250x150")
    tkinter.Label(compress, text="Prozent der Ursprünglichen Auflösung").pack()
    prozent=tkinter.Entry(compress)
    prozent.pack()
    def compress_pic():
        bilder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')
        bilder += "/converted_files/"
        pic_types = r" *.png  *.tiff  *.gif  *.jpg  *.ico  *.TIF  *.psd  *.svg"
        file = tkinter.filedialog.askopenfilename(master=compress, filetypes=[("Bilder", pic_types)])
        try:
            foo = Image.open(file)
            x, y = foo.size

            def get():
                return prozent.get()

            proz = get()
            x2, y2 = math.floor(x / (100 / int(proz))), math.floor(y / (100 / int(proz)))
            foo = foo.resize((x2, y2), Image.ANTIALIAS)
            endung = file.split(".")[-1]
            file_save = file.split("/")[-1]
            foo.save(bilder + file_save + "_comp_." + endung)
            messagebox.showinfo("Erfolgreich", "Kompression erfolgreich")
        except:
            messagebox.showinfo("Bild Auswählen", "Bitte wählen sie ein Bild aus")

    tkinter.Button(compress, text="compress", command=compress_pic).pack()

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
    def new_v():
        try:
            webbrowser.open_new_tab('https://mega.nz/folder/0PQUWJBY#5uzbZalOMbdzTT4RqfW1ig')
        except:
            res = messagebox.askquestion(title="Inkompabilität", message="Ihr Browser wird wahrscheinlich nicht unterstützt. Wenn sie auf Ja drücken, wird folgender Link kopiert:\nhttps://mega.nz/folder/0PQUWJBY#5uzbZalOMbdzTT4RqfW1ig")
            if res == 'yes':
                try:
                    root.clipboard_clear()
                finally:
                    root.clipboard_append("https://mega.nz/folder/0PQUWJBY#5uzbZalOMbdzTT4RqfW1ig")

    var1=os.path.isdir(bilder+"\\converted_files")

    if var1 is not True:
        create_folder()

    root.title("File editor 1.1.1")
    root.geometry("400x175")
    tkinter.Label(root, text="Was möchtest du machen?").pack()
    tkinter.Button(root, text="Pdf editor", command=pdf).pack()
    tkinter.Button(root, text="Picture convert", command=cov).pack()
    tkinter.Button(root, text="Compress Picture", command=comp).pack()
    tkinter.Button(root, text="Neue Version suchen", command=new_v).pack()
    tkinter.Button(root, text="Create shortcut", command=create_shortcut).pack()
    root.mainloop()

if __name__ == '__main__':
    main()