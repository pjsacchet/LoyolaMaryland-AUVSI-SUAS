# AdaFruit Ultimate GPS Breakout
## Pins
# Power
**VIN** = Power input, 3-5 VDC (Volts DC)

**GND** = Ground. Connect to power supply and microcontroller ground.

Optional Power pins

**EN** - When pulled to ground, turns off GPS Module.Tradeoff - lose fix if turned off and takes a while tog et fix back. Use to save power if module needs to be off for a long time.

**3.3** - Output of 3.3V regulator. Provides 100mA output.

# Serial Data
**TX** - Transmit data from GPS to microcontroller. 3.3V logic level. I think this is fine because the output can still be understood by 5V thingies (Fix later).

**RX** - Send data to GPS. Can use 3.3V or 5V logic, there is a logic level shifter.

# AdaFruit GPS Library
* We can read data from the module by calling GPS.read(). This should be called constantly.
* To check if new data has been received, call GPS.newNMEAreceived().
* If GPS.newNMEAreceived() returns True, we need to parse the data. This is called with GPS.parse(GPS.lastNMEA()).
* Once this is parsed, we can get specific data such as longitude, latitude, speed, angle, satellites (number of satellites), etc.


### Sources
https://learn.adafruit.com/adafruit-ultimate-gps?view=all - Adafruits Guide

https://learn.adafruit.com/adafruit-ultimate-gps/parsed-data-output - AdaFruit GPS Library Data Guide

