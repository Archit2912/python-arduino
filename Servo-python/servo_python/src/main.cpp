#include <Arduino.h>
#include <Servo.h>

Servo myservo;
int dl = 2000;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(50);
  myservo.attach(9);
  Serial.println("Servo Ready.");  // attaches the servo on pin 9 to the servo object
  // put your setup code here, to run once:
  
}

void loop() {
  if(Serial.available()>0){
    String pos = Serial.readStringUntil('\n');
    int position = pos.toInt();
    if(position >= 0 && position <= 180){  // ensure the position is within the valid range
      myservo.write(position);
      delay(dl);  // wait for the servo to reach the position
      Serial.print("Servo moved to position: ");
      Serial.println(position);
    }
    else{
      Serial.println("ERR:ANGLE OUT OF RANGE");
      delay(dl);  // wait for a moment before the next read
    }
  }
}



