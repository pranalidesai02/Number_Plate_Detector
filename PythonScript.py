import serial
import time


# Define the serial port and baud rate.
# Ensure the 'COM#' corresponds to what was seen in the Windows Device Manager
ser = serial.Serial('COM3', 9600)

def license_plate_detected():
        time.sleep(2) # wait for the serial connection to initialize

        print("LED On and gate open")
        time.sleep(0.1) 
        ser.write(b'T') 
