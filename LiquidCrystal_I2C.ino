#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Waiting...");
}

void loop() {
  if (Serial.available() > 0) {
    char c = Serial.read();
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Expression:");
    lcd.setCursor(0, 1);
    
    if (c == 'A') {
      lcd.print("Happy");
    } else if (c == 'B') {
      lcd.print("Sad");
    } else {
      lcd.print("Unknown");
    }
  }
}
