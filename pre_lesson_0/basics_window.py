import tkinter
root=tkinter.Tk()
root.title('Window basics!')
root.iconbitmap('thinking.ico')
root.geometry('250x700')
root.resizable(0,0)
root.config(bg=  '#999999')

#making second window
top=tkinter.Toplevel()
top.title('Second window')
top.config(bg='#003366')
top.geometry('200x200+500+50')
# run root's window main loop (forever cycle, until close (X) is clicked)
root.mainloop()