import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://fir-2df8d-default-rtdb.firebaseio.com/'
})

x = db.reference('/x')
y = db.reference('/y')
x.set(0)
y.set(0)

def calculate_result(event):
    snapshot = db.reference('/').get()
    x = snapshot.get('x', 0)
    y = snapshot.get('y', 0)
    result = x + y
    ref = db.reference('/Sum')
    ref.set(result)

ref = db.reference('/')
ref.listen(calculate_result)
