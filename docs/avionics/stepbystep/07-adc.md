## ADC

The Cube contains an analog-to-digital converter (ADC) (actually, it contains three - but two are used for battery voltage monitoring). The externally-exposed ADC is by default used for airspeed sensing but we can use it to measure any analog signal. 

Note the pinout for the ADC connector in the [Cube interface specifications](https://docs.cubepilot.org/autopilot/the-cube/introduction/interface-specifications). The 1.25mm JST-GH connectors are fiddly to crimp, but pre-crimped wires are available.


## Example Lua Script - Outputting and Logging Analogue Sensor Data

The following script is an example code which logs data from an analogue sensor plugged into the "ADC" port on the Cube's carrier board. The script logs data for 1 minute, at 1Hz, outputting the readings to the "Messages" tab in Mission Planner and saving the results to potentiometer_log.csv. Once the minute has passed, navigate to the Cube's root directory (Config -> MAVftp).

The code is well commented - the idea is that you can adapt it to your needs and desires (e.g. transmitting to a ground station, deciding whether to preprocess onboard or on the GS, etc). Make sure to consult the scripting docs linked from the Luascript section, and see what you can create!

```lua
-- Minimum working example: Logging analog readings from CubeOrange+ ADC port to a .csv file on the Cube's SD card.
local file_name = "potentiometer_log.csv" -- Log file name
local file -- File object initialisation
local analog_in = analog:channel()
local pot_voltage = {} -- Table to hold potentiometer voltage readings
local count = 0 -- Readings counter initialisation
local READINGS_COUNT = 60 -- Number of readings to log
local LOOP_DELAY_MS = 1000 -- Delay between readings in milliseconds

if not analog_in:set_pin(8) then
  gcs:send_text(0, "Invalid analog pin")
end -- Sets ADC pin 8 for potentiometer input

file = io.open(file_name, "a")
if not file then
  error("Could not make file")
end -- Opens file for data logging

file:write('Time [ms], Potentiometer Voltage [V]\n')
file:flush() -- Writes CSV header

local function write_to_file()
  if not file then
    error("Could not open file")
  end -- Error check
  file:write(tostring(millis()) .. ", " .. table.concat(pot_voltage,", ") .. "\n") -- Writes data with timestamp, in CSV format
  file:flush() -- Updates the file
end -- Writes data to file

function update()
  pot_voltage[1] = analog_in:voltage_latest() -- Gets latest voltage reading from potentiometer
  gcs:send_text(0, string.format("Potentiometer Voltage: %.2f V", pot_voltage[1])) -- Outputs voltage to GCS
  write_to_file() -- Calls function to write data to file
  count = count + 1
  if count >= READINGS_COUNT then
    file:close()
    return nil
  end -- Stops logging after set number of readings
  return update, LOOP_DELAY_MS
end

return update()
```