import tkinter as tk

root=tk.Tk()
def show_prev():
    root.destroy()
    import page1

button = tk.Button(text="PREV",command=show_prev)
button.pack()

root.mainloop()