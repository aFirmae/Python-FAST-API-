import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://fir-2df8d-default-rtdb.firebaseio.com/'
})

u_details = [
    {"Name": "John Doe", "DOB": "2nd March, 2025", "Age": -1},
    {"Name": "Felica Sanders", "DOB": "2nd December, 1256", "Age": 765},
    {"Name": "Katie Smith", "DOB": "3rd March, 1999", "Age": 21}
]

# print("Your details: ")
# name = input("Name: ")
# dob = input("DOB: ")
# age = int(input("Age: "))
# u_details.append({"Name": name, "DOB": dob, "Age": age})

# for i in range(len(u_details)):
#     first_name = u_details[i]["Name"].split()[0]
#     ref = db.reference(f'/{first_name}')
#     ref.set(u_details[i])

def remove_from_db(username):
    for i in range(len(u_details)):
        if u_details[i]["Name"].split()[0] == username:
            u_details.pop(i)
            break
    ref = db.reference(f'/{username}')
    ref.delete()
    
username = input("Enter the name of the user you want to remove: ")
remove_from_db(username)