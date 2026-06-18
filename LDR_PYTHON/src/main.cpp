#include <Arduino.h>
int pin = A0;
int pval;

int dl = 2000;
void setup() {
  pinMode(pin, INPUT);
  Serial.begin(9600);
  // put your setup code here, to run once:
  
}

void loop() {
  pval = analogRead(pin);
  
  Serial.println(pval);
  
  delay(dl);
  // put your main code here, to run repeatedly:
}