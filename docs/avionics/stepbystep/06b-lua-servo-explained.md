# How the Lua Servo Script Works

This page explains `servo_slew.lua`, the script you ran on the [previous page](06a-lua-servo.md). It's shown below a section at a time, with line numbers matching the full script. You should already have it running; this page gives you the understanding to customise it, or to write one of your own.

The script's sole purpose is to generate a sine wave and turn it into a servo PWM signal.

??? example "The whole script, `servo_slew.lua`"

    ```lua
    --8<-- "docs/avionics/stepbystep/assets/servo_slew.lua"
    ```

!!! tip "Reading Lua"

    * `--` starts a comment. Lua ignores the rest of the line.
    * `local` keeps a variable inside this script. Anything **not** marked `local` is global.
    * A colon just means "do this to that". `STEST_CHAN:get()` means "get the value of `STEST_CHAN`", and `param:add_table()` means "add a table to the parameters". Read it left to right and it usually says what it does.

## Naming the parameter table

```lua linenums="3"
--8<-- "docs/avionics/stepbystep/assets/servo_slew.lua:3:4"
```

The script creates its own parameters, which then appear in Mission Planner's Full Parameter List. Script parameters are grouped together by a table key, and each parameter in the table is given a prefix, so that you can search for them in the list. The prefix becomes part of every parameter's name.

* **`PARAM_TABLE_KEY`** is this script's table key, 135.
* **`PARAM_TABLE_PREFIX`** is the prefix, `STEST_`. Searching for `STEST` in the Full Parameter List finds all five of the script's parameters.

!!! warning "Each script needs its own table key"

    If two scripts on your Cube use the same table key, their parameters will compete and things won't work as expected. When you write a script with parameters of its own, give it a different key, and a different prefix.

## Two helper functions

The script uses two small helper functions so that it doesn't have to repeat itself for every parameter.

```lua linenums="6" hl_lines="3 4"
--8<-- "docs/avionics/stepbystep/assets/servo_slew.lua:6:11"
```

**`bind_param()` finds an existing parameter by name.** `Parameter()` creates an empty parameter object, `p`, and `p:init(name)` points it at the parameter called `name`. You can think of `p` as the parameter's address: the script uses it later to read the value. If there's no parameter with that name, `assert` outputs an error message and stops the script.

!!! tip "`assert()` for error messages"
    
    `assert()` runs the thing in the first parameter it's passed, and if the run fails it gives the error message in the second parameter. This is handy for debugging. 

```lua linenums="13" hl_lines="3 4"
--8<-- "docs/avionics/stepbystep/assets/servo_slew.lua:13:17"
```

**`bind_add_param()` creates a parameter, then finds it.** `param:add_param()` adds a new parameter to the table, at position `idx` and with a default value. Then `bind_param()` finds the "address" of the new parameter, using its full name: the prefix and the name joined together with `..`, so `'CHAN'` becomes `STEST_CHAN`.

## Creating the parameters

```lua linenums="19" hl_lines="2 4-8"
--8<-- "docs/avionics/stepbystep/assets/servo_slew.lua:19:26"
```

Line 20 creates the table itself, with room for 10 parameters. Lines 22 to 26 then use the helper functions to create, locate and set a default for each of the five parameters, and keep the address of each in a variable of the same name.

These are the parameters you met on the previous page.

!!! note "Parameters stay set"

    Once you've set a value, it's stored on the Cube, so it survives reboots and edits to the script.

## The update function

`update()` is where the work happens. It runs 200 times a second, and the line that makes that happen is `return update, 5` (line 42): each time `update()` finishes, it asks ArduPilot to run it again 5 ms later. There's more on this [below](#running-it-again-and-again).

```lua linenums="28" hl_lines="15"
--8<-- "docs/avionics/stepbystep/assets/servo_slew.lua:28:43"
```

### Reading the settings

```lua linenums="29"
--8<-- "docs/avionics/stepbystep/assets/servo_slew.lua:29:31"
```

`:get()` reads the current value of a parameter. If `STEST_CHAN` or `STEST_FREQ` is 0, the rest is skipped, so setting either to 0 turns the script off.

!!! tip "Changes take effect straight away"

    Because the script reads its parameters every time `update()` runs, a change you make in Mission Planner takes effect as soon as you click `Write Params`, without a reboot. Try changing `STEST_FREQ` or `STEST_PCT` while the servo is moving.

### Making the sine wave

```lua linenums="32"
--8<-- "docs/avionics/stepbystep/assets/servo_slew.lua:32:34"
```

Line 32 gets the time since the Cube was switched on. `millis()` gives it in milliseconds, so multiplying by 0.001 turns it into seconds. (`:tofloat()` just turns it into an ordinary number that Lua can do maths with.)

Line 33 is π, near enough.

Line 34 is where the movement comes from. A sine wave rises smoothly to +1, falls back through 0 to -1, and rises again, over and over: the same back-and-forth we want from the servo. Feeding it the time makes it move as time passes. With `STEST_FREQ` at 1, this is what happens over the first second:

| Time (s) | `output` | Servo |
|---|---|---|
| 0 | 0 | Centre |
| 0.25 | +1 | One end |
| 0.5 | 0 | Centre |
| 0.75 | -1 | Other end |
| 1 | 0 | Centre, ready to go again |

The rest of what's inside `math.sin()`, the `pi`, `freq` and `2.0`, sets how fast it goes round. With `STEST_FREQ` at 2, everything in that table happens twice as fast, so the servo goes there and back twice a second.

Last, `STEST_PCT` × 0.01 shrinks the swing. At 100 nothing changes; at 50, `output` only reaches +0.5 and -0.5.

### Turning it into a PWM signal

```lua linenums="35"
--8<-- "docs/avionics/stepbystep/assets/servo_slew.lua:35:38"
```

The wave is centred on the midpoint of `STEST_PWM_MIN` and `STEST_PWM_MAX`, and scaled so that a full swing reaches each end. `math.floor()` rounds the result down to a whole number, because a PWM signal is set in whole microseconds.

### Sending it to the servo

```lua linenums="39"
--8<-- "docs/avionics/stepbystep/assets/servo_slew.lua:39:39"
```

`SRV_Channels:set_output_pwm_chan_timeout()` sets the output to that PWM signal, overriding the autopilot.

!!! info "ArduPilot counts outputs from zero here"

    That's why the script passes `chan-1`: output 5, your MAIN OUT 5, is number 4. Parameter names like `SERVO5_FUNCTION` count from 1, so this is an easy one to trip over in your own scripts.

!!! note "The 100 ms timeout"

    The last value, `100`, makes the override last for 100 ms, after which the output goes back to the autopilot's control. `update()` renews it every 5 ms, so while the script runs it keeps control, but if the script stops, the servo isn't left stuck where it was.

### Line 40

```lua linenums="40"
--8<-- "docs/avionics/stepbystep/assets/servo_slew.lua:40:40"
```

!!! warning "Don't switch line 40 on as it is"

    Removing the `--` would print every PWM value to Mission Planner's `Messages` tab, 200 times a second: far too fast to read, and enough to flood the link. If you want to see the values, print them much less often.

## Running it again and again

```lua linenums="42" hl_lines="1 4"
--8<-- "docs/avionics/stepbystep/assets/servo_slew.lua:42:45"
```

!!! info "No `while true` loops"

    In a lot of languages you'd repeat something with a `while true` loop. An ArduPilot script can't do that, because a loop that never finishes would hold up the autopilot. Instead, the function finishes each time, and tells ArduPilot which function to call next and how long to wait first.

`return update, 5` asks ArduPilot to call `update()` again in 5 ms. The comment after it, `-- 200Hz`, is the author's note of what that works out to: once every 5 ms is 200 times a second. The last line, `return update()`, starts the cycle: it runs `update()` once as soon as the script loads, and that run schedules the next.

## Going further

### PWM limits or percentage?

This script has two ways of adjusting the servo's movement limits. The short table below compares them.

| | `STEST_PCT` | `STEST_PWM_MIN` and `STEST_PWM_MAX` |
|---|---|---|
| What it changes | How much of the range is used | Where the ends of the range are |
| The centre | Stays put | Moves to halfway between the two |
| Can one side move further than the other? | No | Yes |
| Values to set | One | Two |

!!! question "Thought experiment"

    Under what circumstances would you choose to use `STEST_PCT` instead of `STEST_PWM_MIN` and `STEST_PWM_MAX`? Think about what each one is for, rather than which is better.

??? question "Check your understanding: which would you use to stop a control surface hitting its end stops?"

    The limits: measure where the mechanism's end stops are, and set `STEST_PWM_MIN` and `STEST_PWM_MAX` just inside them.

    But look at line 34 again. Nothing in the script stops `STEST_PCT` going above 100, and if it does, the servo is driven **past** your limits. A limit that can be overridden by accident isn't much of a limit. A safer script would clamp `pwm` between `pwm_min` and `pwm_max` before sending it.

!!! tip "Things to try"

    Do these with the servo free, not fitted to a mechanism.

    1. Change `STEST_FREQ` while the servo is moving. Try 0.5, then 2.
    2. Set `STEST_PCT` to 50, and watch the swing halve about the same centre.
    3. Set `STEST_PWM_MIN` to 1200 and leave `STEST_PWM_MAX` at 2000. Where's the centre now?
    4. Set the limits to 1250 and 1750, then set `STEST_PCT` to 150. Where does the servo go, and why?
    5. Add a line before line 39 that clamps `pwm` between `pwm_min` and `pwm_max`, upload it, and try step 4 again. Lua's `math.max()` and `math.min()` will do it.
    6. Compare the script's 1000 to 2000 with the `Min` and `Max` columns for output 5 in `Servo Output`. Which one does the servo obey?
    7. Move the servo to another output, set that output's `SERVOn_FUNCTION` to 0, and point `STEST_CHAN` at it.
    8. Make line 40 print the PWM value once a second instead of 200 times. You'll need a counter.
    9. Change line 34 so the servo jumps between the two ends instead of sweeping smoothly.
    10. Make a copy of the script with its own table key and prefix, and run both at once on two servos.

* [:material-information:ArduPilot - Lua scripts](https://ardupilot.org/plane/docs/common-lua-scripts.html)
* [:material-information:ArduPilot - Lua API reference](https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_Scripting/docs/docs.lua) - every function a script can call, including the ones used here
* [:material-information:ArduPilot - Script examples](https://github.com/ArduPilot/ardupilot/tree/master/libraries/AP_Scripting/examples) - really wide range

Next, the guide moves on from servos to reading sensors, starting with the Cube's [ADC](07-adc.md).
