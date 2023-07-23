import tkinter

# frame 2 widgets
def create_frame_2(parent_frame):
    frame_2 = tkinter.Frame(parent_frame, bg="#3F1651", width=parent_frame.winfo_width(), height=parent_frame.winfo_height())

    full_name_2 = tkinter.Label(frame_2, text="Full Name:", bg="#3F1651", fg="#E6A1D7", font=("Arial", 12))
    full_name_2.grid(row=0, column=0, pady=10)

    entry_name = tkinter.Entry(frame_2, bg="white", fg="black", font=("Arial", 12))
    entry_name.grid(row=0, column=1, pady=10)

    # save information
    def save_info():
        save_name = entry_name.get()

        with open("info_contract_tracing.txt", "a") as file:
            file.write(f"Name: {save_name}\n")

    save_button = tkinter.Button(frame_2, text="Save", bg="#F5AE52", fg="#F76301", font=("Arial", 12), command=save_info)
    save_button.grid(row=1, column=1, pady=10)

    return frame_2