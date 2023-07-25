import tkinter as tk
import frame_2
import frame_3

# Next frame
def show_next_page():
    frame.pack_forget()
    frame_2.create_frame_2(window).pack(fill=tk.BOTH, expand=True)

# go to frame 3
def show_frame_3():
    frame.pack_forget()
    frame_3.create_frame_3(window).pack(fill=tk.BOTH, expand=True)

window = tk.Tk()
window.title("Trace Me")
window.geometry("880x440")

app_bg = tk.PhotoImage(file="app_background.png")

bg_label = tk.Label(window, image=app_bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(bg="#653780")

# Frame 1 widgets

start_button = tk.Button(frame, text="Start", bg="#1B7979", fg="#F2C75B", font=("Arial", 16, "bold"), width=10, command=show_next_page)
start_button.grid(row=0, column=0, padx=10, pady=45)

search_button = tk.Button(frame, text="Search", bg="#E53F71", fg="#3F1651", font=("Arial", 16, "bold"), width=10, command=show_frame_3)
search_button.grid(row=0, column=1, padx=10, pady=45)

frame.pack()

window.mainloop()
