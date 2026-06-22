import time
import serial
ser = serial.Serial('COM3', 9600)  
time.sleep(2) 
start = ser.readline().decode('utf-8').rstrip()
print(f"Arduino: {start}")
while True:
    try:
      if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(f"Arduino: {line}")
        
    except KeyboardInterrupt:
        print("error....")
        break
    

