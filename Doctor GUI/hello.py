import requests,json
doctor_id = "#ORDR1004"
ptid="#OR59038"
# url = 'http://127.0.0.1:8000/doctor/api/booking/'+doctor_id[1:]
url = 'http://127.0.0.1:8000/doctor/api/patient/'+ptid[1:]
response_API = requests.get(url)
data = response_API.text
parse_json = json.loads(data)
appointments =  parse_json
print(appointments)

