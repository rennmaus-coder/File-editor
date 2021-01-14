import os, tkinter, sys
import os.path

# christian@palm-family.de
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
bilder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')
def create_shortcut():
    import comtypes
    from comtypes.client import CreateObject
    from comtypes.persist import IPersistFile
    from comtypes.shelllink import ShellLink
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
    pfad=os.path.dirname(os.path.abspath(sys.argv[0]))
    pfad+='/anwendungen/Pdf editor.py'
    os.popen(pfad)
def cov():
    pfad = os.path.dirname(os.path.abspath(sys.argv[0]))
    pfad += '/anwendungen/Convert Images.py'
    os.popen(pfad)


var=os.path.isfile(desktop+"\\output.lnk")
var1=os.path.isdir(bilder+"\\converted_files")
if var is True or var1 is True:
    pass
    print("True")
else:
    create_shortcut()
    print("nein")
root=tkinter.Tk()
tkinter.Label(root, text="Was möchtest du machen?").pack()
tkinter.Button(root, text="Pdf Editieren", command=pdf).pack()
tkinter.Button(root, text="Bilder convert", command=cov).pack()
root.mainloop()