import serial


ser = serial.Serial('COM3', 9600, timeout=1)  
while True:
    while(ser.inWaiting() == 0):
        pass
    unioData = ser.readline().decode('utf-8').rstrip()
    photoData = int(unioData)  # Convert the string data to an integer
    print(f"Photoresistor Value: {photoData}")
    val = (1./132.)*photoData  # Calculate the voltage value based on the photoresistor reading
    #volt max is 5v
    val = round(val, 1)  # Round the voltage value to 1 decimal places
    print(f"Voltage Value: {val}")
    
