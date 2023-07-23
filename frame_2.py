import tkinter as tk

def show_next_page():
    frame.pack_forget()
    frame_2.pack()

def create_frame_2(parent_frame):
    frame_2 = tk.Frame(parent_frame, bg="#934AB3")

    label_frame_2 = tk.Label(frame_2, text="try lang next page", bg="#934AB3", fg="#FFB6C1", font=("Arial", 18))
    label_frame_2.pack(pady=30)

    return frame_2