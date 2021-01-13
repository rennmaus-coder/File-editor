def main():
    # christian@palm-family.de
    from PIL import Image
    import os, tkinter, glob, random
    from tkinter import filedialog, messagebox, ttk
    root = tkinter.Tk()

    listboxfile = tkinter.Listbox(root, selectmode='browse')
    listboxfile.place(x=100, y=250, width=250, height=100)
    def new_img():
        input = tkinter.filedialog.askopenfilenames(parent=root, title="Dateien auswählen", filetypes=[("PNG", ".png"),("tiff", ".tiff"),("GIF", ".gif")])
        listboxfile.delete('0', 'end')
        for file in root.tk.splitlist(input):
            listboxfile.insert('end', file)
        return input

    root.geometry("350x350")
    listboxNamen = tkinter.Listbox(master=root, selectmode='browse')
    listboxNamen.insert('end', '.png')
    listboxNamen.insert('end', '.tiff')
    listboxNamen.insert('end', '.pdf')
    listboxNamen.insert('end', '.gif')
    listboxNamen.place(width=65, height=70)

    def conv():
        messagebox.showwarning(title='Wichtig!', message='Dateien gleicher Endung werden überschrieben!!\nPS: Dateiendung auswählen nicht vergessen')
        input = listboxfile.get('0', 'end')
        listeAusgewaehlt = listboxNamen.curselection()
        itemAusgewaehlt = listeAusgewaehlt[0]
        nameAusgewaehlt = listboxNamen.get(itemAusgewaehlt)
        num=random.randint(1, 20000)
        z=0
        for file in root.tk.splitlist(input):
            z+=1
            im = Image.open(file)
            f, e=os.path.splitext(file)
            i=0
            output = f + nameAusgewaehlt
            bol=False

            if e == '.tiff' or e == '.png':
                im.save(f+'.gif')
                im=Image.open(f+'.gif')

            else:
                pass

            while output in glob.glob(file):
                output = f +"_"+num+nameAusgewaehlt
                if i==100:
                    bol=True
                    messagebox.showerror(title='error', message='Nach 100 versuchen wurde der Vorgang abgebrochen')
                    break
            if bol==False:
                im.save(output)
                print(f"Datei: {output} wurde erfolgreich abgespeichert ({z}/{len(root.tk.splitlist(input))})")
            else:
                break
    but=tkinter.Button(root, text="select files", command=new_img)
    but.place(y=300)
    but.pack()
    tkinter.Button(root, text="convert", command=conv).pack()
    def beende():
        root.destroy()
    tkinter.Button(root, text="beenden", command=beende).pack()
    root.mainloop()

if __name__ == '__main__':
    main()