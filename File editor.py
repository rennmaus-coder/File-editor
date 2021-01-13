import os, tkinter, sys
import os.path

# christian@palm-family.de
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
def create_shortcut():
    import comtypes
    from comtypes.client import CreateObject
    from comtypes.persist import IPersistFile
    from comtypes.shelllink import ShellLink
    pfad = os.path.dirname(os.path.abspath(sys.argv[0]))

    s = CreateObject(ShellLink)
    s.SetPath(pfad+'\\anwendungen\\converted_files\\')

    p = s.QueryInterface(IPersistFile)
    p.Save(desktop+"\\output.lnk", True)

    s = CreateObject(ShellLink)
    p = s.QueryInterface(IPersistFile)
    p.Load(desktop+"\\output.lnk", True)

def pdf():
    pfad=os.path.dirname(os.path.abspath(sys.argv[0]))
    pfad+='/anwendungen/Pdf editor.py'
    os.popen(pfad)
def cov():
    pfad = os.path.dirname(os.path.abspath(sys.argv[0]))
    pfad += '/anwendungen/Convert Images.py'
    os.popen(pfad)


var=os.path.isfile(desktop+"\\output.lnk")
if var==True:
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