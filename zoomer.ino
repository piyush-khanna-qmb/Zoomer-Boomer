// Piyush Khanna ji
// [Wed] 29/06/2023, 12:21 AM

#include <WiFi.h>
// Ye ji banega Hot-sapot
////////////////// Wi-Fi settings //////////////////

const char* ssid = "MyESP32Hotspot";
const char* password = "password";

////////////////// Wi-Fi settings //////////////////

////////////////// Server settings //////////////////

WiFiServer server(80);
WiFiClient client;

////////////////// Server settings //////////////////

void setup() {
  Serial.begin(115200);

  WiFi.softAP(ssid, password);
  IPAddress localIP = WiFi.softAPIP();

  server.begin();
}

void loop()
{
  if (!client.connected())
  {
    client = server.available();
    delay(1);
  }

  if (Serial.available())
  {
    String sauda = Serial.readStringUntil('\n');
    Serial.println("Sending: "+sauda);
    if (client.connected())
    {
      client.println(sauda);
    }
  }


  if (!client.connected())
  {
    client.stop();
  }
}