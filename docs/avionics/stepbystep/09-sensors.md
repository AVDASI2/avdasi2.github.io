---
icon: material/gauge
---

# Sensors: worked examples

Your closed loop works from what the Cube itself measures, such as its pitch and the PWM it sends. An external sensor gives you an **independent check**: something outside the loop that tells you, for example, the landing gear is deployed. This external validation is critical to both: confirming expected behaviour during live operation, and for reference during reflective activity, such as your reports.

This page brings together the pieces you need, on other pages, and walks through **two worked examples** from sensor to plot: a flap's angle, and whether the landing gear is down.

!!! note "This is a starting point, not a finished product"

    The examples show one way of doing it, so you can see every step working. They aren't the answer. Decide what *your* model needs to confirm, which sensor and input suit it, and how you'll know you can trust the reading. Use the examples to learn, then build your own.

!!! info "A new page"

    These examples haven't been tested widely yet. If something doesn't work, or isn't clear, message Robin Carter on Teams.

## How the pieces fit

A reading goes through four stages:

1. **A sensor** turns position into a voltage, or a switch into on and off.
2. **An analog-to-digital converter (ADC)** turns the voltage into a number: either the 16-bit I²C ADC board in your kit, or the Cube's own ADC port.
3. **A Lua script on the Cube** reads that number and sends it to the ground station as a *named value*.
4. **CubeGUI** shows it, plots it and logs it. The Cube's own log records it too.

| To do this | Go to |
|---|---|
| Choose a sensor, and think through fitting it | [Sensors](../sensors.md) |
| Wire it to the I²C ADC board, and use the example script (recommended) | [10. I2C](10-i2c.md) |
| Wire it to the Cube's own ADC | [11. ADC](11-adc.md) |
| Read an on/off switch on a spare output pin, with no ADC | [Part B](#b-if-your-sensor-only-says-yes-or-no-is-the-gear-down), below |
| Get a Lua script onto the Cube | [06. Servos via Lua Script](06-lua-servo.md) |
| Show, plot and log the value in CubeGUI | [CubeGUI recipes](https://github.com/AVDASI2/CubeGUI/blob/main/docs/recipes.md) 1, 2, 3 and 7 |

## A. Is the flap where we expect?

The set-up: a potentiometer at the flap's hinge, wired to channel 0 of the I²C ADC board, read by a script you build from the ADS1115 example on [10. I2C](10-i2c.md). At the end, CubeGUI plots the flap's measured angle against the angle it was asked for.

### 1. Fit the sensor

1. Mount the potentiometer at the flap's hinge, so that it turns with the flap. [Sensors](../sensors.md) has the options.
2. Move the flap through its full travel by hand, and check the potentiometer never reaches its own end stop.

!!! note "Why at the hinge"

    A sensor on the servo only tells you what the servo did. One on the flap catches slack, flex and air load between the two, which is the point.

!!! warning "Careful"

    A potentiometer forced past its travel breaks, or slips on its shaft. A sensor that slips still gives a sensible-looking number: just the wrong one.

### 2. Wire it to the I²C ADC board

1. Connect the board to the Cube, as on [10. I2C](10-i2c.md).
2. Connect the potentiometer's outer pins to the board's supply and ground, and its middle pin (the wiper) to **channel 0**.

!!! warning "Careful"

    Never put more on an input than the board's supply voltage. The board can't measure it, and may be damaged.

### 3. Run the example script unchanged first

1. Copy the ADS1115 script from [10. I2C](10-i2c.md) into a new file called `flap_adc.lua`.
2. Put it on the Cube in `APM/scripts`, as on [06. Servos via Lua Script](06-lua-servo.md), and reboot.
3. In Mission Planner's Messages tab, check you see `ADS1115 detected successfully`, then a line of four readings in mV every second.
4. Move the flap by hand: the first of the four numbers (channel 0) should change.

!!! note "Why unchanged first"

    If it works now and breaks later, the fault is in the change you made, not in the wiring.

!!! warning "Careful"

    `ADS1115 not detected on I2C bus!` means the Cube can't find the board: check the wiring, and the board's address switch (the script expects 0x48).

### 4. Change it to send named values

1. Open `flap_adc.lua`. Near the top, find `local LOOP_DELAY_MS = 1000` and change **1000** to **20**.
2. Find the line that starts `if current_channel >= 4 then`. Select it, and every line under it down to the line just above `else`. That `else` is followed by `return update, 10 -- Continues reading next channel`, and stays.
3. Replace the selected lines with these:

    ```lua
                if current_channel >= 4 then -- All 4 channels have been read
                    -- Named values: CubeGUI shows, plots and logs them, and the
                    -- Cube's own log records them too (as NVF messages).
                    -- Names are at most 10 characters; longer ones are cut short.
                    gcs:send_named_float("ADC0", voltage_readings[1]) -- mV
                    gcs:send_named_float("ADC1", voltage_readings[2])
                    gcs:send_named_float("ADC2", voltage_readings[3])
                    gcs:send_named_float("ADC3", voltage_readings[4])
                    current_channel = 0 -- Back to channel 0, and keep going
                    return update, LOOP_DELAY_MS
    ```

4. Save it, copy it onto the Cube over the old one, and reboot.
5. Check the Messages tab: after `ADS1115 detected successfully`, the lines of readings have stopped.

!!! note "What changed, and why"

    Text once a second becomes named values about 10 times a second (reading all four channels takes about 80 ms), which CubeGUI can plot. The text lines are gone because ten a second would flood the Messages tab. The script no longer stops after 60 readings. It no longer writes to its CSV file either: CubeGUI's log and the Cube's own log both record named values. The readings stay in mV: you convert to degrees in step 6, so the raw data survives a wrong calibration.

!!! warning "Careful"

    Lua doesn't care about indentation, but it does need every `if` closed by its `end`. Replace exactly the lines in step 2: one line too many or too few, and the script stops with an error in the Messages tab naming the line.

### 5. See it in CubeGUI

1. In your settings file, under `"plots"`, add: `{"panel": "plotPanel", "signal": "ADC0", "label": "Flap sensor (mV)"}`
2. Under `"logging"`, add `"ADC0"` to `"extraSignals"`.
3. Start CubeGUI, connect, and move the flap by hand: the plot should follow.

!!! note "Why this works"

    CubeGUI shows any named value a script sends, by its name ([recipe 2](https://github.com/AVDASI2/CubeGUI/blob/main/docs/recipes.md#recipe-2-plot-a-value-from-a-lua-script)). Nothing arriving? Look in the Setup tab, under "Values from Lua scripts".

!!! tip "Look at the noise"

    With nothing moving, how much does the plot wobble? That's the smallest change you can trust.

### 6. Calibrate it: mV to degrees

1. Set the flap to several angles across its travel. Measure each with a protractor or inclinometer, and write down `ADC0` (in the Setup tab) at each.
2. Plot mV against angle, and fit a straight line: the mV at 0°, and the degrees per mV.
3. In `flap_adc.lua`, under the `gcs:send_named_float("ADC0", …)` line, add these, with your two numbers:

    ```lua
                    -- Your numbers, from your calibration
                    local FLAP_MV_AT_ZERO = 2500   -- mV at 0 deg
                    local FLAP_DEG_PER_MV = 0.06   -- deg per mV
                    gcs:send_named_float("FLAP_DEG", (voltage_readings[1] - FLAP_MV_AT_ZERO) * FLAP_DEG_PER_MV)
    ```

4. Copy it onto the Cube and reboot. Check `FLAP_DEG` against your protractor at two angles.

!!! warning "Careful"

    Approach each angle from above and from below. If the readings differ, that's hysteresis, in the linkage or the sensor. If the points don't lie on a straight line, use more of them, or a curve. Calibrate again after any change to the mounting.

### 7. Compare what was asked with what happened

1. Calibrate the flap's servo, so its slider works in degrees ([recipe 5](https://github.com/AVDASI2/CubeGUI/blob/main/docs/recipes.md#recipe-5-work-in-degrees-instead-of-pwm)). If it isn't in your settings file yet, add it first ([recipe 4](https://github.com/AVDASI2/CubeGUI/blob/main/docs/recipes.md#recipe-4-add-a-servo)), named `Flap`.
2. Replace the `ADC0` plot with: `{"panel": "plotPanel", "signal": "Flap", "compare": "FLAP_DEG", "label": "Flap: asked (solid), measured (dashed)"}`
3. Add `"FLAP_DEG"` to `"extraSignals"`, start CubeGUI, and move the flap with its slider: the dashed line should follow the solid one.

!!! note "What the gap means"

    Slack, flex, the servo not reaching its target, and in the tunnel, air load. Measuring that gap is what the sensor is for.

## B. If your sensor only says yes or no: is the gear down?

A limit switch is either open or closed, so it doesn't need an ADC. One of the Cube's spare output pins can read it directly, as a digital input (GPIO), which keeps the ADC board's channels for sensors that need them.

The set-up: a microswitch that closes when the landing gear is fully down, wired to **AUX OUT 6**. At the end, CubeGUI shows `GEAR_DN`: 1 when the gear is down, 0 when it isn't.

### 1. Fit the switch

1. Decide what "down" means for your gear: fully extended, locked, or within a few degrees.
2. Mount the switch on slotted holes, so the gear leg presses its lever at exactly that point.
3. Move the gear down by hand, and check the leg doesn't crush the switch at the end of its travel.

!!! note "Which switch"

    A small microswitch with a lever suits a gear leg: the leg presses the lever as it comes down.

!!! note "Why slotted holes"

    A switch trips a little before the end of its own travel, and the exact point varies from switch to switch. Slots let you move it until it trips where you decided.

### 2. Wire it

1. Connect the switch's **common** terminal to AUX OUT 6's **signal** pin (the bottom row).
2. Connect its **normally open** terminal to AUX OUT 6's **−** pin (ground).
3. Leave AUX OUT 6's **+** pin unconnected.

!!! warning "Careful"

    The + pin carries the UBEC's 5 V. The switch needs only signal and ground.

!!! note "Why this way round"

    With the switch closed only when the gear is down, a broken wire reads "not down": wrong, but the safe way round.

### 3. Turn AUX OUT 6 into an input

1. In CubeGUI's Setup tab, type `SERVO14_FUNCTION` in **Add parameter**, set it to **-1**, and click **Apply changes...**.
2. Reboot the Cube.

!!! note "Why SERVO14"

    AUX OUT 1 to 6 are the Cube's `SERVO9` to `SERVO14`. A function of -1 stops it being a servo output, so a script can read it as an input (GPIO pin 55).

### 4. Add the script

1. Make a new file called `gear_switch.lua`, containing exactly this:

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
      -- Open switch: the pull-up reads high. Closed (gear down): grounded, reads low.
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

2. Put it on the Cube in `APM/scripts`, beside your other scripts, and reboot.
3. Check the Messages tab shows `gear_switch.lua: started`.

!!! warning "Careful on Windows"

    The file must end in `.lua`, not `.lua.txt` (turn on file name extensions in File Explorer). Copy the file itself, never by pasting it through an email, which can join its lines into one long comment that does nothing.

!!! note "Why wait for three readings"

    A switch can chatter as it closes, or under vibration in the tunnel. Counting a change only once three readings agree (0.3 s) stops a flicker looking like a fault.

### 5. See it in CubeGUI, and use it

1. In your settings file, under `"controls"`, add: `{"panel": "valuePanel", "signal": "GEAR_DN", "label": "Gear down (1 = yes)"}`
2. Add `"GEAR_DN"` to `"extraSignals"`, so it's logged.
3. Start CubeGUI and connect. Move the gear down and up by hand: the value should go to 1 and back to 0.

!!! tip "Going further"

    [Recipe 7](https://github.com/AVDASI2/CubeGUI/blob/main/docs/recipes.md#recipe-7-make-a-panel-that-keeps-itself-up-to-date) has a gear panel that guesses the gear's position from how long it takes to move. In your copy of it, read the switch with `down = cube.latest("GEAR_DN");` and turn the lamp red if the gear was asked to go down, its travel time has passed, and `down` still isn't 1. That turns a guess into a confirmation.

### 6. Prove it

1. **Before fitting the switch:** touch a wire between AUX OUT 6's signal and − pins. `GEAR_DN` should go to 1, and back to 0 when you take it away.
2. **Find where it trips:** move the gear slowly, and measure where `GEAR_DN` changes, going down and coming up.
3. **Check it repeats:** put the gear down 20 times. It should confirm every time, and never when it shouldn't.
4. **Check the faults:** unplug the switch's wire, then hold the gear just short of down. Both should read 0.

!!! tip "You could also"

    Get a yes or no from a potentiometer, with a trip point in the script (on at 35°, off below 33°, so it doesn't flicker at the edge), or from a switch on a spare ADC channel. A potentiometer tells you the angle too, but a slipped shaft gives a confident wrong answer. A switch tells you less, but is harder to fool.

## How certain are you?

A number on a plot isn't proof. Before you rely on a sensor, be able to answer:

* **What does it actually measure?** The surface, or something attached to it that could slip or bend?
* **How small a change can it see?** Resolution, and noise (Part A, step 5).
* **How well does it repeat?** Go to the same angle several times, from both sides.
* **How fast is it?** Moving the surface quickly: does the measured line lag the asked one?
* **What does a fault look like?** A loose wire, a slipped shaft, a dead board. Would you notice, or would it look like a real reading?
* **Is the calibration still right?** When did you last check it?
* **For a switch: where exactly does it trip?** Measured both ways, and checked again after the mounting is touched.
* **Is it really independent?** It's outside the control loop, but it still runs through the Cube and a Lua script: if the Cube stops, so does the check.

## Now your own

The examples confirm a flap's angle and the gear's position. Decide what your model needs to confirm, then choose your sensors, inputs, names, rates, calibration and checks to suit. Keep a note of what you decided and why: it belongs in your report.

!!! warning "A check, not a control"

    Nothing here moves a servo. CubeGUI and the example scripts only show, plot and log the readings. If you want a reading to *act*, for example to stop a servo at a limit, talk to us first.
