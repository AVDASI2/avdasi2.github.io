---
icon: material/chip
---

The Cube can interface with sensors via a range of protocols. The most relevant for our purposes are the built-in Analogue-to-Digital Converter (ADC), which is usually used for an airspeed sensor, and the Inter-Integrated Circuit (I²C or I2C) protocol that enables the Cube to communicate with other devices.

The Cube only has one available ADC, which is fine for a single input e.g. a flap angle sensor. If you want to sense more channels (e.g. a fully-integrated UAV with two flaps - which **isn't** a core requirement for the unit) then you'll need some external ADCs, which are provided in your kit on a breakout board. It is strongly suggested that you begin with the internal ADC, as I2C compatibility can be tricky.

## Sensor types

There are a vast range of sensors available, but for the purposes of this unit we're interested in _angle_ and/or _position_. Sensors can be _discrete_ e.g. limit switches or light gates, or _continuous_ e.g. a potentiometer outputting a voltage corresponding to its angle of rotation.

Sensors can also be _analog_ e.g. the aforementioned potentiometer, or an LDR, or lots of other things, or _digital_ e.g. a rotary encoder, that might output a series of pulses or a more sophisticated message that might indicate an incremental change in position (that needs to be integrated into an absolute position if required), or directly send an absolute position.

For the purposes of AVDASI2 we will focus on sensors which are both _continuous_ and _analog_. You should have used these in previous years.

Some suggestions for AVDASI2 sensing:

* [Rotary potentiometers](https://uk.rs-online.com/web/c/passive-components/variable-resistors/potentiometers/?selectedNavigation=attributes.Potentiometer_Type=Rotary)
    * Lots of options! You've probably seen the rotary ones with shafts that are often used for input dials - many students default to these due to familiarity but then realise that they take up lots of space and they have to get very creative mounting them to their main structure and attaching the shaft to their linkage.
* [Through-hole potentiometer 10kΩ](https://uk.rs-online.com/web/p/potentiometers/1675335?gb=s)
    * This is one example of a different type, included in Avionics kits.
    * A low-friction option with a 'D'-shaped hole, so that an axle would not be able to slip.
    * Detailed dimensions of mounting holes available in datasheet.
* [Other potentiometers](https://uk.rs-online.com/web/c/passive-components/variable-resistors/potentiometers/)
    * Use the filters on the left to look for mounting configurations (RS's filters are really annoying - can you work out what to select to get to the Bourns 10kΩ one above? I can't). 
    * Note that 'linear' could refer to a potentiometer that measures motion in a line (also 'slide' refers to this) or one that has a linear resistance vs. position, as opposed to a logarithmic profile, which also has important uses.
* Active sensors
    * Resistive sensors are known as 'passive' - you can directly measure resistance without any other clever stuff. Other sensors exist, here are a few.
    * [Hall effect sensors](https://www.instructables.com/Hall-effect-sensor/) - use magnetic fields to measure position/rotation with no contact (there will still be a small opposing force to motion generated, but usually far less than a potentiometer - consider whether this is actually important given other friction forces in your application).
    * [Rotary/linear encoders](https://www.instructables.com/Tutorial-of-Rotary-Encoder-With-Arduino/) - noted above, but need additional processing circuitry and code.


## Integration

There are two main areas of integration considerations when selecting a sensor - listed here with a non-exhaustive list of considerations:

* **Physical integration**
    * Where will the sensor be positioned?
    * What will it be measuring? (is that what you actually intend to measure?)
    * How much space does it need?
    * How will it be attached (to its support and to the moving element, if it's e.g. a potentiometer on an axle)
    * How will you ensure the attachments won't slip?
    * How will you remove and replace it in case of failure, and at end-of-life? (Chemical bonding tends to make this tricky!)
    * Do you need to be able to adjust any positions/attachments for calibration? (Or can you do this digitally/in post-processing?)
    * ...
* **Digital integration**
    * What signal does the sensor output? What will it be inputting into?
    * What is the range and resolution of your ADC? Is this sufficient, given whatever linkage chain it's attached to?
    * Where will your wires run? Do you need to ensure any routes remain accessible?
    * Is there a maximum length or a voltage drop in your connection? Can you account for this via calibration post-integration?
    * Where will data be stored? Raw and/or postprocessed?


## Built-in ADC

You could test sensors initially using your Picos that you're familiar with, or just with a multimeter! When you're ready to integrate with the Cube:

* Make a cable to connect to the ADC port as described in the Cube [interface specification](https://docs.cubepilot.org/autopilot/the-cube/introduction/interface-specifications#analog-or-port-adc) - see the Avionics support team for a crimping induction. Note that the ADC port has +5V out, ADC in, and Ground, and the full ADC range is 6.6V (things run internally at 3.3V and there will be an internal potential divider circuit).
* Use the Ardupilot [ADC input instructions](https://ardupilot.org/plane/docs/common-analog-pins.html) and the Ardupilot's [Cube overview page](https://ardupilot.org/plane/docs/common-thecubeorange-overview.html) to view data from your analog sensor (hint: Cube overview page notes it's ADC is Ardupilot pin 8).
* To save the data from your analog sensor, it is simplest to log it to a file in the Cube's SD card. To do this, you must use a lua script, uploaded to the Cube. A basic working example script, which will log data from the analog sensor once per second for a minute, then save it to a .csv in the Cube's SD card, is available in the "06. Lua Scripts" page of these docs.



## I2C

https://en.wikipedia.org/wiki/I²C

Your I2C ADC board: https://uk.rs-online.com/web/p/analogue-development-tools/2163761?gb=s 


More to follow here too...
