#include <TouchScreen.h>

#include <Elegoo_TFTLCD.h>
#include <pin_magic.h>
#include <registers.h>

#include <Elegoo_GFX.h>


#define LCD_CS A3                                               // Chip Select goes to Analog 3
#define LCD_CD A2                                               // Command/Data Goes to Analog 2
#define LCD_WR A1                                               // LCD Write goes to Analog 1
#define LCD_RD A0                                               // LCD Read goes to Analog 0

#define LCD_RESET A4                                            // LCD Reset goes to Analog 4

#define BLACK    0x0000                                          // Color definitions hex
#define BLUE     0x001F
#define RED      0xF800
#define GREEN    0x07E0
#define CYAN     0x07FF
#define MAGENTA  0xF81F
#define YELLOW   0xFFE0 
#define WHITE    0xFFFF


Elegoo_TFTLCD tft(LCD_CS, LCD_CD, LCD_WR, LCD_RD, LCD_RESET); // Create instance of LCD called tft


void setup(void) {
  Serial.begin(9600);

  tft.reset();

  tft.begin(0x9341);
  
}

void loop(void) {
  tft.setRotation(1);         //sets to landscape
  tft.fillScreen(BLUE);       //fills screen with BLUE
  tft.setCursor(0, 0);        //cursor to upper left

  tft.setTextColor(RED);      //sets text color to red
  tft.setTextSize(3);         //text size 3 (1-6)
  tft.println("HYDRODUINO!!");

  delay(3000);
}
