import tkinter
import tkinter.messagebox as messagebox

def create_frame_3(parent_frame):
    frame_3 = tkinter.Frame(parent_frame, bg="#E6A1D7")

    def search_info():
        search_data = search_entry.get().lower()
        found_entries = []

        with open("info_contract_tracing.txt", "r") as file:
            lines = file.readlines()

        current_entry = ""
        for line in lines:
            if line.startswith("Name: "):
                current_entry = line[6:].strip()
            if search_data in line.lower():
                found_entries.append(current_entry + "\n" + line)

        if found_entries:
            result_text.config(state=tkinter.NORMAL)
            result_text.delete(1.0, tkinter.END)
            result_text.insert(tkinter.END, "\n\n".join(found_entries))
            result_text.config(state=tkinter.DISABLED)
        else:
            messagebox.showinfo("Search Results", "No matching entries found.")

    # Label header
    info_data = tkinter.LabelFrame(frame_3, text="Search Information Entries", bg="#E6A1D7", fg="#3F1651", font=("Arial", 12, "bold"))
    info_data.pack(pady=20, padx=20, fill=tkinter.BOTH, expand=True)

    # Search
    search_label = tkinter.Label(info_data, text="Search:", bg="#E6A1D7", fg="#61346B", font=("Arial", 12))
    search_label.grid(row=0, column=0, padx=10, pady=10)
    search_entry = tkinter.Entry(info_data, bg="white", fg="black", font=("Arial", 12), width=30)
    search_entry.grid(row=0, column=1, pady=10)

    # Search button
    search_button = tkinter.Button(info_data, text="\N{left-pointing magnifying glass}", bg="#E53F71", fg="#F2C75B", font=("Arial", 12), command=search_info)
    search_button.grid(row=0, column=2, padx=5, pady=10)

    # Text widget to display search results
    result_text = tkinter.Text(info_data, bg="white", fg="black", font=("Arial", 12), wrap=tkinter.WORD, state=tkinter.DISABLED)
    result_text.grid(row=1, column=0, columnspan=3, pady=10, padx=10, sticky="nsew")

    # Add a scrollbar to the text widget
    scrollbar = tkinter.Scrollbar(info_data, command=result_text.yview)
    scrollbar.grid(row=1, column=3, sticky="ns")
    result_text.config(yscrollcommand=scrollbar.set)

    return frame_3
