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
#define BACKBLUE 0x31AA
#define GRAY     0xC618
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

  Elegoo_GFX_Button lightButton(void);
  void initButton(Elegoo_GFX *gfx, int16_t 50, int16_t 110, 
		      uint8_t 50, uint8_t 50, 
		      uint16_t WHITE, uint16_t GRAY, uint16_t WHITE,
		      char *"on/off", uint8_t 2);
  void drawButton(boolean inverted = false);
  boolean contains(int16_t 40, int16_t 110);

void loop(void) {
  tft.setRotation(1);         //sets to landscape
  tft.fillScreen(BACKBLUE);       //fills screen with BLUE
  tft.setCursor(100, 0);        //cursor to upper left

  tft.setTextColor(WHITE);      //sets text color to red
  tft.setTextSize(2);         //text size 3 (1-6)
  tft.println("HYDRODUINO");

  tft.setCursor(50, 20);
  tft.setTextColor(WHITE);
  tft.setTextSize(1);
  tft.println("Temperature                Humidity");

  tft.fillRoundRect(45, 35, 75, 50, 6, GRAY);        //rounded rectangle (x, y, width, height, radius, color)

  tft.fillRoundRect(200, 35, 75, 50, 6, GRAY);

  tft.setCursor(45, 100);
  tft.setTextColor(WHITE);
  tft.setTextSize(1);
  tft.println("Lights            Fan            Pumps");

 
  tft.fillRoundRect(135, 110, 50, 50, 6, GRAY);
  tft.fillRoundRect(225, 110, 50, 50, 6, GRAY);

  tft.setCursor(120, 170);
  tft.setTextColor(WHITE);
  tft.setTextSize(1);
  tft.println("Add Nutrients");

  tft.fillRoundRect(40, 190, 40, 40, 6, WHITE);
  tft.fillRoundRect(90, 190, 40, 40, 6, WHITE);
  tft.fillRoundRect(140, 190, 40, 40, 6, WHITE);
  tft.fillRoundRect(190, 190, 40, 40, 6, WHITE);
  tft.fillRoundRect(240, 190, 40, 40, 6, WHITE);

  delay(6000);
}
