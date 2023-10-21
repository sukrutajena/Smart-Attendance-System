
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://smartattendancesys-599de-default-rtdb.firebaseio.com/"
})

ref=db.reference('Students')

data={


    "2001109196":
        {
            "name":"RUCHIKA PATRA",
            "major":"CSE",
            "starting_year":2020,
            "total_attendance":0,
            "grade": "A",
            "year":4,
            "Pnone_number": 7978678976,
            "last_attendance_time":"2023-01-10 11:30:00"
        },
    "2001109204":
        {
            "name":"SHIBANI PATRO",
            "major":"CSE",
            "starting_year":2020,
            "total_attendance":0,
            "grade": "E",
            "year":4,
            "Pnone_number": 9668163523,
            "last_attendance_time":"2023-01-10 11:30:00"
        },
    "2001109211":
        {
            "name": "SUKRUTA JENA",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 7,
            "grade": "O",
            "year": 4,
            "Pnone_number": 9556360703,
            "last_attendance_time": "2023-01-10 12:30:00"
        },
    "2001109400":
        {
            "name": "SUCHISMITA SWAIN",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance":0,
            "grade": "A",
            "year": 4,
            "Pnone_number": 6370179396,
            "last_attendance_time": "2023-01-10 11:30:00"
        }
}

for key,value in data.items():
    ref.child(key).set(value)
