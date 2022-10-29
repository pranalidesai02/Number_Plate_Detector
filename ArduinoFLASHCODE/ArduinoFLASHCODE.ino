const int ledPinG = 13;   // the pin that the Green LED is attached to
const int ledPinR = 12;   // the pin that the Red LED is attached to 
const int motorPin1 = 10; // the pin that the motor is attached to
const int motorPin2 = 11; // the pin that the motor is attached to
int incomingByte;         // a variable to read incoming serial data into

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPinG, OUTPUT);
  pinMode(ledPinR, OUTPUT);
  // initialize the motor pin
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
}

void loop() {
  //turn on the Red LED :
  digitalWrite(ledPinG, LOW);
  digitalWrite(ledPinR, HIGH);

  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();


    // if it's a capital T (ASCII 72), turn off the Red LED, turn on the Green LED, open the gate, wait for 10s and close the gate:
    if (incomingByte == 'T') {
      digitalWrite(ledPinG, HIGH);
      digitalWrite(ledPinR, LOW);

      digitalWrite(motorPin1, HIGH);
      digitalWrite(motorPin2, LOW);

      delay(2000);
      
      digitalWrite(motorPin1, LOW);
      digitalWrite(motorPin2, LOW);

      delay(10000);

      digitalWrite(motorPin1, LOW);
      digitalWrite(motorPin2, HIGH);

      delay(2000);

      digitalWrite(motorPin1, LOW);
      digitalWrite(motorPin2, LOW);

    }
  }
}