import tkinter as tk

def set_messsge():
    text = text_input.get()
    title_label.configure(text=text)

window = tk.Tk()
window.title('Jugle Python')
window.minsize(width= 400, height= 400)

title_label = tk.Label(master=window, text='Hunter Milf')
title_label.pack()

text_input = tk.Entry(master=window)
text_input.pack()

btn = tk.Button(master=window, text='OL', command= set_messsge)
btn.pack()

window.mainloop()

