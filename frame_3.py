import tkinter

def create_frame_3(parent_frame):
    frame_3 = tkinter.Frame(parent_frame, bg="#E6A1D7")

    # Label header
    info_data = tkinter.LabelFrame(frame_3, text="Search Information Entries", bg="#E6A1D7", fg="#3F1651", font=("Arial", 12, "bold"))
    info_data.pack(pady=20, padx=20, fill=tkinter.BOTH, expand=True)

    # Search
    search_label = tkinter.Label(info_data, text="Search:", bg="#E6A1D7", fg="#61346B", font=("Arial", 12))
    search_label.grid(row=0, column=0, padx=10, pady=10)
    search_entry = tkinter.Entry(info_data, bg="white", fg="black", font=("Arial", 12), width=30)
    search_entry.grid(row=0, column=1, pady=10)

    # search button
    search_button = tkinter.Button(info_data, text="\N{left-pointing magnifying glass}", bg="#E53F71", fg="#F2C75B", font=("Arial", 12))
    search_button.grid(row=0, column=2, padx=5, pady=10)

    return frame_3