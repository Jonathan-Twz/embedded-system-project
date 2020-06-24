#include <dht11.h>
dht11 DHT;
#define DHT11_PIN 4

void setup(){
  Serial.begin(9600);
}

void loop(){
  int chk;
  chk = DHT.read(DHT11_PIN); // READ DATA
//  switch (chk){
//  case DHTLIB_OK: 
//    Serial.println("OK,\t"); 
//    break;
//  case DHTLIB_ERROR_CHECKSUM: 
//    Serial.println("Checksum error,\t"); 
//    break;
//  case DHTLIB_ERROR_TIMEOUT: 
//    Serial.println("Time out error,\t"); 
//    break;
//  default: 
//    Serial.println("Unknown error,\t"); 
//    break;
//  }
  Serial.print("humidity(%):");
  Serial.println(DHT.humidity,1);
  Serial.print("tempe(C):");
  Serial.println(DHT.temperature,1); 
  Serial.println(" ");
  delay(1000);
}


