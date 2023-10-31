import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            expression = screen.get().replace("^", "**")
            result = str(eval(expression))
            screen.set(result)
        except Exception as e:
            screen.set("Hata")
    elif text == "C":
        screen.set("")
    else:
        current_text = screen.get()
        current_text += text
        screen.set(current_text)

root = tk.Tk()
root.title("Hesap Makinesi")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, bd=10, insertwidth=4, width=30, justify='right')
entry.grid(row=0, column=0, columnspan=4)

button_texts = [
    '+', '-', '*', '/',
    '1', '2', '3', '%',
    '4', '5', '6', '^',
    '7', '8', '9', '',
    '', '0', '=', 'C'
]

satır = 1
sutun = 0

for button_text in button_texts:
    if button_text:
        button = tk.Button(root, text=button_text, padx=20, pady=20, bd=8)
        button.grid(row=satır, column=sutun)
        button.bind("<Button-1>", on_click)
    sutun += 1
    if sutun > 3:
        sutun = 0
        satır += 1

root.mainloop()
