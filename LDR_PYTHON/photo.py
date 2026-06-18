import serial
import matplotlib.pyplot as plt
import csv


ser = serial.Serial('COM3', 9600, timeout=1)  
photo_value = []
light_value = []
with open('data.csv',mode='w',newline='') as file:
    writer = csv.writer(file)#file is opened in write mode and a csv writer object is created
    writer.writerow(['Photoresistor Value', 'Light Value'])
    
    while True:
        while(ser.inWaiting() == 0):
         pass
        try:
         unioData = ser.readline().decode('utf-8').rstrip()
         photoData = int(unioData) # Convert the string data to an integer
         photo_value.append(photoData)  # Append the photoresistor value to the list
         val = (1./132.)*photoData  # Calculate the voltage value based on the photoresistor reading
    #volt max is 5v
         val = round(val, 1)  # Round the voltage value to 1 decimal places
         light_value.append(val)  # Append the light value to the list
         print(f"Light Value: {val}")
         writer.writerow([photoData, val])  # Write the data to the CSV file
         if len(photo_value) >= 20:  # Check if we have collected 20 readings then plot the graph
           break
      
        except ValueError:
         print("Invalid data received. Skipping this reading.")
        
# Plotting the photoresistor values and voltage values
plt.plot(photo_value, light_value, linestyle='-', marker='o', color='b')
plt.xlabel("Photoresistor Value")
plt.ylabel("Light Value (0–5)")
plt.title("Photoresistor vs Light")
plt.grid(True)
plt.show()


    
