import pyrebase
from datetime import datetime
# dd/mm/YY
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

config = {
  "apiKey": "AIzaSyAUW5isJoxjlgWxwOpEaQr4oWiPNwydG04",
  "authDomain": "openhack-fac81.firebaseapp.com",
  "databaseURL": "https://openhack-fac81.firebaseio.com",
  "storageBucket": "openhack-fac81",
}



firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


db = firebase.database()


data = {"date":dt_string, "hight":"50","rain":"100","flow":"50"}
db.child("chalakudi").child("meloor").push(data)


# user = db.child("chalakudi").order_by_child("").get()
# print(user.val())

