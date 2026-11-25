# Things to change in the next big overhaul

Not published: only files under `docs/` and listed in `publish.yaml` reach the site. (This repository is public on GitHub, so this file can be read there.)

This file collects changes we've decided to leave for a whole-site overhaul, rather than make piecemeal: pages that now disagree, structure to rethink, and loose ends. Add to it whenever something is spotted; strike items through when done. Newest first within each section.

## Pages that disagree

| Added | Where | What disagrees | Leaning |
|---|---|---|---|
| 2026-11-25 | Sensors (`avionics/sensors.md`) vs 09 Sensors: Worked Examples | Sensors says "begin with the internal ADC, as I2C compatibility can be tricky". 09 makes the I²C board with an external ADC the main route ("recommended"), with the Cube's ADC second. | Bring Sensors in line with 09 |
| 2026-11-25 | Sensors, "Built-in ADC" | Points to an example script "in the '06. Lua Scripts' page"; the ADC example is on 11 ADC. | Fix the reference, or merge the section into 11 |
| 2026-11-25 | Sensors, "I2C" | Ends "More to follow here too..." with two bare links. | Point to 10 I2C and 09 |
| 2026-11-25 | More (`98-more.md`), "Initial Steps Cheat Sheet" | Its RC binding steps ("plane, 1 channel aileron flap elevator and rudder", "Click register then click bind") differ from 08 RC (no flaps; choose RX1/RX2/RX3 before Bind appears). | Make the cheat sheet a summary that links to the full pages |

## Structure and order

| Added | Idea | Notes |
|---|---|---|
| 2026-11-25 | Separate step-by-step tracks: Mission Planner, and CubeGUI? | Today one sequence mixes both: 05 servos via Mission Planner, 07 CubeGUI, 08 RC hands over to CubeGUI, 09 sensors in CubeGUI. |
| 2026-11-25 | Where the Cube's ADC page belongs | Now 11, after I2C, as the second route. Could move to an "additional information" section, or merge with the Sensors page's "Built-in ADC". |
| 2026-11-25 | Data Logging (12) is hidden | Decide whether it's wanted. CubeGUI's own docs point to it. |
| 2026-11-25 | Unlisted pages: `06c-other-lua-scripts.md`, `08-pymavlink.md` | Reachable only by link, or not at all. PyMAVLink's page links to `cube.md` and `examplecode.md#gs-py`, which don't exist (the only broken links left in the build). |
| 2026-11-25 | Numbering rule | A plain number is a main step, a letter an extra on that step (06/06a, 08/08a). Keep to it when pages are added. |

## Loose ends

| Added | What |
|---|---|
| 2026-11-25 | 08a Mode Switch Script has two "Video:" boxes ("Setup walkthrough", "Code walkthrough") with no videos. |
| 2026-11-25 | The repository's `.venv` is Python 3.10, too old for `scripts/build_live.py` (needs `tomllib`, Python 3.11+). |
| 2026-11-25 | `assets/controller.jpg` and `assets/Transmitter.jpg` belonged to the old RC page (Taranis X9 Lite, Archer R6) and are no longer used. |
