import os, tkinter, sys

# christian@palm-family.de

def pdf():
    pfad=os.path.dirname(os.path.abspath(sys.argv[0]))
    pfad+='/anwendungen/Pdf editor.py'
    os.popen(pfad)
def cov():
    pfad = os.path.dirname(os.path.abspath(sys.argv[0]))
    pfad += '/anwendungen/Convert Images.py'
    os.popen(pfad)
root=tkinter.Tk()
tkinter.Label(root, text="Was möchtest du machen?").pack()
tkinter.Button(root, text="Pdf Editieren", command=pdf).pack()
tkinter.Button(root, text="Bilder convert", command=cov).pack()
root.mainloop()