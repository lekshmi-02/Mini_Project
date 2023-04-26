import tkinter as tk
from tkinter import StringVar,ttk
import json

TOKEN_NO = 0
# Create main window
root = tk.Tk()
root.title("Doctor Page")
appointment_data = [{"doctor_id": "D001", "appointments": [
    {"token_no":"1","patient_id": "1001", "age": 45, "gender": "Male", "date": "2023-04-26", "time": "09:30 AM", "session": "Morning"},
    {"token_no":"2","patient_id": "1002", "age": 34, "gender": "Female", "date": "2023-04-27", "time": "02:00 PM",
     "session": "Evening"}]
                     },
                    {
                        "doctor_id": "D002",
                        "appointments": [
                            {
                                "token_no":"1",
                                "patient_id": "P002",
                                "age": 29,
                                "gender": "Female",
                                "date": "2023-04-26",
                                "time": "10:45 AM",
                                "session": "Morning"
                            },
                            {
                                "token_no":"2",
                                "patient_id": "P005",
                                "age": 55,
                                "gender": "Male",
                                "date": "2023-04-27",
                                "time": "11:30 AM",
                                "session": "Morning"
                            }
                        ]
                    },
                    {
                        "doctor_id": "D003",
                        "appointments": [
                            {
                                "token_no":"1",
                                "patient_id": "P003",
                                "age": 62,
                                "gender": "Male",
                                "date": "2023-04-26",
                                "time": "02:15 PM",
                                "session": "Evening"
                            },
                            {
                                "token_no":"2",
                                "patient_id": "P006",
                                "age": 46,
                                "gender": "Female",
                                "date": "2023-04-27",
                                "time": "04:00 PM",
                                "session": "Evening"
                            }
                        ]
                    }
                    ]


def get_patient_history(patient_id):
    with open('Doctor GUI/patient_history.json') as f:
        data = json.load(f)

    appointments = []
    for appointment in data:
        if appointment["patient_id"] == patient_id:
            appointments.append(appointment)

    return appointments

def add_appointment_data(patient_id):
    # Get the appointment data for the specified patient ID
    patient_history_data_window = tk.Toplevel(root)
    patient_history_data_window.title("Patient History")
    appointments = get_patient_history(patient_id)

    # Create the table columns
    columns = ["Doctor ID", "Date", "Time", "Gender", "Symptoms", "Prescriptions", "Remedies"]

    # Create the table
    table = ttk.Treeview(patient_history_data_window, columns=columns, show="headings")
    for col in columns:
        table.heading(col, text=col)

    # Populate the table with the appointment data
    for appointment in appointments:
        values = (appointment["doctor_id"], appointment["date"], appointment["time"], appointment["gender"], ", ".join(appointment["symptoms"]), ", ".join(appointment["prescriptions"]), ", ".join(appointment["remedies"]))
        table.insert("", "end", values=values)

    # Display the table
    table.grid(row=3,column=0)
# Function to show appointments when button is clicked
def show_appointments():
#     # Get doctor id from entry field
    doctor_id = doctor_id_entry.get()
    for data in appointment_data:
        if data["doctor_id"]==doctor_id_entry.get():
            no_of_appointments = len(data["appointments"])
    appointment_label = tk.Label(text="No of Appointments")
    appointment_label.grid(row=1,column=0)
    appointment_label_value = tk.Label(text=f"{no_of_appointments}")
    appointment_label_value.grid(row=1,column=1)
    # # Calculate number of appointments for morning and evening sessions
    # morning_appointments = 0
    # evening_appointments = 0

    # TODO: Implement code to calculate number of appointments for the day

    # # You can replace the above two lines with your own code
    # for key in appointment_data:
    #     if key["doctor_id"] == doctor_id:
    #         morning_appointments = 4
    #         evening_appointments = 4
    # # Show number of appointments for morning and evening sessions
    # morning_appointments_label.configure(text="Morning Appointments: " + str(morning_appointments))
    # evening_appointments_label.configure(text="Evening Appointments: " + str(evening_appointments))

    # patient_history_table = ttk.Treeview(root, columns=("doctor_id", "department", "date", "time", "symptoms", "remedies", "medicines"))
    # patient_history_button.grid(row=12,column=0)
    # patient_history_table.grid(row=13,column=0,columnspan=2,sticky='nsew')
    # patient_history_table.heading("doctor_id", text="Doctor ID",)
    # patient_history_table.heading("department", text="Department")
    # patient_history_table.heading("date", text="Date")
    # patient_history_table.heading("time", text="Time")
    # patient_history_table.heading("symptoms", text="Symptoms")
    # patient_history_table.heading("remedies", text="Remedies")
    # patient_history_table.heading("medicines", text="Medicines")



def show_patient_history():
    patient_history_window = tk.Toplevel(root)
    patient_history_window.title("Patient History")
    patient_id_label = tk.Label(patient_history_window, text="Patient ID")
    patient_id_label.grid(row=0,column=0)
    patient_id_entry = tk.Entry(patient_history_window)
    patient_id_entry.grid(row=0,column=1)

    add_data_button = tk.Button(patient_history_window, text="View Patient History", command=lambda: add_appointment_data(patient_id_entry.get()))
    add_data_button.grid(row=1,column=1)        

    


def add_checkup_summary():
    checkup_summary_window = tk.Toplevel(root)
    checkup_summary_window.title("Checkup Summary")
    patient_id_label = tk.Label(checkup_summary_window, text="Patient ID")
    patient_id_label.grid(row=0,column=0)
    patient_id_entry = tk.Entry(checkup_summary_window,justify="left")
    patient_id_entry.grid(row=1,column=0)
    date_label = tk.Label(checkup_summary_window, text="Date")
    date_label.grid(row=2,column=0)
    date_entry = tk.Entry(checkup_summary_window,)
    date_entry.grid(row=3,column=0)
    symptoms_label = tk.Label(checkup_summary_window, text="Symptoms")
    symptoms_label.grid(row=4,column=0)
    symptom_entry = tk.Text(checkup_summary_window,height=4)
    symptom_entry.grid(row=5,column=0)
    remedy_label = tk.Label(checkup_summary_window, text="Remedies")
    remedy_label.grid(row=6,column=0)
    remedy_entry = tk.Text(checkup_summary_window,height=4)
    remedy_entry.grid(row=7,column=0)
    prescription_label = tk.Label(checkup_summary_window, text="Prescriptions")
    prescription_label.grid(row=8,column=0)
    prescription_entry= tk.Text(checkup_summary_window,height=5)
    prescription_entry.grid(row=9,column=0)


    
    # for key in appointment_data:
    #     if key["doctor_id"] == doctor_id_entry.get():
    #         for data in key["appointments"]:
    #             if data["token_no"]==str(TOKEN_NO+1):
    #                 patient_id_value.config(text=data["patient_id"])
    #                 patient_age_value.config(text=data["age"])
    #                 patient_gender = StringVar(value=data["gender"])
    #                 patient_gender_value.config(text=patient_gender.get())
def show_patient_data():
    global TOKEN_NO
    token_no_label = tk.Label(root, text="Token Id")
    token_no_label.grid(row=5,column=0)
    token_value_label = tk.Label(root, text=TOKEN_NO + 1)
    token_value_label.grid(row=5,column=1)
    patient_id_label = tk.Label(root, text="Patient Id")
    patient_id_label.grid(row=6,column=0)
    patient_id_value = tk.Label(root, text=" ")
    patient_id_value.grid(row=6,column=1)
    patient_age_label = tk.Label(root, text="Patient Age")
    patient_age_label.grid(row=7,column=0)
    patient_age_value = tk.Label(root, text=" ")
    patient_age_value.grid(row=7,column=1)
    patient_gender_label = tk.Label(root, text="Patient Gender")
    patient_gender_label.grid(row=8,column=0)
    patient_gender_value = tk.Label(root, text="")
    patient_gender_value.grid(row=8,column=1)

    for key in appointment_data:
        if key["doctor_id"] == doctor_id_entry.get():
            for data in key["appointments"]:
                if data["token_no"]==str(TOKEN_NO+1):
                    patient_id_value.config(text=data["patient_id"])
                    patient_age_value.config(text=data["age"])
                    patient_gender = StringVar(value=data["gender"])
                    patient_gender_value.config(text=patient_gender.get())

    patient_history_btn = tk.Button(text="VIEW PATIENT HISTORY",command=show_patient_history)
    patient_history_btn.grid(row = 10, column=0)
    checkup_summary_btn = tk.Button(text="ADD CHECKUP SUMMARY",command=add_checkup_summary)
    checkup_summary_btn.grid(row = 10, column=1)
    

                




def start_consultation():
    global TOKEN_NO

    global start_button

    show_patient_data()
    TOKEN_NO+=1
    start_button.config(text="NEXT")


    



# Create entry field and show appointment button
doctor_id_label = tk.Label(root, text="Doctor ID:")
doctor_id_label.grid(row=0,column=0)

doctor_id_entry = tk.Entry(root)
doctor_id_entry.grid(row=0,column=1)

show_appointment_button = tk.Button(root, text="Show Appointments", command=show_appointments)
show_appointment_button.grid(row=1,column=0)

# # Create labels to display number of appointments for morning and evening sessions
# morning_appointments_label = tk.Label(root, text="Morning Appointments:")
# morning_appointments_label.grid(row=2,column=0)

# evening_appointments_label = tk.Label(root, text="Evening Appointments:")
# evening_appointments_label.grid(row=3,column=0)

start_button = tk.Button(root, text="START SESSION", command=start_consultation)
start_button.grid(row=4,column=0)
# Start the main loop

root.mainloop()
