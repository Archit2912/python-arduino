#include <Arduino.h>
#include <IRremote.hpp>
int irpin = 9;

int dl = 2000;
const uint32_t BUTTON_UP = 0xE718FF00;
const uint32_t BUTTON_DOWN = 0xAD52FF00;
const uint32_t BUTTON_LEFT = 0xF708FF00;
const uint32_t BUTTON_RIGHT = 0xA55AFF00;
const uint32_t BUTTON_OK = 0xE31CFF00;
const uint32_t BUTTON_4 = 0xBB44FF00;
const uint32_t BUTTON_5 = 0xBF40FF00;
const uint32_t BUTTON_6 = 0xBC43FF00;

// put function declarations here:


void setup() {
  Serial.begin(9600);
  IrReceiver.begin(irpin, ENABLE_LED_FEEDBACK); // Start the receiver
  Serial.println("IR Receiver is ready.");
  
}

void loop() {
 while(IrReceiver.decode()==0){// Wait until the receiver gets a value
   
}
  uint32_t value = IrReceiver.decodedIRData.decodedRawData;
  if(value == BUTTON_UP){
    Serial.println("UP");
  }
  else if(value == BUTTON_DOWN){
    Serial.println("DOWN");
  }
  else if(value == BUTTON_LEFT){
    Serial.println("LEFT");
  }
  else if(value == BUTTON_RIGHT){
    Serial.println("RIGHT");
  }
  else if(value == BUTTON_OK){
    Serial.println("OK");
  }
  else if(value == BUTTON_4){
    Serial.println("4");
  }
  else if(value == BUTTON_5){
    Serial.println("5");
  }
  else if(value == BUTTON_6){
    Serial.println("6");
  }
  else{
    Serial.print("Unknown button: ");
    Serial.println(value, HEX);
  }
  // decodedRawData stores the received HEX code
  IrReceiver.resume(); // Receive the next value
  delay(dl);

}

// put function definitions here:
