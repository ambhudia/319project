#include <Servo.h>

// The servo library takes care of generating pulses, and its source code is found at
// https://github.com/energia/Energia/blob/master/libraries/Servo/Servo.h
// Note that the PWM range is not the same as that noted in the documentation
// This is to keep the servo operating in the regime where the behaviour is not
// significantly non-linear

Servo servo1;
Servo servo2;
Servo servo3;             

float a1; // angle at servo 1
float a2; // angle at servo 2

String data;

// dataRef: What is this input for?
// 'a' for a1
// 'b' for a2
// 'r' to riase pen
// 'l' to lower pen
String dataRef;  // if "a" angle 1, if "b" angle 2

// flag: Are we in the correct system state? (a -> a1, b -> a2)
// case 0 if "a" not yet received, or pen was just lowered/raised
// case 1 if "a" received and case was 0
// case 2 if "b" received and case was 1
int flag = 0; 


void raisePen(){ 
// It just so happened that when I set up my robot, the pen was vertical
// at 100 degrees and sufficiently raised as 30 degrees
  servo3.write(30);
  Serial.println("Pen raised");
  }

void lowerPen(){
  servo3.write(100);
  Serial.println("Pen lowered");
  }



void setup()
{

  servo1.attach(P2_0); // Register the ports of each servo
  servo2.attach(P2_2); // It just so happened that I switched the connections
  servo3.attach(P2_1); // when wring everything together (P2.1 <-> P2.2)
  servo1.write(180);   // This is the rest position
  servo2.write(180);   // 
  raisePen();          // start robot wiht pen raised
  Serial.begin(9600);  // begin allow serial I/o with 9600 baud rate
} 

void loop(){
  if (Serial.available() > 0) {
      // Only desire to do something if serial input received
      data = Serial.readStringUntil('\n'); // Define delimiter to read up until

      // dataref is the flag given to the microcontroller to let it know what
      // we want it to do:
      // "a": angle a1 input
      // "b": angle a2 input
      // "l": lower pen
      // "r": raise pen
      dataRef = data.substring(0,1);


      // set corresponding variables by case, and update flags
      if (dataRef == "a") {
          a1 = data.substring(1,data.length()).toFloat();
          flag = 1; // we have received a valid a1
      } else if(dataRef == "b") {
          if (flag==1) { // set this onbly if we got angle a1
            a2 = data.substring(1,data.length()).toFloat();
            flag = 2; // we have received both angles
          }
          else { // received garbage, go to next iteration
            flag = 0;  // reset flag
            Serial.println("a1 not recieved");
            }
      } else if(dataRef == "r") { 
          raisePen();
          flag = 0;
      } else if(dataRef == "l") {
          lowerPen();
          flag = 0;
      } else {
          Serial.println("Garbage recieved"); // received garbage, go to next iteration
      }
      if (flag==2) { // we got the correct inputs. Write angles to servos and reset flag
          servo1.write(a1);
          servo2.write(a2);
          flag = 0;
        }
    }
  }
