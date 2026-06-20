import time
import serial
import keyboard

ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino's serial port
time.sleep(2)
start = ser.readline().decode('utf-8').strip()
print(f"Arduino : {start}")
print("Press any key to start the program")
if keyboard.read_event():
    print("Program started...")
    time.sleep(1)
    print("Use the arrow keys(<-/->) to control the servo. Press 'e' to exit.")
    angle = 0 #intial angle is set to 0
    print("Setting initial angle to 0 degrees...")
    ser.write(f"{angle}\n".encode('utf-8'))
    print("Ready to recieve input...")
    time.sleep(0.1)
    while True:
      
      try: 
        if keyboard.is_pressed('left'):
            angle = max(0, angle - 25)  # Decrease angle by 25 degrees, minimum 0
            ser.write(f"{angle}\n".encode('utf-8'))
            response = ser.readline().decode('utf-8').strip()
            print(f"Arduino : {response}")
            time.sleep(0.2)
            
        elif keyboard.is_pressed('right'):
            angle = min(180, angle + 25)  # Increase angle by 25 degrees, maximum 180
            ser.write(f"{angle}\n".encode('utf-8'))
            response = ser.readline().decode('utf-8').strip()
            print(f"Arduino : {response}")
            time.sleep(0.2)
            
        elif keyboard.is_pressed('e'):
            print("Exiting program...")
            break
      except Exception as e:
        print(f"An error occurred: {e}")
        break
            
        