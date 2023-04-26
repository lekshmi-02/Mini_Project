import tkinter as tk
from tkinter import ttk
import json

def get_patient_history(patient_id):
    with open('patient_history.json') as f:
        data = json.load(f)

    appointments = []
    for appointment in data:
        if appointment["patient_id"] == patient_id:
            appointments.append(appointment)

    return appointments

def add_appointment_data(patient_id):
    # Get the appointment data for the specified patient ID
    appointments = get_patient_history(patient_id)

    # Create the table columns
    columns = ["Doctor ID", "Date", "Time", "Gender", "Symptoms", "Prescriptions", "Remedies"]

    # Create the table
    table = ttk.Treeview(root, columns=columns, show="headings")
    for col in columns:
        table.heading(col, text=col)

    # Populate the table with the appointment data
    for appointment in appointments:
        values = (appointment["doctor_id"], appointment["date"], appointment["time"], appointment["gender"], ", ".join(appointment["symptoms"]), ", ".join(appointment["prescriptions"]), ", ".join(appointment["remedies"]))
        table.insert("", "end", values=values)

    # Display the table
    table.pack(fill=tk.BOTH, expand=True)

def show_main_page():
    root.destroy()
    import main

# Create the Tkinter window
root = tk.Tk()

# Create the input fields and button
patient_id_label = tk.Label(root, text="Patient ID")
patient_id_label.pack()
patient_id_entry = tk.Entry(root)
patient_id_entry.pack()

add_data_button = tk.Button(root, text="View Patient History", command=lambda: add_appointment_data(patient_id_entry.get()))
add_data_button.pack()

button = tk.Button(text="GO BACK",command=show_main_page)
button.pack()

# Start the Tkinter event loop
root.mainloop()
