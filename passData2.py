import serial

ser = serial.Serial('COM3', 9600,timeout=1)
while True:
    while(ser.inWaiting() == 0):
        pass
    unioData = ser.readline().decode('utf-8').rstrip()
    #split the  string data into int/float values
    splitData = unioData.split(',')#this will return an array of strings
    x = float(splitData[0])#convert the first string to float
    y = float(splitData[1])#convert the second string to float
    z = float(splitData[2])#convert the third string to float
     
    print(f"x: {x}, y: {y}, z: {z}")
    
        