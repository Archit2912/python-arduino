#include <Arduino.h>

// put function declarations here:
int cnt = 1;
int dl = 2000;

void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
  
}

void loop() {
  Serial.print("Hello World! ");
  Serial.println(cnt);
  delay(dl);
  cnt++;
  // put your main code here, to run repeatedly:
}

// put function definitions here:
