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

start_button = tkinter.Button(frame, text="Start", bg="#1B7979", fg="#F2C75B", font=("Arial", 16, "bold"), width=10, command=show_next_page)
start_button.grid(row=0, column=0, padx=10, pady=45)

search_button = tkinter.Button(frame, text="Search", bg="#E53F71", fg="#3F1651", font=("Arial", 16, "bold"), width=10, command=save_info)
search_button.grid(row=0, column=1, padx=10, pady=45)

frame.pack()

window.mainloop()