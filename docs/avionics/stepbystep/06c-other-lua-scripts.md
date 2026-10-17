# Other Lua Scripts

<!-- in-progress:start -->
!!! abstract "Draft idea: not in the nav or on the live site"

    A page highlighting a few of ArduPilot's example scripts: what each one does, why it's useful for this unit, and the occasional important line. Candidates are below, with each script's own header comment as its description. Nothing here is written yet.

| Script | What it does (its own header comment) | Links to |
|---|---|---|
| [`hello_world.lua`](https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_Scripting/examples/hello_world.lua) | "an example of saying hello": the smallest possible script, sending a message to Mission Planner | 06a, as a first script |
| [`servo_set_get.lua`](https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_Scripting/examples/servo_set_get.lua) | Sets MAIN1 to 1700 PWM for a second, hands it back to its assigned function for a second, then 1100 PWM, and reads the output back | 06b, the same `set_output_pwm_chan_timeout` call |
| [`analog_input_and_GPIO.lua`](https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_Scripting/examples/analog_input_and_GPIO.lua) | Reads an analog pin, PWM in and GPIO | [07. ADC](07-adc.md) |
| [`i2c_scan.lua`](https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_Scripting/examples/i2c_scan.lua) | Scans for devices on the I²C bus | [08. I2C](08-i2c.md) |
| [`logging.lua`](https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_Scripting/examples/logging.lua) | Logs to a file on the SD card and to the dataflash log | Data logging (PLAN.md: `logger:write()`) |
| [`ahrs-print-angle-and-rates.lua`](https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_Scripting/examples/ahrs-print-angle-and-rates.lua) | Displays the vehicle's lean angles and rotation rates, once a second | Attitude in the tunnel |
| [`RCIN_test.lua`](https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_Scripting/examples/RCIN_test.lua) | Gets RC input, through scripting `RCx_OPTION`s | RC, if it stays in the MWE (ISSUES.md K5) |

`servo_scan.lua` also moves a servo "in a sinusoidal fashion", so it's close to `servo_slew.lua` and probably not worth its own entry.
<!-- in-progress:end -->
