---
icon: material/file-code
---

# Example Code

!!! warning "Being updated, September 2026"

    The Cube configuration, the example scripts and this guidance are being
    revised for 2026-27. A more robust version is coming shortly, including a
    ready-to-load parameter file so you can set the Cube up in one step.

    Everything here works, and is what we used last year. If something looks
    wrong or contradicts what you're told in a workshop, ask — and check back
    here before you build anything on top of the scripts.

A series of scripts were written to show a minimum viable ground station. Keep in mind your code will need to be better than this, you can’t just copy it and hope for the best. It does provide a baseline to build off of and an example of how to meet the basic functionality needed.

Each script should be able to be executed individually but Main.py allows you to execute them all simultaneously. You don’t need to take your approach in your own GS but this is good since you can debug each function independently.

!!! info "All these scripts are stored in the [avdasi2-avionics-demo](https://github.com/AVDASI2/avdasi2-avionics-demo) GitHub repository and can be accessed there."
    You can clone that repository to start your own code.

## Main.py

Links all the scripts together. Call each script as a function after defining them up top.

```python title="main.py"
--8<-- "docs/code/GCS/main_example.py"
```

## GS.py {#gs-py}

This script is what connects the cube to your ground station. It creates the connection, waits for a heartbeat, and after heartbeat is received it listens and prints messages. There’s a wide range of messages and statuses you can listen for from the cube, some more useful than others, so up to you to figure out which ones you want. It also notifies you if the heartbeat is interrupted.

```python title="GS.py"
--8<-- "docs/code/GCS/GS_example.py"
```

## Arm.py {#arm-py}

This script allows you to arm/disarm the cube and toggle its safety switch. Arming allows logging and the safety switch locks all servo movement. 

```python title="Arm.py"
--8<-- "docs/code/GCS/Arm_example.py"
```

## Servo.py

This script actuates the movement of a servo. You’ll have to edit it to allow multiple servos moving simultaneously. 

```python title="Servo.py"
--8<-- "docs/code/GCS/Servo_example.py"
```

## UI.py

This script is a barebones user interface for a GCS. It uses tkinter python module. This was used for its simplicity but you can use whatever module or language you want (there’s some that can make really nice looking UIs). The UI calls functions from the previous arming and servo controller scripts and maps them to buttons. It also allows you to input a specific servo angle and move the servo accordingly.

```python title="UI.py"
--8<-- "docs/code/GCS/UI_example.py"
```

## I2C.lua {#I2C-lua}

This script gives an overview on how to write onboard code in LUA for the Cube and how to communicate using the I2C protocol.

```lua title="I2C.lua"
--8<-- "docs/code/Onboard/I2C_LUA_example.lua"
```

## Mode-Switch.lua

```lua title="Mode-Switch.lua"
--8<-- "docs/code/Onboard/Mode_switch_example.lua"
```

