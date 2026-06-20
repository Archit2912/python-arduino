#include <Arduino.h>
#include <Servo.h>
Servo myservo;  // create servo object to control a servo

// put function declarations here:
int dl = 2000;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(50);//waits for 50ms for the input to arrive.
  myservo.attach(9);  
  Serial.println("Servo is ready");
  // put your setup code here, to run once:
  
}

void loop() {
  if(Serial.available()>0){
    String pos = Serial.readStringUntil('\n');
    int position = pos.toInt();
    if(position>=0 && position<=180){
    Serial.print("Servo moving to:");
    Serial.println(position);  
    myservo.write(position);
    
    delay(dl);
    
    
  }
  else{
    Serial.println("ERR:INVALID ANGLE");
  }
  }
  // put your main code here, to run repeatedly:
}

// put function definitions here:
