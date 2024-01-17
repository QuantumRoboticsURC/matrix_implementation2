#include <Adafruit_GFX.h>
#include <Adafruit_NeoMatrix.h>
#include <Adafruit_NeoPixel.h>
#ifndef PSTR
 #define PSTR // Make Arduino Due happy
#endif

#define PIN 23
#define LED_RED_HIGH     (31 << 11)
#define LED_GREEN_HIGH     (63 << 5)  

#define LED_BLUE_HIGH     31
const int pinx = 25;
const int piny = 26;
const int pinz = 33;


Adafruit_NeoMatrix matrix = Adafruit_NeoMatrix(8, 8, 1, 1, PIN,
  NEO_TILE_TOP   + NEO_TILE_RIGHT   + NEO_TILE_ROWS   + NEO_TILE_PROGRESSIVE +
  NEO_MATRIX_TOP + NEO_MATRIX_RIGHT + NEO_MATRIX_ROWS + NEO_MATRIX_ZIGZAG,
  NEO_GRB + NEO_KHZ800);

const uint16_t colors[] = {
  matrix.Color(255, 0, 0), matrix.Color(0, 255, 0), matrix.Color(0, 0, 255) };

void setup() {
  matrix.begin();
  matrix.setTextWrap(false);
  matrix.setBrightness(20);
  matrix.setTextColor(colors[2]);
  pinMode(pinx, INPUT);
  pinMode(piny, INPUT);
  pinMode(pinz, INPUT);

}

int x    = matrix.width();
int pass = 0;

void loop() {
  int estx = digitalRead(pinx);
  int esty = digitalRead(piny);
  int estz = digitalRead(pinz);
  if (esty == 0 && estx == 0 && estz == 0){
     matrix.fillScreen(0);
     matrix.show();
  }
  else if (esty == 1 && estx == 0 && estz == 0){
    matrix.fillScreen(colors[0]);
    matrix.show();
  
  }
  else if (esty == 0 && estx == 1 && estz == 0){
    matrix.fillScreen(colors[1]);
    matrix.show();
    delay(500);
    matrix.fillScreen(0);
    matrix.show();
    delay(500);
  }
   else if (esty == 1 && estx == 1 && estz == 0){
    matrix.fillScreen(colors[2]);
    matrix.show();
  }
  else if (esty == 0 && estx == 0 && estz == 1){
  matrix.fillScreen(0);
  matrix.setCursor(x, 0);
  matrix.print(F("QUANTUM ROBOTICS"));
  matrix.setRotation(0);
  if(--x < -96) {
    x = matrix.width();
  }
  matrix.show();
  delay(250);
  }
  else{
    matrix.fillScreen(0);
    matrix.show();
  }
}
