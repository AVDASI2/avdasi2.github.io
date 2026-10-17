# Lua servo script explained

<!-- TEMPLATE. Text is from your notes, verbatim apart from formatting.
     Every *[Placeholder: …]* is a gap your notes don't cover. Delete the
     comments and the notes box when the page is written.

     The script lives once, in assets/servo_slew.lua. Each excerpt below is
     a snippets include of a line range ("file:first:last"), with linenums
     set to the first line so the numbers match the full script. hl_lines
     counts from the top of the excerpt, not from linenums. -->

<!-- in-progress:start -->
!!! abstract "Template notes: remove before publishing"

    * "more information, examples, etc. can be found here: …" has no link yet.
    * The notes write `Param:add_param()`; the script has `param:add_param()` (line 15).
    * "These variable assignments create new parameters" is placed with lines 3–4. It may instead mean lines 20–26.
    * `:get()` is used in `update()` (lines 29–30) but the note sits with the parameter creation, so it stays there.
<!-- in-progress:end -->

`--` starts a comment. This script’s sole purpose is to generate a sine wave and turn it into a servo PWM signal.

```lua title="servo_slew.lua"
--8<-- "docs/avionics/stepbystep/assets/servo_slew.lua"
```

## Parameter Table Identity

<!-- Component: code excerpt with highlighted lines -->
```lua linenums="3"
--8<-- "docs/avionics/stepbystep/assets/servo_slew.lua:3:4"
```

<!-- Component: tip admonition, as in 03-telemetry.md -->
!!! tip

    `local` in LUA anything NOT marked local is global

These variable assignments create new parameters in Mission Planner. Note that the table key must be unique across each script on the cube otherwise they will clash. Also note, once created these parameters will survive reboots and script edits.

## Helper functions

```lua linenums="6" hl_lines="3 4"
--8<-- "docs/avionics/stepbystep/assets/servo_slew.lua:6:11"
```

Helper function to find the address of existing parameters. `p` is essentially the address of the parameter, `name`, that the function looks for. `assert` outputs an error message and stops the script if the parameter is not found.

```lua linenums="13" hl_lines="3 4"
--8<-- "docs/avionics/stepbystep/assets/servo_slew.lua:13:17"
```

Helper function to create a parameter, then find it. `Param:add_param()` creates a new parameter, then our helper function `bind_param()` finds the “address” of the new parameter.

## Creating the parameters

```lua linenums="19" hl_lines="2 4-8"
--8<-- "docs/avionics/stepbystep/assets/servo_slew.lua:19:26"
```

Utilising our helper functions, we can now create the new parameters required to customise the servo response. We create, locate, and add default values to each parameter using the helper functions we created.

`:get()` reads the current value of the parameter

## `update()`

```lua linenums="28" hl_lines="5-12"
--8<-- "docs/avionics/stepbystep/assets/servo_slew.lua:28:41"
```

Function `update()` does some maths, using some pre-existing functions, more information, examples, etc. can be found here: …

<!-- Component: info admonition, as in 02-missionplanner.md -->
!!! info "Important LUA functionality"

    instead of using a “while true” loop, LUA requires its functions to call themselves, with a delay setting.

```lua linenums="42" hl_lines="1 4"
--8<-- "docs/avionics/stepbystep/assets/servo_slew.lua:42:45"
```

`return update, 5` will repeatedly call the update function at a rate of 200 times per second. (pauses for 5ms after each cycle)

<!-- Component: information links, as on 06-lua.md -->
* [:material-information: Lua scripts](https://ardupilot.org/plane/docs/common-lua-scripts.html)
* [:material-information: Script examples](https://github.com/ArduPilot/ardupilot/tree/master/libraries/AP_Scripting/examples)

<!-- in-progress:start -->
<!-- Parked: from your notes, and possibly not needed. Inside the in-progress
     markers, so it is never published as it stands. -->
!!! abstract "Parked from your notes: may not be needed"

    LUA script to communicate the values with MP. MP custom plugin would be required to add a new slider etc to MP. Alternatives:

    * (Personal Preference) PyMAVlink + custom localhost GUI
    * Custom MP Plugin communicating with LUA script
    * Repurpose YAW gimble settings and use FOLLOW mode to avoid auto correcting
    * Use full parameter list with LUA to set specified angles (conversion can then be student-made)

    Full param list is perhaps cumbersome but would allow for a single numeric entry that should correspond to an angle of servo. Similarly, using the MP Servo/Relay tab and doing the conversion manually.

    Another option, and it may be too creative: repurpose an inaccessible Servo on the Servo/Relay tab that you will now put in the desired angle of the servo. The way this works would be: MP sends `DO_SET_SERVO` to the Servo that doesn’t exist, then, LUA reads that, knows its time to set the actual servo to the specified deflection. Then, student-made conversion algorithm converts desired angle into required PWM and outputs to the Servo that IS connected. That could give you an immediate switch between two specified degrees, and the mid-point of the two, e.g. 0,180,90 . It would also allow for students to type in the value they want, say 10, into min, then press min and all should update (may happen as soon as they hit enter)

    | Parameter | Value |
    |---|---|
    | `SERVO16_FUNCTION` | 66 (RCIN16) |
    | `SERVO5_FUNCTION` | 0 |
<!-- in-progress:end -->

<!-- Component: closing line, as in 01-cube.md and 04-power.md -->
*[Placeholder: closing line, e.g. that the next step is [ADC](07-adc.md).]*
