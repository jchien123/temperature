import firebase
import random
import datetime
import time

# Firebase configuration
config = {
    "apiKey": "AIzaSyDa3866etmdqDI9w9xaHb21MCMzO6c-Bpc",
    "authDomain": "temperature-monitor-68311.firebaseapp.com",
    "databaseURL": "https://temperature-monitor-68311-default-rtdb.firebaseio.com/",
    "projectId": "temperature-monitor-68311",
    "storageBucket": "temperature-monitor-68311.appspot.com",
    "messagingSenderId": "232322906124",
    "appId": "1:232322906124:web:953d336ac5b0e6912b1629"
}

# Instantiates a Firebase app
app = firebase.initialize_app(config)

fsdb = app.firestore()


while True: 
    now = datetime.datetime.now()
    data = {
        "timestamp": now.strftime("%m-%d-%Y %H:%M:%S"),
        "temperature": random.randrange(-10,40),
    }

    id = fsdb.collection('temperature').add(data)
    print(id)
    time.sleep(15)
