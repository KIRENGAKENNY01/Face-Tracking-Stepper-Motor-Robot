#include <Stepper.h>

// Stepper motor setup (28BYJ-48 + ULN2003)
const int stepsPerRevolution = 2048;  // ≈360°
const int in1Pin = 8;
const int in2Pin = 9;
const int in3Pin = 10;
const int in4Pin = 11;

// Create Stepper object
Stepper myStepper(stepsPerRevolution, in1Pin, in3Pin, in2Pin, in4Pin);

// Movement parameters
const int stepAmount = 50;   
const int motorSpeed = 10;   // RPM

void setup() {
  Serial.begin(9600);
  myStepper.setSpeed(motorSpeed);
  Serial.println("Stepper Face Tracker Ready.");
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim();

    if (command == "LEFT") {
      Serial.println("Moving LEFT...");
      myStepper.step(-stepAmount);
    }
    else if (command == "RIGHT") {
      Serial.println("Moving RIGHT...");
      myStepper.step(stepAmount);
    }
    else if (command == "CENTERED") {
      Serial.println("Centered. No movement.");
    }
    else {
      Serial.print("Unknown command: ");
      Serial.println(command);
    }
  }
}
