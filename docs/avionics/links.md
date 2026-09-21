---
icon: material/sunglasses
---

# Expert links

If you've got your minimal system working then here are links external docs all in one place for you to bookmark.

- Cube Orange flight controller [CubePilot docs](https://docs.cubepilot.org/autopilot/the-cube) / [ardupilot docs](https://ardupilot.org/copter/docs/common-thecubeorange-overview.html)
- [CubePilot pinout](https://docs.cubepilot.org/autopilot/the-cube/introduction/interface-specifications)
- [Mission Planner](https://ardupilot.org/planner/index.html) ground station software
- [Kahuna](https://beyond-robotix.gitbook.io/docs/kahuna/quick-start-guide) wifi module / [Ardupilot ESP8266 telemetry](https://ardupilot.org/plane/docs/common-esp8266-telemetry.html)
- PyMAVLink and [Ardupilot MAVLink command reference](https://ardupilot.org/dev/docs/mavlink-commands.html)


# Dump

I'm dumping some stuff here so it's available, but it's being worked into the step-by-step guide and then we'll provide a better-documented index somewhere.

Uselful Parameters:

| Parameter           | Value     | Meaning                                                      |
|---------------------|-----------|--------------------------------------------------------------|
| `NTF_BUZZ_VOLUME`   | 1–5       | Sets buzzer volume level                                     |
| `ARMING_CHECK`      | 0         | Disables all arming checks                                   |
| `ARMING_REQUIRE`    | 0         | Disables requirement for arming                              |
| `THR_FAILSAFE`      | 2         | Enables throttle failsafe in **land** mode.                  |
| `FLIGHTMODE_CH`     | 5         | RC channel used to switch flight modes (usually RC5).        |
| `FLTMODE1`          | 0         | Flight mode 1 = Stabilize mode.                              |
| `FLTMODE6`          | 10        | Flight mode 6 = Auto mode.                                   |
| `RC6_OPTION`        | 4         | RC6 triggers Arm/Disarm.                                     |
| `RC7_OPTION`        | 31        | RC7 triggers `Mission Start`.                                |
| `RC8_OPTION`        | 208       | RC8 triggers `Relay Toggle` (custom or user-defined action). |
| `TERRAIN_FOLLOW`    | 0         | Terrain following disabled during missions.                  |
| `TERRAIN_ENABLE`    | 0         | Terrain data not used (no elevation mapping).                |
| `SERIAL1_PROTOCOL`  | 2         | MAVLink protocol enabled on SERIAL1.                         |
| `SERIAL1_BAUD`      | 921       | Baud rate set to 921600                                      |

Default Channel Order:

| Function  | Channel | Port  |
|-----------|---------|-------|
| Aileron   | 1       | Main  |
| Elevator  | 2       | Main  |
| Throttle  | 3       | Main  |
| Rudder    | 4       | Main  |

Flap Control:

| Parameter        | Value   | Meaning                                |
|------------------|---------|----------------------------------------|
| `SERVO5_OPTION`  | 0 / 2   | 0 = PyMAVLink control, 2 = RC Control  |
| `SERVO5_MAX`     | CALC    | Maximum PWM output for SERVO5.         |
| `SERVO5_MIN`     | CALC    | Minimum PWM output for SERVO5.         |
| `SERVO5_TRIM`    | CALC    | Neutral (center) PWM value for SERVO5. |

Aileron Control:

| Parameter        | Value | Meaning                                     |
|------------------|--------|--------------------------------------------|
| `SERVO1_OPTION`  | 4      | RC passthrough or assigned aileron output. |
| `SERVO1_MAX`     | CALC   | Maximum PWM signal.                        |
| `SERVO1_MIN`     | CALC   | Minimum PWM signal.                        |
| `SERVO1_TRIM`    | CALC   | Neutral PWM value.                         |

Elevator Control:

| Parameter        | Value    | Meaning                                     |
|------------------|----------|---------------------------------------------|
| `SERVO2_OPTION`  | 0 / 19   | 0 = PyMAVLink control, 19 = RC Control      |
| `SERVO2_MAX`     | CALC     | Maximum PWM signal.                         |
| `SERVO2_MIN`     | CALC     | Minimum PWM signal.                         |
| `SERVO2_TRIM`    | CALC     | Neutral PWM value.                          |

Rudder Control:

| Parameter        | Value  | Meaning                         |
|------------------|--------|---------------------------------|
| `SERVO4_OPTION`  | 21     | Assigned rudder control output. |
| `SERVO4_MAX`     | CALC   | Maximum PWM value.              |
| `SERVO4_MIN`     | CALC   | Minimum PWM value.              |
| `SERVO4_TRIM`    | CALC   | Neutral PWM value.              |


Servo Actions

`Ctrl F` opens up some a settings menu. Click `toggle servo safety` as seen below to turn off the safety. 

![Toggle safety MP](assets/toggle_safety-MP.png)

In `Actions` there’s the arm button as seen below. This panel also allows you to manually set the flight mode.

![Arm MP](assets/arm-MP.png)

The `Servo/Relay` panel allows you to manually move servos in Mission Planner.

![servo MP](assets/servo-MP.png)

!!! tip "Make sure safety toggle is off or you won't be able to move anything"
    You'll also need to have set up the parameters for the servo you want to move
