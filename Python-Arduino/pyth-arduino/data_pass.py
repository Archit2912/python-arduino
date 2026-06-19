import serial
import time
print("Python -> Arduino Communication")
print("Type EXIT to quit.\n")  
ser = serial.Serial('COM3', 9600)
time.sleep(2)# Wait for the serial connection to initialize
startup_message = ser.readline().decode('utf-8').strip()# Read the startup message from Arduino and decode it
print(f"Arduino: {startup_message}")
while True:
    try:
     data = input("Enter data to send to Arduino: ")
     if data.upper() == "EXIT":
        print("Exiting...")
        break
     ser.write((data + "\n").encode())  # Send data to Arduino and encode it to bytes
     print(f"Python: {data}")
     response = ser.readline().decode('utf-8').strip()# Read response from Arduino and decode it
     if response:
      print(f"Arduino: {response}")
     else:
      print("No response from Arduino.")
    except Exception as e:
     print(f"An error occurred: {e}")
     break
ser.close()  # Close the serial connection when done
print("Serial connection closed.")
    