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
    age_label.grid(row=2, column=0, padx=5, pady=5)
    entry_age = tkinter.Spinbox(personal_info, from_=0, to=150, font=("Arial", 12), width=29)
    entry_age.grid(row=2, column=1, pady=5)

    # Phone Number
    phone_num = tkinter.Label(personal_info, text="Phone Number:", bg="#3F1651", fg="#E6A1D7", font=("Arial", 12))
    phone_num.grid(row=1, column=2, padx=10, pady=10)
    num_entry = tkinter.Entry(personal_info, bg="white", fg="black", font=("Arial", 12), width=30)
    num_entry.grid(row=1, column=3, pady=10)

    # Vaccine and Test
    vaccine_test = tkinter.LabelFrame(frame_2, text="Part II. COVID-19 Vaccination and Test", bg="#3F1651", fg="#F2C75B", font=("Arial", 12, "bold"))
    vaccine_test.pack(pady=5, padx=20, fill=tkinter.BOTH, expand=True)

    # Vaccine
    label_vaccine = tkinter.Label(vaccine_test, text="COVID-19 Vaccination:", bg="#3F1651", fg="#E6A1D7", font=("Arial", 12))
    label_vaccine.grid(row=0, column=0, padx=10, pady=5)
    vaccine_options = ttk.Combobox(vaccine_test, values=["None", "First Dose", "Second Dose", "First Booster Shot", "Second Booster Shot"])
    vaccine_options.grid(row=0, column=1, pady=5)

    # Test
    label_test = tkinter.Label(vaccine_test, text="COVID-19 Test in the last 14 days:", bg="#3F1651", fg="#E6A1D7", font=("Arial", 12))
    label_test.grid(row=0, column=2, padx=10, pady=5)
    test_options = ttk.Combobox(vaccine_test, values=["Not been tested", "Tested (Positive)", "Tested (Negative)", "Tested (Pending Results)"])
    test_options.grid(row=0, column=3, pady=5)

    # Symptoms and Exposure
    symptoms_expo = tkinter.LabelFrame(frame_2, text="Part III. Symptoms and Exposure", bg="#3F1651", fg="#F2C75B", font=("Arial", 12, "bold"))
    symptoms_expo.pack(pady=10, padx=20, fill=tkinter.BOTH, expand=True)

    # Exposure
    label_exposure = tkinter.Label(symptoms_expo, text="Exposure in the last 14 days (Check all that apply):", bg="#3F1651", fg="#E6A1D7", font=("Arial", 11))
    label_exposure.grid(row=0, column=0, padx=10, pady=5)
    exposure_options = ["Exposure to cluster of individuals with flu-like illness", "Exposure to confirm case of COVID-19", "Exposure to suspect case for COVID-19", "None"]
    var_exposure = []

    for idx, option in enumerate(exposure_options):
        var_exposure.append(tkinter.IntVar())
        check_button = tkinter.Checkbutton(symptoms_expo, text=option, variable=var_exposure[idx], bg="#3F1651", fg="#E6A1D7", font=("Arial", 10))
        check_button.grid(row=idx + 1, column=0, padx=10, sticky="w")

    # Symptoms
    label_symptoms = tkinter.Label(symptoms_expo, text="Symptoms experienced in the past 7 days (Check all that apply):", bg="#3F1651", fg="#E6A1D7", font=("Arial", 11))
    label_symptoms.grid(row=0, column=1, columnspan=3, padx=10, pady=5, sticky="n")
    symptoms_options = ["Fever", "Cough", "Colds", "Muscle/body pains", "Sore throat", "Diarrhea", "Headache", "Shortness of breath", "Difficulty of breathing", "Loss of taste", "Loss of smell", "None of the above"]
    var_symptoms = []

    for idx, option in enumerate(symptoms_options[:4]):
        var_symptoms.append(tkinter.IntVar())
        check_button = tkinter.Checkbutton(symptoms_expo, text=option, variable=var_symptoms[idx], bg="#3F1651", fg="#E6A1D7", font=("Arial", 10))
        check_button.grid(row=idx + 1, column=1, padx=10, sticky="w")

    for idx, option in enumerate(symptoms_options[4:8]):
        var_symptoms.append(tkinter.IntVar())
        check_button = tkinter.Checkbutton(symptoms_expo, text=option, variable=var_symptoms[idx + 4], bg="#3F1651", fg="#E6A1D7", font=("Arial", 10))
        check_button.grid(row=idx + 1, column=2, padx=10, sticky="w")

    for idx, option in enumerate(symptoms_options[8:]):
        var_symptoms.append(tkinter.IntVar())
        check_button = tkinter.Checkbutton(symptoms_expo, text=option, variable=var_symptoms[idx + 8], bg="#3F1651", fg="#E6A1D7", font=("Arial", 10))
        check_button.grid(row=idx + 1, column=3, padx=10, sticky="w")

    # save information
    def save_info():
        save_name = entry_name.get()
        save_age = int(entry_age.get())
        save_num = num_entry.get()
        save_vaccine = vaccine_options.get()
        save_test = test_options.get()
        save_exposure = [exposure_options[i] for i, var in enumerate(var_exposure) if var.get() == 1]
        save_symptoms = [symptoms_options[i] for i, var in enumerate(var_symptoms) if var.get() == 1]

        # error window for phone number
        if not save_num.isdigit():
            messagebox.showerror("Error", "Please enter a valid phone number (numeric value).")
            return

        with open("info_contract_tracing.txt", "a") as file:
            file.write(f"Name: {save_name}\n")
            file.write(f"Age: {save_age}\n")
            file.write(f"Phone Number: {save_num}\n")
            file.write(f"Vaccination: {save_vaccine}\n")
            file.write(f"COVID-19 Test: {save_test}\n")
            file.write("Symptoms:\n")
            for symptom in save_symptoms:
                file.write(f"- {symptom}\n")
            file.write(f"COVID-19 Exposure:\n")
            for exposure in save_exposure:
                file.write(f"- {exposure}\n")

    save_button = tkinter.Button(frame_2, text="Submit", bg="#F5AE52", fg="#F76301", font=("Arial", 12), command=save_info)
    save_button.pack(pady=10)


    return frame_2
