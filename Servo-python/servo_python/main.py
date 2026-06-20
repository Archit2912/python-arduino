import time
import serial
print("Controlling servo with python")
ser = serial.Serial('COM3', 9600)  
time.sleep(2)  
print("Arduino is ready.")
start = ser.readline().decode('utf-8').strip()
print(f"Arduino : {start}")
print("Type 'exit' to quit.")
while True:
    angle = input("Enter servo angle (0-180): ")
    if angle.lower() == 'exit':
        print("Exiting...")
        break
    try:
        angle_int = int(angle)
        if 0 <= angle_int <= 180:
            ser.write(f"{angle_int}\n".encode())
            print(f"Sent angle: {angle_int}")
            response = ser.readline().decode('utf-8').strip()#RESPONSE IS MUST AS ARDUINO ALSO SENDS DATA
            print(f"Arduino: {response}")
        else:
            print("Please enter a valid angle between 0 and 180.")
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 180.")
