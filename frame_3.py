import tkinter

def create_frame_3(parent_frame):
    frame_3 = tkinter.Frame(parent_frame, bg="#3F1651")

    # Label header
    info_data = tkinter.LabelFrame(frame_3, text="Search Information Entries", bg="#3F1651", fg="#F2C75B", font=("Arial", 12, "bold"))
    info_data.pack(pady=20, padx=20, fill=tkinter.BOTH, expand=True)

    # Search
    search_label = tkinter.Label(info_data, text="Search:", bg="#3F1651", fg="#E6A1D7", font=("Arial", 12))
    search_label.grid(row=0, column=0, padx=10, pady=10)
    search_entry = tkinter.Entry(info_data, bg="white", fg="black", font=("Arial", 12), width=30)
    search_entry.grid(row=0, column=1, pady=10)

    return frame_3