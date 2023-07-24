import tkinter
import tkinter.messagebox as messagebox

# frame 2 widgets
def create_frame_2(parent_frame):
    frame_2 = tkinter.Frame(parent_frame, bg="#3F1651", width=parent_frame.winfo_width(), height=parent_frame.winfo_height())

    # Full Name
    full_name_2 = tkinter.Label(frame_2, text="Full Name:", bg="#3F1651", fg="#E6A1D7", font=("Arial", 12))
    full_name_2.grid(row=0, column=0, pady=10)
    entry_name = tkinter.Entry(frame_2, bg="white", fg="black", font=("Arial", 12))
    entry_name.grid(row=0, column=1, pady=10)

    # Age
    age_label = tkinter.Label(frame_2, text="Age:", bg="#3F1651", fg="#E6A1D7", font=("Arial", 12))
    age_label.grid(row=1, column=0, pady=10)
    entry_age = tkinter.Entry(frame_2, bg="white", fg="black", font=("Arial", 12))
    entry_age.grid(row=1, column=1, pady=10)

    # Phone Number
    phone_num = tkinter.Label(frame_2, text="Phone Number:", bg="#3F1651", fg="#E6A1D7", font=("Arial", 12))
    phone_num.grid(row=2, column=0, pady=10)
    num_entry = tkinter.Entry(frame_2, bg="white", fg="black", font=("Arial", 12))
    num_entry.grid(row=2, column=1, pady=10)

    # save information
    def save_info():
        save_name = entry_name.get()
        save_age = entry_age.get()
        save_num = num_entry.get()

        # error window for age and phone number
        if not save_age.isdigit():
            messagebox.showerror("Error", "Please enter a valid age (numeric value).")
            return
        if not save_num.isdigit():
            messagebox.showerror("Error", "Please enter a valid phone number (numeric value).")
            return

        with open("info_contract_tracing.txt", "a") as file:
            file.write(f"Name: {save_name}\n")
            file.write(f"Age: {save_age}\n")
            file.write(f"Phone Number: {save_num}\n")

    save_button = tkinter.Button(frame_2, text="Save", bg="#F5AE52", fg="#F76301", font=("Arial", 12), command=save_info)
    save_button.grid(row=3, column=1, pady=10)

    return frame_2