from tkinter import *
from tkinter import messagebox
from datetime import datetime

doctor_details = [{
    "doctorid": "#ORDR1005",
    "doctorname": "Dr. Emily Chen",
    "department": "Orthopedics"
}]
appointments = [
    {
        "id": 5,
        "patientid": "#OR62593",
        "doctorid": "#ORDR1005",
        "doctorname": "1",
        "department": "1",
        "date": "2023-05-20",
        "time": "22:48:00",
        "token": 1,
        "symptoms": "",
        "prescription": "",
        "remedies": ""
    },
    {
        "id": 6,
        "patientid": "#OR85418",
        "doctorid": "#ORDR1005",
        "doctorname": "1",
        "department": "1",
        "date": "2023-05-20",
        "time": "22:48:00",
        "token": 2,
        "symptoms": "",
        "prescription": "",
        "remedies": ""
    },
    {
        "id": 7,
        "patientid": "#OR46473",
        "doctorid": "#ORDR1005",
        "doctorname": "1",
        "department": "1",
        "date": "2023-05-05",
        "time": "22:48:00",
        "token": 3,
        "symptoms": "",
        "prescription": "",
        "remedies": ""
    },
    {
        "id": 8,
        "patientid": "#OR24872",
        "doctorid": "#ORDR1005",
        "doctorname": "1",
        "department": "1",
        "date": "2023-05-20",
        "time": "22:48:00",
        "token": 4,
        "symptoms": "",
        "prescription": "",
        "remedies": ""
    },
    {
        "id": 9,
        "patientid": "#OR57758",
        "doctorid": "#ORDR1005",
        "doctorname": "1",
        "department": "1",
        "date": "2023-05-04",
        "time": "22:48:00",
        "token": 5,
        "symptoms": "",
        "prescription": "",
        "remedies": ""
    },
    {
        "id": 10,
        "patientid": "#OR56853",
        "doctorid": "#ORDR1005",
        "doctorname": "1",
        "department": "1",
        "date": "2023-05-26",
        "time": "22:48:00",
        "token": 6,
        "symptoms": "",
        "prescription": "",
        "remedies": ""
    },
    {
        "id": 11,
        "patientid": "#OR22727",
        "doctorid": "#ORDR1005",
        "doctorname": "1",
        "department": "1",
        "date": "2023-05-26",
        "time": "22:48:00",
        "token": 7,
        "symptoms": "",
        "prescription": "",
        "remedies": ""
    },
    {
        "id": 12,
        "patientid": "#OR21800",
        "doctorid": "#ORDR1005",
        "doctorname": "1",
        "department": "1",
        "date": "2023-05-04",
        "time": "22:48:00",
        "token": 8,
        "symptoms": "",
        "prescription": "",
        "remedies": ""
    },
    {
        "id": 13,
        "patientid": "#OR23051",
        "doctorid": "#ORDR1005",
        "doctorname": "1",
        "department": "1",
        "date": "2023-05-04",
        "time": "22:48:00",
        "token": 9,
        "symptoms": "",
        "prescription": "",
        "remedies": ""
    },
    {
        "id": 14,
        "patientid": "#OR33823",
        "doctorid": "#ORDR1005",
        "doctorname": "1",
        "department": "1",
        "date": "2023-05-04",
        "time": "22:48:00",
        "token": 10,
        "symptoms": "",
        "prescription": "",
        "remedies": ""
    },
    {
        "id": 15,
        "patientid": "#OR54922",
        "doctorid": "#ORDR1005",
        "doctorname": "1",
        "department": "1",
        "date": "2023-05-04",
        "time": "22:48:00",
        "token": 11,
        "symptoms": "",
        "prescription": "",
        "remedies": ""
    },
    {
        "id": 16,
        "patientid": "#OR77255",
        "doctorid": "#ORDR1005",
        "doctorname": "1",
        "department": "1",
        "date": "2023-05-04",
        "time": "22:48:00",
        "token": 12,
        "symptoms": "",
        "prescription": "",
        "remedies": ""
    },
    {
        "id": 17,
        "patientid": "#OR99966",
        "doctorid": "#ORDR1005",
        "doctorname": "1",
        "department": "1",
        "date": "2023-05-04",
        "time": "22:48:00",
        "token": 13,
        "symptoms": "",
        "prescription": "",
        "remedies": ""
    }]


class DoctorLogin:
    def __init__(self):
        self.details_frame = None
        self.appointment_label = None
        self.doctor_id = None
        self.appointment_button = None
        self.dep_name = None
        self.dep_name_label = None
        self.doctor_name = None
        self.doctor_name_label = None
        self.doctor_window = None
        self.window = Tk()
        self.window.title("Doctor Login")
        self.window.config(padx=20, pady=20)
        self.login_frame = Frame(self.window,height=100,width=100)
        self.login_frame.place(x=25,y=50)
        self.doctor_id_label = Label(self.login_frame,text="Enter Doctor Id: ")
        self.doctor_id_label.grid(row=0, column=0)
        self.doctor_id_entry = Entry(self.login_frame)
        self.doctor_id_entry.grid(row=0, column=1)
        self.enter_button = Button(self.login_frame,text="Enter", command=self.show_doctor_details)
        self.enter_button.grid(row=1, column=0, columnspan=2,padx=10,pady=10)
        self.appointments = 0
        self.today_date = datetime.now().strftime("%Y-%m-%d")
        self.window.geometry("300x200")
        self.window.resizable(False,False)
        self.window.mainloop()

    def show_doctor_details(self):
        self.doctor_id = self.doctor_id_entry.get()
        for data in doctor_details:
            if self.doctor_id == data["doctorid"]:
                self.doctor_window = Toplevel(self.window)
                self.doctor_window.geometry("400x400")
                self.doctor_window.config(padx=20, pady=20)
                self.details_frame = LabelFrame(self.doctor_window,height=200,width=300,text="Doctor Details")
                self.details_frame.pack()
                self.doctor_window.title("Doctor Page")
                self.doctor_name_label = Label(self.details_frame, text="Doctor Name :",)
                self.doctor_name_label.place(x=65,y=30)
                self.doctor_name = Label(self.details_frame, text=data["doctorname"])
                self.doctor_name.place(x=145,y=30)
                self.dep_name_label = Label(self.details_frame, text="Department    :")
                self.dep_name_label.place(x=65,y=60)
                self.dep_name = Label(self.details_frame, text=data["department"])
                self.dep_name.place(x=145,y=60)
                self.appointment_button = Button(self.details_frame, text="Show the appointments",
                                                 command=self.show_appointments)
                self.appointment_button.place(x=80,y=100)
                self.doctor_window.resizable(False,False)
            else:
                messagebox.showerror(title="Invalid id", message="Enter a valid Doctor Id")

    def show_appointments(self):
        global appointments
        for appointment in appointments:
            if appointment["doctorid"] == self.doctor_id and appointment["date"] == self.today_date:
                self.appointments += 1

        self.appointment_label = Label(self.doctor_window, text=f"No: of appointments: {self.appointments}")
        self.appointment_label.place(x=118,y=250)

        self.start_button = Button(self.doctor_window, text="START SESSION", bg="green",width=15,command=self.show_session_details)
        self.start_button.place(x=123,y=280)

    def show_session_details(self):
        pass


