from tkinter import *
from tkinter import messagebox
from datetime import datetime
from tkinter import ttk


import requests
import json


global appointments

class DoctorLogin:
    def __init__(self):
        self.patient_id = None
        self.patient_id_value = None
        self.patient_id_label = None
        self.next_button = None
        self.table = None
        self.token_no_label = None
        self.start_button = None
        self.tab = None
        self.token_details_frame = None
        self.session_window = None
        self.details_frame = None
        self.appointment_label = None
        self.doctor_id = None
        self.appointment_button = None
        self.dep_name = None
        self.dep_name_label = None
        self.doctor_name = None
        self.doctor_name_label = None
        self.doctor_window = None
        self.token_no = 0
        self.window = Tk()
        self.window.title("Doctor Login")
        self.window.config(padx=20, pady=20)
        self.login_frame = Frame(self.window, height=100, width=100)
        self.login_frame.place(x=25, y=50)
        self.doctor_id_label = Label(self.login_frame, text="Enter Doctor Id: ")
        self.doctor_id_label.grid(row=0, column=0)
        self.doctor_id_entry = Entry(self.login_frame)
        self.doctor_id_entry.grid(row=0, column=1)
        self.enter_button = Button(self.login_frame, text="Enter", command=self.show_doctor_details)
        self.enter_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.appointments = 0
        self.today_date = datetime.now().strftime("%Y-%m-%d")
        self.window.geometry("300x200")
        self.window.resizable(False, False)
        self.window.mainloop()

    def show_doctor_details(self):
        self.doctor_id = self.doctor_id_entry.get()
        url = 'http://127.0.0.1:8000/doctor/api/'+self.doctor_id[1:]
        response_API = requests.get(url)
        data = response_API.text
        parse_json = json.loads(data)
        doctor_details = parse_json
           
        if self.doctor_id == doctor_details["doctorid"]:
            self.doctor_window = Toplevel(self.window)
            self.doctor_window.geometry("400x400")
            self.doctor_window.config(padx=20, pady=20)
            self.details_frame = LabelFrame(self.doctor_window, height=200, width=300, text="Doctor Details")
            self.details_frame.pack()
            self.doctor_window.title("Doctor Page")
            self.doctor_name_label = Label(self.details_frame, text="Doctor Name :", )
            self.doctor_name_label.place(x=65, y=30)
            self.doctor_name = Label(self.details_frame, text=doctor_details["doctorname"])
            self.doctor_name.place(x=145, y=30)
            self.dep_name_label = Label(self.details_frame, text="Department    :")
            self.dep_name_label.place(x=65, y=60)
            self.dep_name = Label(self.details_frame, text=doctor_details["department"])
            self.dep_name.place(x=145, y=60)
            self.appointment_button = Button(self.details_frame, text="Show the appointments",
                                                 command=self.show_appointments)
            self.appointment_button.place(x=80, y=100)
            self.doctor_window.resizable(False, False)
        else:
            messagebox.showerror(title="Invalid id", message="Enter a valid Doctor Id")

    def show_appointments(self):
        url = 'http://127.0.0.1:8000/doctor/api/booking/'+self.doctor_id[1:]
        response_API = requests.get(url)
        data = response_API.text
        parse_json = json.loads(data)
        global appointments 
        appointments =  parse_json
        for appointment in appointments:
            if appointment["doctorid"] == self.doctor_id and appointment["date"] == self.today_date:
                self.appointments += 1
        self.appointment_button.config(state="disabled")

        self.appointment_label = Label(self.doctor_window, text=f"No: of appointments: {self.appointments}")
        self.appointment_label.place(x=118, y=250)

        self.start_button = Button(self.doctor_window, text="START SESSION", bg="green", width=15,
                                   command=self.show_session_details)
        self.start_button.place(x=123, y=280)

    def show_session_details(self):
        global appointments
        self.token_no += 1
        self.appointments -= 1

        self.session_window = Toplevel(self.doctor_window)
        self.session_window.title("Appointments")
        self.session_window.geometry("750x600")
        self.session_window.resizable(False, False)
        self.tab = ttk.Notebook(self.session_window, height=400, width=700)
        self.tab.place(x=20, y=80)

        self.token_details_frame = LabelFrame(self.session_window, width=400, height=400, text="Patient Details")
        self.token_details_frame.place(x=140, y=200)
        self.appointment_label = Label(self.token_details_frame,
                                       text=f"No: of appointments remaining: {self.appointments}",font=(None, 11))
        self.appointment_label.place(x=50, y=150)
        self.token_no_label = Label(self.token_details_frame, text=f"Token Id : {self.token_no}", font=(None, 15),
                                    bg="gray")
        self.token_no_label.place(x=110, y=200)
        self.separator = ttk.Separator(self.token_details_frame,orient="vertical")
        self.separator.place(x=350,y=0,height=380)
        self.patient_id_label = Label(self.token_details_frame, text="Patient Id", font=("Times New Roman", 13))
        self.patient_id_label.place(x=400, y=120)
        self.patient_id_value = Label(self.token_details_frame, text=" ", font=(None, 13))
        self.patient_id_value.place(x=530, y=120)
        self.patient_name_label = Label(self.token_details_frame, text="Name", font=("Times New Roman", 13))
        self.patient_name_label.place(x=400, y=150)
        self.patient_name_value = Label(self.token_details_frame, text=" ", font=(None, 13))
        self.patient_name_value.place(x=530, y=150)
        self.patient_age_label = Label(self.token_details_frame, text="Age", font=("Times New Roman", 13))
        self.patient_age_label.place(x=400, y=180)
        self.patient_age_value = Label(self.token_details_frame, text=" ", font=(None, 13))
        self.patient_age_value.place(x=530, y=180)
        self.patient_gender_label = Label(self.token_details_frame, text="Gender", font=("Times New Roman", 13))
        self.patient_gender_label.place(x=400, y=210)
        self.patient_gender_value = Label(self.token_details_frame, text=" ", font=(None, 13))
        self.patient_gender_value.place(x=530, y=210)
        self.next_button = Button(self.token_details_frame, text="NEXT PATIENT", bg="green", width=15,
                                  command=self.next_session_details)
        self.next_button.place(x=110, y=100)
        self.in_button = Button(self.token_details_frame, text="IN", bg="green",width=10,command=self.disable_button)
        self.in_button.place(x=80, y=300)
        self.out_button = Button(self.token_details_frame, text="OUT", bg="green",width=10,command=self.enable_button)
        self.out_button.place(x=160, y=300)

        self.table = ttk.Treeview(self.session_window, columns=(
            "Id", "date", "time", "doctorname", "department", "symptoms", "prescription", "remedies"), show="headings")
        self.table.heading('Id', text="Id")
        self.table.heading('date', text="Date")
        self.table.heading('time', text="Time")
        self.table.heading('doctorname', text="Doctor Name")
        self.table.heading('department', text="Department")
        self.table.heading('symptoms', text="Symptoms")
        self.table.heading('prescription', text="Prescription")
        self.table.heading('remedies', text="Remedies")
        self.table.column('Id', width=60, anchor="center")
        self.table.column('date', width=80, anchor="center")
        self.table.column('time', width=80, anchor="center")
        self.table.column('doctorname', width=80)
        self.table.column('department', width=100)
        self.table.column('symptoms', width=100)
        self.table.column('prescription', width=100)
        self.table.column('remedies', width=100)
        self.table.place(x=40, y=80)
        self.checkup_summary_frame = LabelFrame(self.session_window, width=400, height=400, text="Add Checkup Summary")
        self.token_details_frame.place(x=140, y=200)
        self.patient_id_label_checkup = Label(self.checkup_summary_frame, text="Patient Id :", font=(None, 10))
        self.patient_id_label_checkup.place(x=50, y=50)
        self.patient_id_value_checkup = Label(self.checkup_summary_frame, text=" ", font=(None, 13))
        self.patient_id_value_checkup.place(x=150, y=50)
        # self.date_label = Label(self.checkup_summary_frame, text="Date:")
        # self.date_label.place(x=50, y=100)
        self.symptoms_label = Label(self.checkup_summary_frame, text="Symptoms")
        self.symptoms_label.place(x=50, y=80)
        self.symptom_entry = Text(self.checkup_summary_frame, height=5,width=50)
        self.symptom_entry.place(x=130, y=80)
        self.remedy_label = Label(self.checkup_summary_frame, text="Remedies")
        self.remedy_label.place(x=50,y=180)
        self.remedy_entry = Text( self.checkup_summary_frame,height=5,width=50)
        self.remedy_entry.place(x=130,y=180)
        self.prescription_label = Label(self.checkup_summary_frame,text="Prescriptions")
        self.prescription_label.place(x=50, y=280)
        self.prescription_entry = Text(self.checkup_summary_frame,height=5,width=50)
        self.prescription_entry.place(x=130, y=280)
        self.save_button = Button(self.checkup_summary_frame,text="SAVE",bg="green",width=15,command=self.save_checkup_summary)
        self.save_button.place(x=400, y=20)

        # self.patient_age_label = Label(self.token_details_frame, text="Patient Age")
        # self.patient_age_label.place(x=80,y=100)
        # self.patient_age_value = Label(self.token_details_frame, text=" ")
        # self.patient_age_value.place(x=180,y=100)
        # patient_gender_label = tk.Label(root, text="Patient Gender")
        # patient_gender_label.grid(row=8, column=0)
        # patient_gender_value = tk.Label(root, text="")
        # patient_gender_value.grid(row=8, column=1)

        for appointment in appointments:
            self.id = appointment["id"]
            if appointment["token"] == self.token_no:
                ptid = appointment["patientid"]
                url = 'http://127.0.0.1:8000/doctor/api/patient/'+ptid[1:]
                response_API = requests.get(url)
                data = response_API.text
                parse_json = json.loads(data)
                self.patient_id_value.config(text=f": {appointment['patientid']}",font=("Times New Roman", 13))
                self.patient_id_value_checkup.config(text=f": {appointment['patientid']}",font=("Times New Roman", 13))
                self.patient_id = appointment['patientid']
                self.patient_name_value.config(text=f": {parse_json['firstname']} {parse_json['lastname']}",font=("Times New Roman", 13))
                self.patient_age_value.config(text=f": {parse_json['age']}",font=("Times New Roman", 13))
                self.patient_gender_value.config(text=f": {parse_json['gender']}",font=("Times New Roman", 13))
        for data in appointments:
            if self.patient_id == data['patientid']:
                self.table.insert('', "end", values=[data["id"], data["date"], data["time"], data["doctorname"],
                                                     data["department"], data["symptoms"], data["prescription"],
                                                     data["remedies"]])

        self.tab.add(self.token_details_frame, text="Appointments")
        self.tab.add(self.table, text="Patient History")
        self.tab.add(self.checkup_summary_frame, text="Add checkup Summary")

    def enable_button(self):
        self.in_button.config(state=NORMAL)
        self.out_button.config(state=DISABLED)
        url =f"http://127.0.0.1:8000/doctor/api/doctor/{self.doctor_id}/out"
        requests.get(url)


    def disable_button(self):
        self.out_button.config(state=NORMAL)
        self.in_button.config(state=DISABLED)

    def next_session_details(self):

        global appointments
        self.token_no += 1
        self.appointments -= 1

        if self.appointments == -1:
            self.doctor_window.destroy()
        else:
            for appointment in appointments:
                self.id = appointment["id"]
                if appointment["token"] == self.token_no:
                    ptid = appointment["patientid"]
                    url = 'http://127.0.0.1:8000/doctor/api/patient/'+ptid[1:]
                    response_API = requests.get(url)
                    data = response_API.text
                    parse_json = json.loads(data)
                    self.appointment_label.config(text=f"No: of appointments remaining: {self.appointments}")
                    self.token_no_label.config(text=f"Token Id : {self.token_no}")
                    self.patient_id_value.config(text=f": {appointment['patientid']}")
                    self.patient_id_value_checkup.config(text=f": {appointment['patientid']}")
                    self.patient_id = appointment['patientid']
                    self.patient_name_value.config(text=f": {parse_json['firstname']} {parse_json['lastname']}",font=("Times New Roman", 13))
                    self.patient_age_value.config(text=f": {parse_json['age']}",font=("Times New Roman", 13))
                    self.patient_gender_value.config(text=f": {parse_json['gender']}",font=("Times New Roman", 13))
            for data in appointments:
                if self.patient_id == data['patientid']:
                    self.table.delete(*self.table.get_children())
                    self.table.insert('', "end", values=[data["id"], data["date"], data["time"], data["doctorname"],
                                                     data["department"], data["symptoms"], data["prescription"],
                                                         data["remedies"]])

    def save_checkup_summary(self):
        global appointments
        symptom_data = self.symptom_entry.get("1.0",END)
        remedy_data = self.remedy_entry.get("1.0",END)
        prescription_data = self.prescription_entry.get("1.0",END)
        
        url = "http://127.0.0.1:8000/doctor/api/checkup/"+str(self.id)

        payload = {"symptom":symptom_data,"prescription":prescription_data,"remedy":remedy_data}
        json_data = json.dumps(payload)
        headers = {"Content-Type": "application/json"}

        response = requests.post(url, data=json_data, headers=headers)

        if response.status_code == 200:
            print("Data posted successfully!")
        else:
            print("Error posting data:", response.text)