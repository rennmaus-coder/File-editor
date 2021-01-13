def main():
    # christian@palm-family.de
    from PIL import Image
    import os, tkinter
    from tkinter import filedialog, messagebox, ttk
    root = tkinter.Tk()

    listboxfile = tkinter.Listbox(root, selectmode='browse')
    listboxfile.place(x=100, y=250, width=250, height=100)

    def new_img():
        input = tkinter.filedialog.askopenfilenames(parent=root, title="Dateien auswählen", filetypes=[("PNG", ".png"), ("tiff", ".tiff"), ("GIF", ".gif")])
        listboxfile.delete('0', 'end')
        for file in root.tk.splitlist(input):
            listboxfile.insert('end', file)
        return input

    def add_img():
        input = tkinter.filedialog.askopenfilenames(parent=root, title="Dateien auswählen", filetypes=[("PNG", ".png"), ("tiff", ".tiff"), ("GIF", ".gif")])
        for file in root.tk.splitlist(input):
            listboxfile.insert('end', file)
    root.geometry("350x350")
    Options=['.png', '.tiff', '.pdf', '.gif', '.TIF']
    variable = tkinter.StringVar(root)
    variable.set(Options[0])
    opt = tkinter.OptionMenu(root, variable, *Options)
    opt.config(width=90, font=('Helvetica', 12))
    opt.pack()

    def conv():
        messagebox.showwarning(title='Wichtig!', message='Dateien gleicher Endung werden überschrieben!!')
        input = listboxfile.get('0', 'end')
        for file in root.tk.splitlist(input):
            im = Image.open(file)
            f, e=os.path.splitext(file)
            output = f + variable.get()

            if e == '.tiff' or e == '.png' or e == '.TIF':
                im.save(f+'.gif')
                im=Image.open(f+'.gif')
                listboxfile.delete('0', '1')

            else:
                pass

            im.save(output)
        listboxfile.delete('0', 'end')
        messagebox.showinfo(title="Konvertierung erfolgreich", message="Konvertierung erfolgreich!")
    but=tkinter.Button(root, text="select new files", command=new_img)
    but.place(y=300)
    but.pack()
    tkinter.Button(root, text="select more files", command=add_img).pack()
    tkinter.Button(root, text="convert", command=conv).pack()

    def beende():
        root.destroy()
    tkinter.Button(root, text="beenden", command=beende).pack()
    root.mainloop()

if __name__ == '__main__':
    main()