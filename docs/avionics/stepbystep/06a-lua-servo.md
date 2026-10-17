# Lua servo walkthrough

<!-- TEMPLATE. Text is from your notes, verbatim apart from formatting.
     Every *[Placeholder: …]* is a gap your notes don't cover. Delete the
     comments and the notes box when the page is written. -->

<!-- in-progress:start -->
!!! abstract "Template notes: remove before publishing"

    * Arming – uncertain. The admonition below says no arming is necessary; the recap says to try arming if it doesn't work.
    * `STEST_CHAN` is "set to 1" in the steps but 5 in the recap and the example.
    * The steps say `SCR_ENABLE`; the recap says `SCR_ENABLED`.
    * The steps reboot before the script is mentioned; the recap uploads the script before rebooting.
    * The script's own default for `STEST_CHAN` is 0 (line 22), and it does nothing until the channel is above 0. `STEST_FREQ` defaults to 1, which matches "Watch 1 cycle".
    * The script is ArduPilot's own `servo_slew.lua` example, unchanged. It needs crediting, and ArduPilot's code is GPLv3.
    * **C4** (`ISSUES.md`): page 06 has no first script, no upload over MAVFtp to `APM/scripts`, and no mention of `SCR_HEAP_SIZE`. This page can close it.
<!-- in-progress:end -->

*[Placeholder: introduction. What this page gets you to, and that it follows on from the [Servos via Mission Planner](05-servos.md) and [Lua Scripts](06-lua.md).]*

<!-- Component: info admonition, as in 02-missionplanner.md -->
!!! info "NO ARMING IS NECESSARY"

    Toggle Safety Switch must be done in ++ctrl+f++ menu

## The script

*[Placeholder: where to get the script, and how to upload it.]*

<!-- The script lives once, in assets/, and is pulled in here with a
     snippets include, as examplecode.md does. It is ArduPilot's own example,
     unchanged: libraries/AP_Scripting/examples/servo_slew.lua -->
:material-download: [servo_slew.lua](assets/servo_slew.lua)

<!-- Suggested, not from your notes: credit the source.
* [:material-information:ArduPilot - servo_slew.lua example](https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_Scripting/examples/servo_slew.lua)
-->

```lua title="servo_slew.lua"
--8<-- "docs/avionics/stepbystep/assets/servo_slew.lua"
```

## Setting up

<!-- Component: numbered steps, as in 00-kit.md -->
1. `SCR_ENABLE` – set to 1
2. REBOOT
3. `STEST_CHAN` – set to 1 – this is the servo output number the script will use. Therefore, set this value to the MAIN OUT pins that the servo is connected to. i.e. MAIN OUT = 5, `SERVO5_FUNCTION` = 0, `STEST_CHAN` = 5.
4. **SETUP – MANDATORY HARDWARE – SERVO OUTPUT** – Watch 1 cycle between HIGH and LOW

*[Placeholder: screenshot of the Servo Output screen.]*

## Recap

<!-- Component: parameter table, as in 02-missionplanner.md -->
Parameters of concern:

| Parameter | Value | Description |
|---|---|---|
| `SERVO5_FUNCTION` | 0 | disabled |
| `SCR_ENABLED` | 1 | enables scripts |
| `STEST_CHAN` | 5 | script target channel |

1. Flash Sub
2. Flash Plane
3. `SERVO5_FUNCTION` = 0
4. `THR_FAILSAFE` = 0
5. `SCR_ENABLED` = 1
6. Upload Script
7. Write params
8. Reboot
9. `STEST_CHAN` = 5
10. Toggle Safety Switch
11. If not working, check SERVO OUTPUT, try ARMING

<!-- Component: closing line, as in 01-cube.md and 04-power.md -->
*[Placeholder: closing line, e.g. that the next page, [Lua servo script explained](06b-lua-servo-explained.md), goes through the script.]*
