# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
Initializes the sensor, gets and prints readings every two seconds.
"""
import time
import board
import adafruit_si7021
import datetime
import sqlite3
import firebase

# Create library object using our Bus I2C port
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_si7021.SI7021(i2c)

conn = sqlite3.connect("temp_data.sqlite")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS temp (date TEXT, time TEXT, temperature FLOAT, humidity FLOAT)")

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
    try:
        now = datetime.datetime.now()
        print (now.strftime("\n%c"))
        
        temperature, humidity = sensor.temperature, sensor.relative_humidity
        
        print("Temperature: %0.1f C" % temperature)
        print("Humidity: %0.1f %%" % humidity)
        
        data = {
            "Timestamp": now.strftime("%m-%d-%Y %H:%M:%S"),
            "Temperature": temperature,
            "Humidity": humidity
        }

        id = fsdb.collection('temperature').add(data)
        print(f"Added to collection temperature with id: {id}")
        
        c.execute(f"INSERT INTO temp Values (datetime('now'), datetime('now','localtime'), {temperature}, {humidity})")
        conn.commit()
        #x = c.execute("SELECT * FROM temp").fetchall()
        #print(x)
        time.sleep(15)
    except KeyboardInterrupt:
        print("Closing database connection")
        conn.close()
        break

#conn.close()
