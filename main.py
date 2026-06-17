import serial
import time
ser = serial.Serial('COM3', 9600)
time.sleep(2) 
while True:
    while (ser.inWaiting() == 0):
        pass
    arduino_data = ser.readline()
    arduino_data = str(arduino_data, 'utf-8').strip('\r\n')   #UTF-8 is the default encoding format used to translate those strings into raw binary data
    print(arduino_data)
    

    
# Replace 'COM3' with your Arduino's port