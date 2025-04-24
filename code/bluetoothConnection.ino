#include <SoftwareSerial.h>

SoftwareSerial mySerial(TxD of Bluetooth Module, RxD of Bluetooth Module);

void setup() {
	//	Open serial communications and wait for port
  Serial.begin(9600);
  mySerial.begin(9600);
  while (!Serial) {
  ;
  }
  Serial.println("Start Communication");
}

void loop() {
  if (mySerial.available()) {
  	Serial.write(mySerial.read());
  }
  if (Serial.available()) {
  	mySerial.write(Serial.read());
  }
}
  
 
