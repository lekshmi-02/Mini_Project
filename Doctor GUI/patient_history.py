from tkinter import *
from tkinter import ttk

appointments = [
    {
        "id": 5,
        "patientid": "#OR62593",
        "doctorid": "#ORDR1005",
        "doctorname": "Emily Chen",
        "department": "Orthopaedics",
        "date": "2023-05-27",
        "time": "22:48:00",
        "token": 1,
        "symptoms": "Hello",
        "prescription": "Hello",
        "remedies": "Hello"
    },
    {
        "id": 6,
        "patientid": "#OR62593",
        "doctorid": "#ORDR1006",
        "doctorname": "Dr Susan",
        "department": "Gynaecology",
        "date": "2023-05-27",
        "time": "22:48:00",
        "token": 2,
        "symptoms": "Headache",
        "prescription": "Paracetamol",
        "remedies": "Drink Water"
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
        "date": "2023-05-27",
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
class CheckupSummary:
    def __init__(self):
        self.checkup_summary_window = Tk()
        self.checkup_summary_window.title("Checkup Summary")
        self.patient_id_label_checkup = Label(text="Patient ID")
        self.patient_id_label_checkup.place(x=50,y=50)
        self.patient_id_value
        self.date_label = Label(text="Date")
        self.date_label.grid(row=2, column=0)
        self.date_entry = Entry( )
        self.date_entry.grid(row=3, column=0)
        self.symptoms_label = Label( text="Symptoms")
        self.symptoms_label.grid(row=4, column=0)
        self.symptom_entry = Text(height=4)
        self.symptom_entry.grid(row=5, column=0)
        self.remedy_label = Label( text="Remedies")
        self.remedy_label.grid(row=6, column=0)
        self.remedy_entry = Text( height=4)
        self.remedy_entry.grid(row=7, column=0)
        self.prescription_label = Label(text="Prescriptions")
        self.prescription_label.grid(row=8, column=0)
        self.prescription_entry = Text(height=5)
        self.prescription_entry.grid(row=9, column=0)
        self.checkup_summary_window.mainloop()

checkup = CheckupSummary()