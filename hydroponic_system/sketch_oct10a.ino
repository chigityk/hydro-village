const int airPin = 22; //the pin for air pump
const int fanPin = 24; // the pin for fan
const int h2oPin = 26; // the pin that the LED is attached to
int incomingByte;      // a variable to read incoming serial data into
 
void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(h2oPin, OUTPUT);
  pinMode(airPin, OUTPUT);
  pinMode(fanPin, OUTPUT);
}
 
void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a capital A (ASCII 72), turn on the air pump;
    if (incomingByte == 'A') {
      digitalWrite(airPin, HIGH);
    }
        // if it's a capital A (ASCII 72), turn off the air pump;
    if (incomingByte == 'B') {
      digitalWrite(airPin, LOW);
    }
        // if it's a capital A (ASCII 72), turn on the fan;
    if (incomingByte == 'C') {
      digitalWrite(fanPin, HIGH);
    }
        // if it's a capital A (ASCII 72), turn off the fan;
    if (incomingByte == 'D') {
      digitalWrite(fanPin, LOW);
    }
    // if it's a capital H (ASCII 72), turn on the h2o pump:
    if (incomingByte == 'H') {
      digitalWrite(h2oPin, HIGH);
    }
    // if it's an L (ASCII 76) turn off the h2o pump:
    if (incomingByte == 'L') {
      digitalWrite(h2oPin, LOW);
    }    
    }
}
