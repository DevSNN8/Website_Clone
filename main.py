import tkinter as tk 
def show_output():
    number = int(num_input.get())

    if number == 0:
        output_r.configure(text='Banana')
        return

    output = ''
    for i in range (1,15):
        output += str(number) + 'X' + str(i)
        output += '=' + str(number * i) + '\n'

    output_r.configure(text=output)

window = tk.Tk()
window.title('Content Python')
window.minsize(width=400, height = 400)

title_label = tk.Label(master=window, text='Brandi Love')
title_label.pack()

num_input = tk.Entry(master=window)
num_input.pack()


btn = tk.Button(
    master=window, text='Result',command=show_output
)
btn.pack()

output_r = tk.Label(master=window)
output_r.pack()

window.mainloop()