#include "DHT.h"
#define DHTPIN 2
#define DHTTYPE DHT22
#define LIGHTPIN A0

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
//  Serial.println("Crop Management Project ACS(Robotics and Automation Sem-4): ");
//  Serial.println("Humidity, Temperature and Light Values:");
  dht.begin();
}
void loop() {
  int sensor_value = analogRead(LIGHTPIN);
//  Serial.println("Light Value(Greater than 1000 = Day or else less than 1000 = Night):");
  Serial.println("");
  Serial.print("Sunlight: ");
  Serial.print(sensor_value);
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(temperature) || isnan(humidity))
  {
    Serial.println("Failed to read from dht sensor");
  }
  else
  {
    Serial.print(" Humidity: ");
    Serial.print(humidity);
    Serial.print("% ");
    Serial.print(" Temperature: ");
    Serial.print(temperature);
    Serial.print("*C ");
    
  }
  delay(500);
}
