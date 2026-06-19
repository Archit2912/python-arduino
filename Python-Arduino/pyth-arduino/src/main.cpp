#include <Arduino.h>

// put function declarations here:
int LED = 13; //led pin number
int dl = 2000; //delay time in milliseconds
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(50);//wait for 50ms for the serial data to arrive then stop waiting
  pinMode(LED, OUTPUT);//led 13 is set to output
  Serial.println("Arduino is ready.");

  // put your setup code here, to run once:
  
}

void loop() {
  if (Serial.available() > 0) {//check if data is available to read
    String cmd = Serial.readStringUntil('\n');//read the data till \n 
    cmd.trim();//remove any unnecessary whitespace from the command
    if (cmd == "ON") {
      digitalWrite(LED, HIGH);
      Serial.println("OK:LED is ON");
      delay(dl);
    } else if (cmd == "OFF") {
      digitalWrite(LED, LOW);
      Serial.println("OK:LED is OFF");
      delay(dl); 
    } else {
      Serial.println("ERR:UNKNOWN CMD");
      delay(dl); 
    }
    
  }

}

// put function definitions here:
