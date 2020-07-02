#include <dht11.h>
#include <MsTimer2.h>
#define DHT11_PIN 4
#define LIGHTSENSOR_PIN 5
#define LED_GREEN_PIN 6
#define BEEP_PIN 7
#define TRACKSENSOR_PIN 8
#define LIGHTSENSOR_ANALOG_PIN A0
#define VOICE_PIN 9
#define GAS_PIN A1
#define RAIN_PIN A2

dht11 DHT;
int chk, temp, humidity, alert_flag, light, voice, track, gas, rain;

void setup() {
  Serial.begin(9600);
  pinMode(LIGHTSENSOR_PIN, INPUT);
  pinMode(TRACKSENSOR_PIN, INPUT);
  pinMode(LED_GREEN_PIN, OUTPUT);
  pinMode(BEEP_PIN, OUTPUT);
  pinMode(LIGHTSENSOR_ANALOG_PIN, INPUT);
  pinMode(VOICE_PIN, INPUT);
  pinMode(GAS_PIN, INPUT);
  pinMode(RAIN_PIN, INPUT);
  MsTimer2::set(1000, update);
  MsTimer2::start();
}

void loop() {
  chk = DHT.read(DHT11_PIN); // READ DATA
  temp = DHT.temperature;
  humidity = DHT.humidity;
  alert_flag = 0;
  light = analogRead(LIGHTSENSOR_ANALOG_PIN);
  voice = digitalRead(VOICE_PIN);
  track = digitalRead(TRACKSENSOR_PIN);
  gas = analogRead(GAS_PIN);
  rain = analogRead(RAIN_PIN);

  if (digitalRead(LIGHTSENSOR_PIN)) {
    digitalWrite(LED_GREEN_PIN, HIGH);
  }
  else {
    digitalWrite(LED_GREEN_PIN, LOW);
    digitalWrite(BEEP_PIN, HIGH);
  }

  if (track or voice or gas > 600 or rain < 800) {
    alert_flag = 1;
  }

  if (alert_flag) {
    digitalWrite(BEEP_PIN, LOW);
  }
  else {
    digitalWrite(BEEP_PIN, HIGH);
  }
}

void update() {
  Serial.print("data");
  Serial.print(' ');

  Serial.print(temp);
  Serial.print(' ');

  Serial.print(humidity);
  Serial.print(' ');

  if (light < 100) {
    Serial.print(0);
  };
  Serial.print(light);
  Serial.print(' ');

  Serial.print(gas);
  Serial.print(' ');

  if (rain < 1000) {
    Serial.print(0);
  };
  Serial.print(rain);
  Serial.print(' ');

  Serial.print(voice);
  Serial.print(' ');

  Serial.print(track);
  Serial.print(' ');

  Serial.println(alert_flag);
}
