# Minimum working example summary


## Cube Setup

|   Port       | What to plug in |
|--------------|-----------------|
| Power 1      | Power plug      |
| USB          | USB dongle      |
| Telem 1      | Wifi chip       |
| RC in        | RC transmitter  |
| AUX OUT 1    | Power pin       |
| MAIN OUT 1-8 | Servo pins      |
| I2C 2        | I2C sensor      |

Add image of full system.


## Servos


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



