import tkinter
import tkinter.messagebox as messagebox
from tkinter import ttk

# frame 2 widgets
def create_frame_2(parent_frame):
    frame_2 = tkinter.Frame(parent_frame, bg="#3F1651")
    frame_2.pack(fill=tkinter.BOTH, expand=True)

    # Personal Information Label
    personal_info = tkinter.LabelFrame(frame_2, text="Part I. Personal Info", bg="#3F1651", fg="#F2C75B", font=("Arial", 12, "bold"))
    personal_info.pack(pady=20, padx=20, fill=tkinter.BOTH, expand=True)

    # Full Name
    full_name_2 = tkinter.Label(personal_info, text="Full Name:", bg="#3F1651", fg="#E6A1D7", font=("Arial", 12))
    full_name_2.grid(row=1, column=0, padx=10, pady=10)
    entry_name = tkinter.Entry(personal_info, bg="white", fg="black", font=("Arial", 12), width=30)
    entry_name.grid(row=1, column=1, pady=10)

    # Age
    age_label = tkinter.Label(personal_info, text="Age:", bg="#3F1651", fg="#E6A1D7", font=("Arial", 12))
    age_label.grid(row=2, column=0, padx=5, pady=0)
    entry_age = tkinter.Spinbox(personal_info, from_=0, to=150, font=("Arial", 12), width=29)
    entry_age.grid(row=2, column=1, pady=0)

    # Phone Number
    phone_num = tkinter.Label(personal_info, text="Phone Number:", bg="#3F1651", fg="#E6A1D7", font=("Arial", 12))
    phone_num.grid(row=1, column=2, padx=10, pady=10)
    num_entry = tkinter.Entry(personal_info, bg="white", fg="black", font=("Arial", 12), width=30)  # Set the width
    num_entry.grid(row=1, column=3, pady=10)

    # Vaccine and Test
    vaccine_test = tkinter.LabelFrame(frame_2, text="Part II. COVID-19 Vaccination and Test", bg="#3F1651", fg="#F2C75B", font=("Arial", 12, "bold"))
    vaccine_test.pack(pady=10, padx=20, fill=tkinter.BOTH, expand=True)

    # Vaccine
    label_vaccine = tkinter.Label(vaccine_test, text="COVID-19 Vaccination:", bg="#3F1651", fg="#E6A1D7", font=("Arial", 12))
    label_vaccine.grid(row=0, column=0, padx=10, pady=5)
    vaccine_options = ttk.Combobox(vaccine_test, values=["None", "First Dose", "Second Dose", "First Booster Shot", "Second Booster Shot"])
    vaccine_options.grid(row=0, column=1, pady=5)

    # Test
    label_test = tkinter.Label(vaccine_test, text="COVID-19 Test:", bg="#3F1651", fg="#E6A1D7", font=("Arial", 12))
    label_test.grid(row=0, column=2, padx=10, pady=5)
    test_options = ttk.Combobox(vaccine_test, values=["Not been tested", "Tested (Positive)", "Tested (Negative)", "Tested (Pending Results)"])
    test_options.grid(row=0, column=3, pady=5)

    # save information
    def save_info():
        save_name = entry_name.get()
        save_age = int(entry_age.get())  # Convert the age to an integer
        save_num = num_entry.get()
        save_vaccine = vaccine_options.get()

        # error window for phone number
        if not save_num.isdigit():
            messagebox.showerror("Error", "Please enter a valid phone number (numeric value).")
            return

        with open("info_contract_tracing.txt", "a") as file:
            file.write(f"Name: {save_name}\n")
            file.write(f"Age: {save_age}\n")
            file.write(f"Phone Number: {save_num}\n")
            file.write(f"Vaccination: {save_vaccine}\n")

    save_button = tkinter.Button(frame_2, text="Save", bg="#F5AE52", fg="#F76301", font=("Arial", 12), command=save_info)
    save_button.pack(pady=10)


    return frame_2
