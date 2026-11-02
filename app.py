


#define BUTTONPIN 2
#define LEDPIN 8

void setup() {
  pinMode(BUTTONPIN, INPUT_PULLUP);
  pinMode(LEDPIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int buttonState = digitalRead(BUTTONPIN);

  if (buttonState == LOW) {
    Serial.println("EMERGENCY ACTIVATED");

    digitalWrite(LEDPIN, HIGH);
    delay(500); // TASK 1: Change to 250

    digitalWrite(LEDPIN, LOW);
    delay(500); // TASK 2: Change to 250

  } else {
    digitalWrite(LEDPIN, LOW);
    Serial.println("SYSTEM STANDBY");
    delay(50);
  }
}
