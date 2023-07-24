import tkinter

def create_frame_3(parent_frame):
    frame_3 = tkinter.Frame(parent_frame, bg="#3F1651")

    # Label header
    info_data = tkinter.LabelFrame(frame_3, text="Search Information Entries", bg="#3F1651", fg="#F2C75B", font=("Arial", 12, "bold"))
    info_data.pack(pady=20, padx=20, fill=tkinter.BOTH, expand=True)

    return frame_3