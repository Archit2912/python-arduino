#include <Arduino.h>

// put function declarations here:
int x=1;
int y= 2;
int z =3;
int dl = 2000;

void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
  
}

void loop() {
  Serial.print(x);
  Serial.print(',');
  Serial.print(y);
  Serial.print(',');
  Serial.println(z);
  x = x+2;
  y = y+5;
  z = z+7;
  delay(dl);
  
  // put your main code here, to run repeatedly:
}

// put function definitions here:
