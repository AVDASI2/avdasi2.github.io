---
icon: material/target
---

# Closed Loop: holding the pitch

In closed loop, the Cube moves the elevator by itself, to hold a pitch angle set in CubeGUI. This is CubeGUI's level 3.

This page gets it working on the bench, before anything is assembled. By the end, tilting the Cube moves the elevator servo, and you can change the controller's gains from CubeGUI. Choosing the gains for your model, and testing them, is then part of your own design work.

!!! danger "Not for flight"

    Everything here is for a model held on a bench or wind-tunnel rig. The closed loop is not a flight controller, and must not be used on anything that flies.

!!! info "Before you start"

    * CubeGUI at level 2, with `cubegui.lua` running: **Who's in charge** says "Script running" ([CubeGUI](07-cubegui.md), and [RC](08-rc.md) step 6)
    * A servo on MAIN OUT 5, standing in for the elevator
    * The transmitter's mode switch set up ([RC](08-rc.md))

## What the closed loop is

This is not the stabilisation on the [Mode switch](08a-mode-switch.md) page. There, the SAS switch put ArduPilot into one of its own flight modes, such as STABILIZE or FBWA, run by ArduPilot's own controller. Here, `cubegui.lua` runs a simpler controller of its own: a PID controller, whose gains you can change from CubeGUI while it runs.

50 times a second, it compares the pitch the Cube measures with the target, and moves the elevator from its trim position by the sum of three terms:

* **P (proportional):** a push in proportion to the error, the gap between the target and the pitch. Gain `CGUI_KP`.
* **I (integral):** builds up while an error remains, to close a gap that P leaves. Gain `CGUI_KI`, limited by `CGUI_IMAX`.
* **D (derivative):** pushes against how fast the pitch is changing, to damp the motion. Gain `CGUI_KD`.

The gains are in microseconds of servo PWM: `CGUI_KP` = 10 means 10 µs for each degree of error. PID control is very widely used, so there's plenty to read on it, and on tuning one.

The script's SAS, used in RC mode, is separate again: a single damping gain, `CGUI_SAS_KD`, in the Setup tab.

## 1. Open CubeGUI at level 3

1. In your settings file (`config/cubegui.json`, unless you've made your own), set `"level"` to `3`, and save it.
2. Run `CubeGUI`, and connect to the Cube.
3. The title now says level 3. **Who's in charge** has two buttons, **CubeGUI drives** and **Closed loop**, and a **pitch target** slider. A new box, **Closed-loop gains (on the Cube)**, shows the three gains.

!!! note "Why the settings file?"

    `CubeGUI(Level=3)` works too, but only for that window. With `"level": 3` in the settings file, `CubeGUI` opens at level 3 every time.

## 2. Turn the loop on, and tilt the Cube

1. Tilt the Cube nose-up. The pitch plot should go positive: that tells you which way is the nose.
2. Put the mode switch **high**, and the pitch target at **0**.
3. Click **Closed loop**. **Who's in charge** turns amber.
4. Tilt the Cube nose-down, then nose-up, and watch the servo.

Which way should the elevator move to bring the nose back? Check the servo moves that way.

!!! warning "Careful: if it moves the other way"

    The loop would push the nose further from the target. Click **CubeGUI drives**, set `SERVO5_REVERSED` to **1** in the Setup tab, and try again. This also reverses the elevator stick in RC mode.

## 3. Change a gain

1. Hold the Cube a few degrees nose-down, and watch the servo for a few seconds.
2. In the gains box, change one gain, click **Apply...** and confirm. The loop uses it straight away.
3. Tilt the Cube again. What changed?

Try each gain on its own, including setting it to 0. Which one keeps the servo creeping while you hold the Cube still?

## 4. Check the ways out

**The transmitter.** With the loop on, put the mode switch **low**. The sticks take over at once.

!!! warning "Careful: switching back to high goes back into the loop"

    CubeGUI is still asking for the closed loop. If you don't want that, click **CubeGUI drives** first.

**Losing CubeGUI.** With the loop on, click **Disconnect**. After about 3 seconds, the script holds the servo still: tilt the Cube to check. When you connect again, check **Who's in charge** before carrying on.

## Where next

The loop works on the bench. On your model, the target, the gains, and how you test them are your decisions. Two records help:

* **The Cube's own log** has a `CGUI` entry 10 times a second: the target, the pitch, and the P, I and D terms separately. CubeGUI's [guide to the Cube's log](https://github.com/AVDASI2/CubeGUI/blob/main/docs/flight-log.md) shows how to download and read it.
* **CubeGUI's CSV log** can include the target too: add `CG_TGT` to `extraSignals` in your settings file (see [config/README.md](https://github.com/AVDASI2/CubeGUI/blob/main/config/README.md)).

## Troubleshooting

* **No Closed loop button:** CubeGUI isn't at level 3 (step 1).
* **Closed loop does nothing, and Who's in charge says "Transmitter (RC)":** the mode switch is low.
* **The gains say "Not on this Cube":** `cubegui.lua` isn't running. See [RC](08-rc.md) step 6.
* **"Held: lost CubeGUI" in red:** the Cube hasn't heard CubeGUI for 3 seconds. Check the connection.

!!! info "This is a new page"

    If something doesn't work as it says, or isn't clear, message Robin Carter on Teams.
