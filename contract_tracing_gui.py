import tkinter
import frame_2

# Next frame
def show_next_page():
    frame.pack_forget()
    frame_2.create_frame_2(window).pack(fill=tkinter.BOTH, expand=True)

window = tkinter.Tk()
window.title("Trace Me")
window.geometry("880x440")

app_bg = tkinter.PhotoImage(file="app_background.png")

bg_label = tkinter.Label(window, image=app_bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tkinter.Frame(bg="#653780")

# frame 1 widgets
start_button = tkinter.Button(frame, text="Start", bg="#F5AE52", fg="#F76301", font=("Arial", 16), command=show_next_page)
start_button.grid(row=3, column=2, pady=10)

frame.pack()

window.mainloop()