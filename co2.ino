#include <Servo.h>
#define MOTOR 10  
#define LED 12
Servo myservo;

void setup() {
  Serial.begin(9600);                         // set the baud rate
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(MOTOR,OUTPUT);
  pinMode(LED,OUTPUT);
  Serial.println("0");                      // print "Ready" once
  myservo.attach(9);
}
void loop() {
  char inByte = ' ';
  int co2=0;
  if(Serial.available())
  {                                         // only send data back if data has been sent
    char inByte = Serial.read();            // read the incoming data
    co2 = (int)inByte;
    Serial.println(inByte);
    while(1){
      if(co2<50)     
      {
        myservo.write(0);// wait for a second
        digitalWrite(LED_BUILTIN, LOW);
        analogWrite(MOTOR,0);
        digitalWrite(LED,LOW);
        delay(2000);
        break;
      } 
    
      if (co2>100)
      {
        myservo.write(90);
        digitalWrite(LED_BUILTIN, HIGH);
        analogWrite(MOTOR,100);
        digitalWrite(LED,HIGH);
        delay(2000);
        break;
      }
    }// send the data back in a new line so that it is not all one long line
  }
 
  delay(100);                                    // delay for 1/10 of a second
}
