int switchPin= 2;
int xpin= A0;
int ypin= A1;

void setup() {
  Serial.begin(9600);
  pinMode(switchPin,INPUT);

}
void loop() {
  int sw_state=digitalRead(switchPin);
  int x_val=analogRead(xpin);
  int y_val=analogRead(ypin);
  Serial.print("Sw state:");
  Serial.println(sw_state);
  delay(10000);
  Serial.print("X value:");
  Serial.println(x_val);
   delay(100000);
  Serial.print("y val: ");
  Serial.println(y_val);
   delay(10000);

  delay(100);

}
