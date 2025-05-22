# FrontEnd.py
import customtkinter as ctk

class HospitalUI(ctk.CTkFrame):
    def __init__(self, master, backend):
        super().__init__(master)
        self.backend = backend
        self.create_widgets()
        self.pack(padx=20, pady=20, fill="both", expand=True)


    def create_widgets(self):
        self.label_title = ctk.CTkLabel(self, text="🏥 Hospital Management System", font=("Arial", 24, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Name
        self.label_name = ctk.CTkLabel(self, text="Name:", anchor="w")
        self.label_name.grid(row=1, column=0, sticky="w", pady=5)
        self.entry_name = ctk.CTkEntry(self, width=300)
        self.entry_name.grid(row=1, column=1, pady=5, padx=10)

        # Age
        self.label_age = ctk.CTkLabel(self, text="Age:", anchor="w")
        self.label_age.grid(row=2, column=0, sticky="w", pady=5)
        self.entry_age = ctk.CTkEntry(self, width=300)
        self.entry_age.grid(row=2, column=1, pady=5, padx=10)

        # Gender
        self.label_gender = ctk.CTkLabel(self, text="Gender:", anchor="w")
        self.label_gender.grid(row=3, column=0, sticky="w", pady=5)
        self.entry_gender = ctk.CTkEntry(self, width=300)
        self.entry_gender.grid(row=3, column=1, pady=5, padx=10)

        # Diagnosis
        self.label_diag = ctk.CTkLabel(self, text="Diagnosis:", anchor="w")
        self.label_diag.grid(row=4, column=0, sticky="w", pady=5)
        self.entry_diag = ctk.CTkEntry(self, width=300)
        self.entry_diag.grid(row=4, column=1, pady=5, padx=10)

        # Buttons
        self.button_add = ctk.CTkButton(self, text="➕ Add Patient", command=self.add_patient, width=140)
        self.button_add.grid(row=5, column=0, pady=10, padx=5)

        self.button_update = ctk.CTkButton(self, text="🔄 Update", command=self.update_patient, width=140)
        self.button_update.grid(row=5, column=1, pady=10, padx=5)

        self.button_delete = ctk.CTkButton(self, text="❌ Delete", command=self.delete_patient, width=140)
        self.button_delete.grid(row=6, column=0, pady=10, padx=5)

        self.button_show = ctk.CTkButton(self, text="📋 Show All", command=self.show_patients, width=140)
        self.button_show.grid(row=6, column=1, pady=10, padx=5)

        # Text Box
        self.text_output = ctk.CTkTextbox(self, height=250, width=700)
        self.text_output.grid(row=7, column=0, columnspan=2, pady=(20, 0))

    def get_inputs(self):
        return (
            self.entry_name.get(),
            self.entry_age.get(),
            self.entry_gender.get(),
            self.entry_diag.get()
        )

    def add_patient(self):
        name, age, gender, diag = self.get_inputs()
        self.backend.add_patient(name, age, gender, diag)
        self.show_patients()

    def show_patients(self):
        records = self.backend.view_patients()
        self.text_output.delete("1.0", "end")
        for row in records:
            self.text_output.insert("end", f"{row}\n")

    def update_patient(self):
        try:
            id = int(self.entry_name.get())  # ID as name field temporarily
            name, age, gender, diag = self.get_inputs()
            self.backend.update_patient(id, name, age, gender, diag)
            self.show_patients()
        except:
            self.text_output.insert("end", "⚠️ Enter valid ID in Name field to update.\n")

    def delete_patient(self):
        try:
            id = int(self.entry_name.get())
            self.backend.delete_patient(id)
            self.show_patients()
        except:
            self.text_output.insert("end", "⚠️ Enter valid ID in Name field to delete.\n")
