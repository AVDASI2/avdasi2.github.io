# PyMAVLink

The cube uses MAVLink, a lightweight communication protocol to receive commands and transmit data to and from the Ground Station. Python has a MAVLink module called Pymavlink that will allow to send and capture MAVLink messages.

To be able to do so, first the code must connect to the Cube through MAVLink (see [Cube Information](cube.md) for how to physically connect to the Cube). An example code will be provided to show a baseline for how to connect to the flight controller with python. (See [GS.py](examplecode.md#gs-py))

!!! tip "Make sure to disconnect from Mission Planner before connecting through PyMAVLink, otherwise it won't work."

Another example code will show how to send commands over MAVLink (in particular, arming the Cube see [Arm.py](examplecode.md#arm-py)). Use this to develop your code.

Sending Commands using MAVLINK: Use the `command_long_send` function of the mavlink library to send control demands to the cube.

This command takes 7 parameters: 
```
(target_system, target_component, command, confirmation, param1 - 7)
```


!!! info "pyMAVLINK “module not found” error"
    Run `pip --upgrade --force-reinstall pymavlink` in an administrator command prompt

    

[Servo Movement documentation (ardupilot.org)](https://ardupilot.org/dev/docs/mavlink-move-servo.html)

[MAVLink common messages (mavlink.io)](https://mavlink.io/en/messages/common.html)