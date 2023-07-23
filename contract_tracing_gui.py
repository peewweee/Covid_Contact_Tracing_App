import tkinter

# Next frame
def show_next_page():
    frame.pack_forget()
    frame_2.pack()

window = tkinter.Tk()
window.title("Trace Me")
window.geometry("840x440")
window.configure(bg="#934AB3")

frame = tkinter.Frame(bg="#934AB3")
frame_2 = tkinter.Frame(bg="#934AB3")

# frame 1 widgets
label_name = tkinter.Label(frame, text="Trace Me", bg="#934AB3", fg="#F7E7FB", font=("Arial", 18))
start_button = tkinter.Button(frame, text="Start", bg="#F5AE52", fg="#F76301", font=("Arial",16), command=show_next_page)
label_message = tkinter.Label(frame, text="Tara na sa ligtas na gala!", bg="#934AB3", fg="#E0C2F2", font=("Arial", 13))

label_name.grid(row=0, column=0, pady=30)
start_button.grid(row=1, column=0, pady=10)
label_message.grid(row=2, column=0)

frame.pack()

# frame 2 widgets
label_frame_2 = tkinter.Label(frame_2, text="try lang next page", bg="#934AB3", fg="#FFB6C1", font=("Arial", 18))
label_frame_2.pack(pady=30)

window.mainloop()