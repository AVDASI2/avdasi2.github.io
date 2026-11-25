---
icon: material/gauge
---

# Sensors: worked examples

Your closed loop works from what the Cube itself measures, such as its pitch and the PWM it sends. An external sensor gives you an **independent check**: something outside the loop that tells you, for example, the landing gear is deployed. This external validation is critical to both: confirming expected behaviour during live operation, and for reference during reflective activity, such as your reports.

This page brings together the pieces you need, on other pages, and walks through **two worked examples** from sensor to plot: the angle of a flap, and whether the landing gear is down.

!!! note "This is a starting point, not a finished product"

    The examples show one way of doing it, so you can see every step working. They aren't the answer. Decide what *your* model needs to confirm, which sensor and input suit it, and how you'll know you can trust the reading. Use the examples to learn, then build your own.

## How the pieces fit

A reading goes through four stages:

1. **A sensor** turns position into a voltage, or a switch into on and off.
2. **An analog-to-digital converter (ADC)** turns the voltage into a number: either the Cube's own ADC port, or the 16-bit I²C ADC board in your kit.
3. **A Lua script on the Cube** reads that number and sends it to the ground station as a *named value*.
4. **CubeGUI** shows it, plots it and logs it. The Cube's own log records it too.

| To do this | Go to |
|---|---|
| Choose a sensor, and think through fitting it | [Sensors](../sensors.md) |
| Wire it to the I²C ADC board, and use the example script (recommended) | [11. I2C](11-i2c.md) |
| Wire it to the Cube's own ADC | [12. ADC](12-adc.md) |
| Read an on/off switch on a spare output pin, with no ADC | [Part B](#b-if-your-sensor-only-says-yes-or-no-is-the-gear-down), below |
| Get a Lua script onto the Cube | [06. Servos via Lua Script](06-lua-servo.md) |
| Show, plot, and log the value in CubeGUI | [CubeGUI recipes](https://github.com/AVDASI2/CubeGUI/blob/main/docs/recipes.md) 1, 2, 3 and 7 |

## A. Is the flap where we expect?

The set-up: a potentiometer on the bench, wired to channel 0 of the I²C ADC board, and a script built from the ADS1115 example on the [I2C page](11-i2c.md). You get the whole chain working first (sensor, board, script, CubeGUI), turning the potentiometer by hand. Fitting it to your model comes last.

### 1. Wire it to the I²C ADC board

1. Connect the board to the Cube, as on the [I2C page](11-i2c.md).
2. Connect the potentiometer's outer pins to the board's supply and ground, and its middle pin (the wiper) to **channel 0**.

!!! warning "Careful"

    Never put more on an input than the board's supply voltage. The board can't measure it, and may be damaged.

### 2. Run the example script unchanged

1. Copy the ADS1115 script from the [I2C page](11-i2c.md) into a new file called `flap_adc.lua`.
2. Put it on the Cube in `APM/scripts`, as on [06. Servos via Lua Script](06-lua-servo.md), and reboot.
3. In Mission Planner's Messages tab, check you see `ADS1115 detected successfully`, then a line of four readings in mV every second.
4. Turn the potentiometer by hand: the first of the four numbers (channel 0) should change.

!!! note "Why unchanged first"

    If it works now and breaks later, the fault is in the change you made, not in the wiring.

!!! warning "Careful"

    `ADS1115 not detected on I2C bus!` means the Cube can't find the board: check the wiring, and the board's address switch (the script expects 0x48).

### 3. Change the script to send named values

**What we want.** CubeGUI to plot the reading live and log it. For that, the script has to send the reading as a *named value*, all the time, about 10 times a second.

**How a script sends a named value.** One line does it:

```lua
gcs:send_named_float("ADC0", voltage_readings[1])
```

`gcs` is the Cube's link to the ground station, and `send_named_float` sends one number with a name attached. The name (`ADC0`) is how CubeGUI finds the number: up to 10 characters, and anything longer is cut short. The number here is channel 0's reading, in mV. The Cube also writes every named value into its own log.

**What the script does now.** In `update()`, find the line `if current_channel >= 4 then`. The block under it runs each time all four channels have been read:

```lua
            if current_channel >= 4 then -- Do this if all 4 channels have been read
                gcs:send_text(0, string.format("ADC: %.0f, %.0f, %.0f, %.0f mV", 
                              voltage_readings[1] or 0,
                              voltage_readings[2] or 0,
                              voltage_readings[3] or 0,
                              voltage_readings[4] or 0)) -- Outputs to GCS
                write_to_file() -- Writes to file
                count = count + 1 -- Increments counter
                if count >= READINGS_COUNT then
                    file:close()
                    gcs:send_text(0, "Logging complete. File closed.")
                    return
                end -- Stops logging after set number of readings
                current_channel = 0 -- Resets for next cycle
                return update, LOOP_DELAY_MS -- Reschedules with full loop delay
```

| Lines | What they do now | For CubeGUI |
|---|---|---|
| `gcs:send_text(...)` (the first five lines) | Send all four readings as one line of text, to the Messages tab | Text can be read, but not plotted: **replace** them with four named values |
| `write_to_file()` | Adds the line to a CSV file on the SD card | CubeGUI's log and the Cube's own log already record named values: **remove** it |
| `count = ...` down to `end -- Stops logging...` | Count the readings, and stop the script after 60 of them | CubeGUI needs readings for as long as it's connected: **remove** them |
| `current_channel = 0` | Go back to channel 0 for the next round | **Keep** |
| `return update, LOOP_DELAY_MS` | Wait `LOOP_DELAY_MS` before the next round | **Keep**, and change the delay (below) |

**How fast.** Each round reads four channels, about 20 ms each, so about 80 ms, then waits `LOOP_DELAY_MS`. At 1000 that's one round a second. At 20, it's a round about every 100 ms: about 10 times a second.

**Make the changes.**

1. Near the top, change `local LOOP_DELAY_MS = 1000` to **20**.
2. In the block, replace the five `gcs:send_text` lines with four named values, `ADC0` to `ADC3`, one for each channel.
3. Delete the `write_to_file()` line, and the counting lines down to and including `end -- Stops logging after set number of readings`.
4. Save it, copy it onto the Cube over the old one, and reboot.
5. Check the Messages tab: after `ADS1115 detected successfully`, the lines of readings have stopped, and there's no error.

!!! warning "Careful"

    Lua needs every `if` closed by its `end`. Delete `if count >= READINGS_COUNT then` and its `end` together: leave one behind, and the script stops with an error in the Messages tab naming the line.

??? note "Check your version"

    The block should now read:

    ```lua
                if current_channel >= 4 then -- Do this if all 4 channels have been read
                    gcs:send_named_float("ADC0", voltage_readings[1]) -- mV
                    gcs:send_named_float("ADC1", voltage_readings[2])
                    gcs:send_named_float("ADC2", voltage_readings[3])
                    gcs:send_named_float("ADC3", voltage_readings[4])
                    current_channel = 0 -- Resets for next cycle
                    return update, LOOP_DELAY_MS -- Reschedules with full loop delay
    ```

### 4. See it in CubeGUI

1. In your settings file, under `"plots"`, add: `{"panel": "plotPanel", "signal": "ADC0", "label": "Flap sensor (mV)"}`
2. Under `"logging"`, add `"ADC0"` to `"extraSignals"`.
3. Start CubeGUI, connect, and turn the potentiometer by hand: the plot should follow.

!!! note "Why this works"

    CubeGUI shows any named value a script sends, by its name ([recipe 2](https://github.com/AVDASI2/CubeGUI/blob/main/docs/recipes.md#recipe-2-plot-a-value-from-a-lua-script)). Nothing arriving? Look in the Setup tab, under "Values from Lua scripts".

!!! tip "Look at the noise"

    With nothing moving, how much does the plot wobble? That's the smallest change you can trust.

### 5. Fit it to your model

There's no single right place for the sensor: it depends on your design. Before you fix it, think it through:

* **Do you want the flap's angle, or how far the servo has turned?** Anything between the two (slack, flex, the linkage, air load) makes them differ.
* **How does your sensor's movement relate to the flap's?** One for one, scaled, or not in a straight line? Your calibration will need to capture it.
* **What between the sensor and the flap could slip, bend or wear?**
* **Can the flap ever push the sensor past the end of its travel?**
* **Where will the wires run, and can you get at it later?**

Note where you put it, and why. The [Sensors](../sensors.md) page has more on choosing and fitting sensors.

!!! warning "Careful"

    If the flap pushes the potentiometer past the end of its travel, it can break or slip on its shaft. A slipped sensor still gives readings, but they're wrong.

### 6. Calibrate it: mV to degrees

**What we want.** CubeGUI showing the flap's angle in degrees, not mV. If the readings lie on a straight line against angle, two numbers turn one into the other: the reading at 0°, and the degrees per mV. Then: angle = (reading − reading at 0°) × degrees per mV.

1. Set the flap to several angles across its travel. Measure each with a protractor or inclinometer, and write down `ADC0` (in the Setup tab) at each.
2. Plot mV against angle, and fit a straight line, to get your two numbers.
3. In `flap_adc.lua`, under the `ADC0` line, add these, with your two numbers:

    ```lua
                    -- Your numbers, from your calibration
                    local FLAP_MV_AT_ZERO = 2500   -- mV at 0 deg
                    local FLAP_DEG_PER_MV = 0.06   -- deg per mV
                    gcs:send_named_float("FLAP_DEG", (voltage_readings[1] - FLAP_MV_AT_ZERO) * FLAP_DEG_PER_MV)
    ```

4. Copy it onto the Cube and reboot. Check `FLAP_DEG` against your protractor at two angles.

!!! note "Why keep ADC0 as well"

    If your calibration turns out wrong, the raw readings are still in the log, and you can work the angles out again.

!!! warning "Careful"

    Approach each angle from above and from below. If the readings differ, that's hysteresis, in the linkage or the sensor. If the points don't lie on a straight line, use more of them, or a curve. Calibrate again after any change to the mounting.

### 7. Compare what was asked with what happened

1. Calibrate the flap's servo, so its slider works in degrees ([recipe 5](https://github.com/AVDASI2/CubeGUI/blob/main/docs/recipes.md#recipe-5-work-in-degrees-instead-of-pwm)). If it isn't in your settings file yet, add it first ([recipe 4](https://github.com/AVDASI2/CubeGUI/blob/main/docs/recipes.md#recipe-4-add-a-servo)), named `Flap`.
2. Replace the `ADC0` plot with: `{"panel": "plotPanel", "signal": "Flap", "compare": "FLAP_DEG", "label": "Flap: asked (solid), measured (dashed)"}`
3. Add `"FLAP_DEG"` to `"extraSignals"`, start CubeGUI, and move the flap with its slider: the dashed line should follow the solid one.

!!! note "What the gap means"

    Whatever lies between the servo and your sensor. Measuring that gap is what the sensor is for.

## B. If your sensor only says yes or no: is the gear down?

A limit switch is either open or closed, so it doesn't need an ADC. One of the Cube's spare output pins can read it directly, as a digital input (GPIO), which keeps the ADC board's channels for sensors that need them.

The set-up: a microswitch on the bench, wired to **AUX OUT 6**. At the end, CubeGUI shows `GEAR_DN`: 1 while the switch is pressed (the gear is down), 0 when it isn't. As in Part A, you get it working on the bench before fitting it.

### 1. Wire it

1. Connect the switch's **common** terminal to AUX OUT 6's **signal** pin (the bottom row).
2. Connect its **normally open** terminal to AUX OUT 6's **−** pin (ground).
3. Leave AUX OUT 6's **+** pin unconnected.

!!! warning "Careful"

    The + pin carries the UBEC's 5 V. The switch needs only signal and ground.

!!! note "Why normally open"

    The switch then connects only while it's pressed. A broken wire reads "not pressed", so "not down": wrong, but the safe way round.

### 2. Turn AUX OUT 6 into an input

1. In CubeGUI's Setup tab, type `SERVO14_FUNCTION` in **Add parameter**, set it to **-1**, and click **Apply changes...**.
2. Reboot the Cube.

!!! note "Why SERVO14"

    AUX OUT 1 to 6 are the Cube's `SERVO9` to `SERVO14`. A function of -1 stops it being a servo output, so a script can read it as an input (GPIO pin 55).

### 3. Write the script

**What we want.** `GEAR_DN` sent to CubeGUI about 10 times a second: 1 while the switch is pressed, 0 when it isn't. The script does four things.

**Set the pin up as an input.** AUX OUT 6 is GPIO pin 55. With nothing connected, an input pin "floats" and reads at random, so the script turns on the chip's own pull-up resistor. That holds the pin high, until the closed switch connects it to ground:

```lua
local PIN = 55              -- AUX OUT 1 to 6 are GPIO pins 50 to 55
local INPUT_PULLUP = 32     -- input, with the chip's own pull-up resistor
gpio:pinMode(PIN, 0)        -- 0 = input
gpio:setPinFullMode(PIN, INPUT_PULLUP)
```

**Read it.** `gpio:read(PIN)` is `true` while the pin is high (switch open) and `false` while it's low (switch pressed). `not` turns that round, so pressed gives 1:

```lua
local now = (not gpio:read(PIN)) and 1 or 0
```

**Wait for three readings in a row.** A switch can chatter as it closes, or under vibration in the tunnel. Counting a change only once three readings agree (0.3 s) stops a flicker looking like a fault:

```lua
if now == candidate then
  count = count + 1
else
  candidate, count = now, 1
end
if count >= AGREE then
  reported = candidate
end
```

**Send it, and go round again.** The same `gcs:send_named_float` as in Part A, then wait 100 ms:

```lua
gcs:send_named_float("GEAR_DN", reported)
return update, 100
```

**Make the file.**

1. Put those pieces together in a new file called `gear_switch.lua`: the set-up at the top, then an `update()` function that reads, waits for agreement, sends and repeats. Add a line that says it has started, so you can see it in the Messages tab.
2. Put it on the Cube in `APM/scripts`, beside your other scripts, and reboot.
3. Check the Messages tab says it has started, with no error.

??? note "Check your version"

    The whole file:

    ```lua
    -- Gear-down limit switch on AUX OUT 6, read as a digital input.
    -- Needs SERVO14_FUNCTION = -1 (AUX OUT 6 as GPIO), then a reboot.
    local PIN = 55              -- AUX OUT 1 to 6 are GPIO pins 50 to 55
    local INPUT_PULLUP = 32     -- input, with the chip's own pull-up resistor
    local AGREE = 3             -- readings in a row before a change counts
    gpio:pinMode(PIN, 0)        -- 0 = input
    gpio:setPinFullMode(PIN, INPUT_PULLUP)
    gcs:send_text(6, "gear_switch.lua: started")

    local reported, candidate, count = 0, 0, 0
    function update()
      -- Open switch: the pull-up reads high. Pressed: grounded, reads low.
      local now = (not gpio:read(PIN)) and 1 or 0
      if now == candidate then
        count = count + 1
      else
        candidate, count = now, 1
      end
      if count >= AGREE then
        reported = candidate      -- only once three readings agree
      end
      gcs:send_named_float("GEAR_DN", reported)   -- 10 characters max
      return update, 100                           -- 10 times a second
    end

    return update()
    ```

!!! warning "Careful on Windows"

    The file must end in `.lua`, not `.lua.txt` (turn on file name extensions in File Explorer). Copy the file itself, never by pasting it through an email, which can join its lines into one long comment that does nothing.

### 4. See it in CubeGUI

1. In your settings file, under `"controls"`, add: `{"panel": "valuePanel", "signal": "GEAR_DN", "label": "Gear down (1 = yes)"}`
2. Add `"GEAR_DN"` to `"extraSignals"`, so it's logged.
3. Start CubeGUI and connect. Press the switch by hand: the value should go to 1, and back to 0 when you let go.

!!! tip "No switch yet?"

    Touch a wire between AUX OUT 6's signal and − pins instead: the same 1, then 0.

!!! tip "Going further"

    [Recipe 7](https://github.com/AVDASI2/CubeGUI/blob/main/docs/recipes.md#recipe-7-make-a-panel-that-keeps-itself-up-to-date) has a gear panel that guesses the gear's position from how long it takes to move. In your copy of it, read the switch with `down = cube.latest("GEAR_DN");` and turn the lamp red if the gear was asked to go down, its travel time has passed, and `down` still isn't 1. That turns a guess into a confirmation.

### 5. Fit it to your model, and prove it

Where the switch goes is your design. Before you fix it, think it through:

* **What does "down" mean for your gear?** Fully extended, locked, or within a few degrees? The switch can only tell you about the point where it trips.
* **How will you set that point?** A switch trips a little before the end of its own travel, and the exact point varies from switch to switch.
* **Can the gear push the switch too far,** and crush it at the end of its travel?
* **Where will the wires run, and can you get at it later?**

Once it's fitted:

1. **Find where it trips:** move the gear slowly, and measure where `GEAR_DN` changes, going down and coming up.
2. **Check it repeats:** put the gear down 20 times. It should confirm every time, and never when it shouldn't.
3. **Check the faults:** unplug the switch's wire, then hold the gear just short of down. Both should read 0.

!!! tip "You could also"

    Get a yes or no from a potentiometer, with a trip point in the script (on at 35°, off below 33°, so it doesn't flicker at the edge), or from a switch on a spare ADC channel. A potentiometer tells you the angle too, but a slipped shaft gives a confident wrong answer. A switch tells you less, but is harder to fool.

## How certain are you?

A number on a plot isn't proof. Before you rely on a sensor, be able to answer:

* **What does it actually measure?** The surface, or something attached to it that could slip or bend?
* **How small a change can it see?** Resolution, and noise (Part A, step 4).
* **How well does it repeat?** Go to the same angle several times, from both sides.
* **Does it keep up?** Move the flap quickly: does the reading trail behind? At about 10 readings a second, a fast movement can happen between two of them.
* **What does a fault look like?** A loose wire, a slipped shaft, a dead board. Would you notice, or would it look like a real reading?
* **Is the calibration still right?** When did you last check it?
* **For a switch: where exactly does it trip?** Measured both ways, and checked again after the mounting is touched.

!!! info "This is a new page"

    These examples haven't been tested widely yet. If something doesn't work, or isn't clear, message Robin Carter on Teams.
