# Open issues: Avionics step-by-step guide

For Tim, ahead of kit issue on **Friday 25 September, 09:00–11:00**.

These came out of a review of every page of the step-by-step guide on 19 September, checked against the ArduPilot and CubePilot documentation and against the kit spreadsheet. Some have been settled since; those are marked so nobody redoes them. **Nothing here has been bench-tested on a real kit** — that is the single most useful thing anyone could do before Friday, and it is section 4 below.

Anything marked **needs Tim** is a question about the kit that only you can answer. If you only have half an hour, do section 1 and the **needs Tim** rows.

| Status | Meaning |
|---|---|
| **Open** | Not done, still needs someone |
| **Settled** | Decided; the guide already says so |
| **Assumed** | We have proceeded on an assumption that has not been confirmed |

---

## 1. Must fix before Friday

| # | Page | Issue | Status |
|---|---|---|---|
| B1 | 02 → 05 | Step 02 has students flash Sub then Plane as a factory reset, which wipes the accelerometer calibration. Step 05 then asks them to **arm**, and a pre-arm check should block that with "3D Accel calibration needed". The guide never mentions calibration. Either drop arming from step 05 (if the Servo/Relay tab can move AUX1 with safety off and not armed) or add a calibration step to 02 | **Open** — decided by the bench test, section 4 |
| B2 | 05 | "Set up the parameters for the servo you want to move" doesn't say which. AUX1 is `SERVO9`, and the Servo/Relay tab only moves an output whose `SERVO9_FUNCTION` is 0, 1, or 51–66; otherwise Mission Planner says "Channel x is already in use". The page should say exactly that, and name the error | **Open** |
| B3 | 03, 04 | The two pages contradict each other. 03 sets up Wi-Fi telemetry; 04 then says "don't do anything with telemetry yet", but 04's last line assumes 03 is done. Either drop "telemetry" from 04's warning or swap the two pages | **Open** |
| B4 | 03 | Every Kahuna ships with the same SSID, so in a room full of kits students would connect to, and rename, another group's board | **Settled 20 Sep** — students name their own board, one group at a time, with the kit number in the name. The page also now says the lab uses its own autonomous network, not eduroam |
| B5 | 02 | Mission Planner is Windows-only and the page only offers unsupported workarounds | **Settled 20 Sep** — one Windows laptop per group, installed before Friday, announced at the intro lecture. The Mac notes on page 02 still need collapsing into an aside |
| B6 | 00 | The Kit page said nothing actionable — no contents, no issue process, no locations | **Settled** — rewritten, with the kit list pulled out to its own page |
| B7 | 05 | The "small" and "large" servo links both point at the same product (DFRobot SER0047), so the "up to 4 A" figure has no source | **Open** — **needs Tim**, see K6 |
| B8 | 04 | The page never says what voltage the bench supply is, how it reaches the power module, or where the BEC's input comes from. These are the connections that damage hardware rather than merely confuse | **Open** — **needs Tim**. This is the most important one on the page |

## 2. Should fix

| # | Page | Issue |
|---|---|---|
| C1 | 02 | The Altitude Angel box is company history a student doesn't need. One line will do: if Mission Planner asks you to log in, skip it |
| C2 | 02 | The macOS dev-build note is a year old and needs rechecking before it says anything |
| C3 | 02 | "Factory reset by flashing Sub" is written as a throwaway aside, but the cheat sheet treats it as the standard procedure. Pick one |
| C4 | 06 | The Lua page stops after enabling scripting — no first script, no upload, no check that it ran. Wants a five-line `gcs:send_text` example over MAVFtp to `APM/scripts`, and a mention of `SCR_HEAP_SIZE` |
| C5 | 07 | Doesn't say the ADC input is **6.6 V max**. Worth a warning next to the pinout link |
| C6 | More, Sensors | The "Cubepilot ADC" and "Cubepilot I2C" links go to the **CubeNode**, a different product |
| C7 | 08 | Points at "Expert Links → CubePilot pinout", but that page is titled "Dump" |
| C8 | 08 | ArduPilot and CubePilot disagree on which GPS port carries which I²C bus. No change proposed, but the Lua bus numbers want confirming on a kit |
| C10 | `99-summary` (hidden) | Uses `SERVOn_OPTION` where it means `SERVOn_FUNCTION`; 4, 19 and 21 are function codes |
| C11 | `07-datalog`, `08-pymavlink` (hidden) | Link to `Data-Logging.md` and `cube.md`, which no longer exist |
| C12 | 08 | NXP's I²C spec link (UM10204) is a 404 |

C9 (which RC hardware the guide describes) is resolved by K5 below.

Already fixed in commit `a4ee413`: every CubePilot link had died when they reorganised their docs, a wrong parameter name on 02, three blocks of broken list formatting, a missing `lua` tag, and assorted typos.

## 3. Kit cross-check — **needs Tim**

Checked against `AVDASI2 Avionics kits.xlsx` from the 2025-26 folder, on the assumption the kit is unchanged for 2026-27. Please confirm that assumption first.

| # | Finding | What we need |
|---|---|---|
| K1 | **The kit list has no BEC**, but step 05 says to use "the provided BEC" to power the servo rail | **Assumed** the kits do include BECs and step 05 stands. Confirm the model and how the servo rail is actually powered |
| K2 | The older sheet lists an "AC-DC **5 V** 5 A" supply. The Power Brick Mini is a step-down regulator for battery inputs, so fed 5 V it cannot produce its regulated ~5.3 V output and the Cube may brown out. The print list only says "power supply with red and yellow XT60" | The supply voltage, and which XT60 goes where. This settles B8 |
| K3 | The Power Brick Mini connects through **POWER2**, but `99-summary` says POWER1 and step 04 names no port | Confirm, then name the port in 04 |
| K4 | The kit has the **ADS-B carrier board**, not the standard one. Pinouts match apart from the receiver | Confirm, so page 01 can name the board students actually see |
| K5 | RC issued is a **FrSky TW MX receiver** plus cable, transmitters held separately. That makes the hidden `06-rc` page (X9 Lite / Archer R6) out of date | Confirm, and say whether RC belongs in the minimum working example |
| K6 | The large servo is "Feetech FT6355M" in one sheet and "FeeTech Servo" in the other. Horns and metal mounts appear on the contents sheet but not the print list students sign | The model, for the stall-current figure (B7), and whether horns and mounts go on the print list |
| K7 | The ADC comes with a loose 10-pin header strip and a Dupont-to-JST cable. The guide never says whether the header needs soldering, or how the cable reaches `I2C2` | Who solders it, where, and the wiring |
| K8 | The 2025-26 prep sheet had outstanding jobs: heatshrink the RC receivers, adapt the RC cables, reprogram the transmitters, print laminated part lists, XT60 soldering | Confirm these are done for 2026-27 |
| K9 | 12 kits (16 in stock, 4 spare), roughly 30 students, so 2–3 per kit. Kits are numbered | Confirm the numbering, since the SSID naming in B4 relies on it |

## 4. The bench test

One kit, reset to the state a student would find it in, worked through from the published guide. Two parts, and the first is worth doing even if there is no time for the second.

**(a) The arming question — about ten minutes.** Can AUX1 be moved from the Servo/Relay tab with the safety off and **not** armed? Does arming fail after the Sub → Plane reset? And does an output with a function already assigned give "Channel x is already in use"? That answers B1 and B2, and B1 decides what the week 2 servo session has to contain.

**(b) The full run — about two hours.** Follow pages 00 to 05 exactly as written, timing each page, renaming the telemetry SSID as page 03 now describes, connecting over UDP, and noting every point where a student would have to guess. **Photograph the complete bench wiring** — that settles B8 and would improve the intro deck's system diagram, which is currently drawn from assumption rather than from the bench.

If neither happens, Friday's workshop becomes the bench test by default: one kit goes through 00–05 at the front before groups start. That is the fallback, not the plan. In that case the front-led section has to describe the bench wiring from the assumed setup, and must **say that it is an assumption** — a room about to wire up bench power should not be handed a guess as though it were a fact.

## 5. Proposed, not yet written

A **"How not to break it"** page, collecting warnings currently scattered across 01, 02, 04 and 05: the fragile micro-USB port and the USB/buzzer lead; not pulling the Cube off its carrier; laptop USB not being able to power servos; servo polarity; the ADC's 6.6 V limit and I²C's 3.3 V logic; pulling JST-GH plugs by the housing; and why we don't use LiPos. That gives Friday's front-led finish its content.

---

*Drafted with AI assistance from a review of the guide against vendor documentation and the kit spreadsheet. Everything above is a proposal to be checked, not a verified fact — particularly anything about what is in the kits.*
