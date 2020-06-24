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
  int temp, humidity;
  temp = DHT.temperature;
  humidity = DHT.humidity;
  Serial.print("data");
  Serial.print(temp);
  Serial.println(humidity);
  delay(1000);
}



