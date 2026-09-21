# Lua Scripting

Ardupilot/Mission Planner are pretty functional, but we're working a little 'off-design' - we're using a flight controller that expects to be, well, flying, and we're confusing it by not giving it a GPS signal, constraining some of its degrees of freedom in the tunnel, and asking it to do things that would probably be a bad idea in flight (e.g. direct manual positioning of control surface servos).

We can work around this using the built-in scripting functionality. The Cube supports Lua scripting (via ArduPilot), enabling onboard automation such as custom sensor logging, custom failsafes, LED behavior, telemetry filtering, or mission logic without requiring firmware modification (which is a good idea for verification/certification of core flight functionality). Lua is a lightweight, high-level scripting language designed for embedded systems, making it ideal for writing custom logic directly on the Cube.

!!! tip "Don't be scared of Lua!"
    It's a strange programming language, but it's the only way to write onboard code for the Cube.
    You'll get used to it don't worry.

Ardupilot scripting support pages: 

* [:material-information: Lua scripts](https://ardupilot.org/plane/docs/common-lua-scripts.html)
* [:material-information: Script setup and use examples](https://ardupilot.org/plane/docs/common-scripting-step-by-step.html)
* [:material-information: Script examples](https://github.com/ArduPilot/ardupilot/tree/master/libraries/AP_Scripting/examples) - really wide range

## Enabling scripting on the CubePilot

Before Lua scripts can be executed onboard the flight controller, the scripting feature must be enabled using the parameters of the Cube. Using Mission Planner (or any other similar GS program), locate the `SCR_ENABLE` parameter and set it to `1` before rebooting the Cube. A new folder should appear in the `APM` folder named `scripts`; if it doesn’t, it needs to be manually created. After this is done, any Lua code uploaded into this folder will be automatically executed when the Cube is rebooted after uploading.

To access the Cube's directories, go to Config -> MAVftp on Mission Planner.

