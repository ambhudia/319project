#include <Servo.h>

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
  servo3.write(50);
  Serial.println("Pen raised");
  }
void lowerPen(){
  servo3.write(100);
  Serial.println("Pen lowered");
  }



void setup()
{

  servo1.attach(P2_0);
  servo2.attach(P2_2);
  servo3.attach(P2_1);
  servo1.write(180);
  servo2.write(180);
  raisePen();
  Serial.begin(9600);  
} 

void loop(){
  if (Serial.available() > 0) {
      // Only desire to do something if serial input received
      data = Serial.readStringUntil('\n'); // Define delimiter
      //data = data.replace("\n", "");  // Strip string of extraneous artifacts

      dataRef = data.substring(0,1);
      // set corresponding variables by case, and update flags
      if (dataRef == "a") {
          a1 = data.substring(1,data.length()).toFloat();
          flag = 1;
      } else if(dataRef == "b") {
          if (flag==1) {
            a2 = data.substring(1,data.length()).toFloat();
            flag = 2;
          }
          else { // received garbage, go to next iteration
            flag = 0;
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
