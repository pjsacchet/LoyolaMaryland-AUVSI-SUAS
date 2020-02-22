# AdaFruit Ultimate GPS Breakout
## Pins
### Power
**VIN** = Power input, 3-5 VDC (Volts DC)

**GND** = Ground. Connect to power supply and microcontroller ground.

Optional Power pins

**EN** - When pulled to ground, turns off GPS Module.Tradeoff - lose fix if turned off and takes a while tog et fix back. Use to save power if module needs to be off for a long time.

**3.3** - Output of 3.3V regulator. Provides 100mA output.

### Serial Data Pins
**TX** - Transmit data from GPS to microcontroller. 3.3V logic level. I think this is fine because the output can still be understood by 5V thingies (Fix later).

**RX** - Send data to GPS. Can use 3.3V or 5V logic, there is a logic level shifter.

### Other Pins - Very vague
**FIX** - Output pin. Pulses every second when no fix. When there is a fix, pulses once every 15 seconds for 200 milliseconds.
**PPS** - Output for V3 modules.

## AdaFruit GPS Library
* We can read data from the module by calling GPS.read(). This should be called constantly.
* To check if new data has been received, call GPS.newNMEAreceived().
* If GPS.newNMEAreceived() returns True, we need to parse the data. This is called with GPS.parse(GPS.lastNMEA()).
* Once this is parsed, we can get specific data such as longitude, latitude, speed, angle, satellites (number of satellites), etc.

## Battery info
GPS comes with a real time clock. A C31220 battery can be attached as a backup

## Antenna 
> There is an output sentence that will tell you the status of the antenna. $PGTOP,11,x where x is the status number. If x is 3 that means it is using the external antenna. If x is 2 it's using the internal antenna and if x is 1 there was an antenna short or problem.
>On newer shields & modules, you'll need to tell the firmware you want to have this report output, you can do that by adding a gps.sendCommand(PGCMD_ANTENNA) around the same time you set the update rate/sentence output.

## GPS Output
http://aprs.gids.nl/nmea/ - Info on NMEA sentences and what they mean (The text output the drone spits out).
RMC Line (Recommended Minimum) - All the useful data. Meaning of each part:
* GMT Current Time
* Status Code - V = Void (invalid), A = Active (GPS can get a lock/fix)
* Next 4: GPS Coords.
* Ground speed in knots 
* Current Date
* Data transfer checksum

### Sources
https://learn.adafruit.com/adafruit-ultimate-gps?view=all - Adafruits Guide

https://learn.adafruit.com/adafruit-ultimate-gps/parsed-data-output - AdaFruit GPS Library Data Guide

