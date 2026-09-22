---
marp: true
theme: flightlab
paginate: true
header: "AVDASI 2 · Avionics & Mechanisms"
footer: "Dr. Steve Bullock · Introduction"
title: "Avionics & Mechanisms: introduction"
description: "Introduction to the Avionics and Mechanisms strands of AVDASI 2, 2026-27."
author: "Dr. Steve Bullock"
---

<style>
/* Five-across team row: square portraits, name, then roles. */
.people { display: flex; gap: 1.1em; }
.people p { flex: 1; text-align: center; font-size: 0.74em; line-height: 1.3; margin: 0; }
.people img { width: 100%; border-radius: 6px; margin-bottom: 0.3em; }
.people strong { display: block; }

/* Compact table, for room lists and schedules that would otherwise overflow. */
.compact table { font-size: 0.72em; }
.compact td, .compact th { padding: 0.25em 0.5em; }

/* A row of photographs with captions underneath. */
.shots { display: flex; gap: 0.9em; align-items: flex-start; }
.shots p { flex: 1; text-align: center; font-size: 0.7em; line-height: 1.3; margin: 0; }
.shots img { width: 100%; max-height: 230px; object-fit: cover; border-radius: 4px; margin-bottom: 0.3em; }
.shots.small p { font-size: 0.64em; }
.shots.small img { max-height: 150px; object-fit: contain; }
/* Markdown puts the strip's three images in one paragraph, so lay that out. */
.strip p { display: flex; gap: 0.8em; margin: 0.5em 0 0; }
.strip img { width: 33%; max-height: 190px; object-fit: cover; border-radius: 4px; }

/* Video: live embed on screen, a linked still in the PDF. */
.realisation ul { display: grid; grid-template-columns: repeat(12, 1fr);
  gap: 0.5em 0.6em; margin-top: 0.5em; padding: 0; list-style: none; }
/* The list is what Marp fragments, so each card has to be a list item. */
.realisation li { display: flex; flex-wrap: wrap; justify-content: center;
  align-items: center; gap: 0.25em; margin: 0;
  border: 1px solid #d8d8dd; border-radius: 6px; padding: 0.4em 0.5em 0.5em; }
.realisation li::marker { content: ""; }
.realisation li:nth-child(-n+3) { grid-column: span 4; }
.realisation li:nth-child(n+4) { grid-column: span 3; }
.realisation strong { flex: 0 0 100%; text-align: center; font-size: 0.6em;
  line-height: 1.25; margin-bottom: 0.3em; color: #b01c2e; }
.realisation img { max-width: 100%; max-height: 124px; object-fit: contain; }
.realisation li:nth-child(n+4) img { max-height: 104px; }
.realisation li:nth-child(4) img { max-height: 44px; }
.realisation li:last-child img { max-height: 92px;
  border-top: 3px solid #00b050; }
.realisation li:last-child img:last-child { border-top-color: #b01c2e; }
@media print { .only-html { display: none !important; } }
@media screen { .only-print { display: none !important; } }
.only-html iframe { width: 100%; height: 420px; border: 0; }
.only-print img { width: 100%; }
</style>

<!-- _class: title -->

# Avionics & Mechanisms

## AVDASI 2 · Introduction

Dr. Steve Bullock

<!--
Full cohort, 1.40 Pugsley, 12:00-13:00.

HARD STOP 12:50. FDAC control lecture 1 is 13:00-15:00 in this room, and the
TSRs set the Quanser rig up during this hour. 25 minutes each half.

(That FDAC slot is two 50-minute lectures with a break, not one 110-minute
block, so if the rig setup needs longer there is a second break inside it to
borrow from. Steve's call, and not a reason to plan on overrunning here.)

Top-level bullets are fragmented - they appear one at a time on a click.
-->

---

# Today

**Who we are, and where things happen**

**Part 1 — Avionics**
What it does in your aircraft · what the requirements ask for · integration · the workshops, and how to get ready

**Part 2 — Mechanisms**
What has to move · the design task · where it meets avionics · the sessions

<div class="strip">

![](../../docs/assets/intro/tunnel-students.jpg)
![](../../docs/assets/intro/servos-installed.jpg)
![](../../docs/assets/intro/servo-micro.jpg)

</div>

---

# Who's who

<div class="people">

![](../../docs/assets/people/bullock.jpg)
**Steve Bullock**
Avionics
Mechanisms

![](../../docs/assets/people/burns.jpg)
**George Burns**
Avionics

![](../../docs/assets/people/ward.jpg)
**Tim Ward**
Avionics

![](../../docs/assets/people/carter.jpg)
**Robin Carter**
Avionics

![](../../docs/assets/people/graham.jpg)
**Mark Graham**
Mechanisms

![](../../docs/assets/people/maes.jpg)
**Vince Maes**
Mechanisms

</div>

<!--
CHECK BEFORE TUESDAY: the four supplied photographs were assigned in the order
they were sent - Burns, Ward, Graham, Maes. Swap the files in
docs/assets/people/ if any of them is wrong.

Robin Carter starts his PhD on 1 Oct and has flown these autopilots on the MSc
Aerial Robotics project - worth saying so when you introduce him.
-->

---

# Where things happen

<div class="compact">

| Space | Room | What for |
|---|---|---|
| **Stack Room** | [QB F.05](https://link.mazemap.com/gLLBFne1) | Avionics workshops, Friday mornings |
| **Avionics lab** | [QB M.003](https://link.mazemap.com/uXsLo5fv) | Kit issue and return, supervised tool use |
| **Design Suite** | [QB 1.59](https://link.mazemap.com/o5Xo8oWt) | Mechanisms sessions, Thursdays |
| **The Hangar** | [QB L.080](https://link.mazemap.com/2QMWAiXk) | Main lab, open access |
| **Here** | [QB PLT](https://link.mazemap.com/KkMVJJVS) | Pugsley Lecture Theatre |

</div>

Room numbers link to the map. All of these are in Queens Building.

<!--
MazeMap share links, also kept in teaching/rooms.md so other units can reuse
them. The Hangar (L.080) is in Queens Building too.
-->

---

# The model is only as good as what moves it

<div class="shots">

![](../../docs/assets/intro/tunnel-model.jpg)
Last year's fuselage in the 7×5 tunnel

![](../../docs/assets/intro/tunnel-students.jpg)
Photos: Ross Dewar

</div>

* Your model has **control surfaces**, and something has to move them repeatably
* Your test campaign needs **data** — measured, time-stamped, logged
* Your aerodynamicists need **the angle you asked for**, not the one you got
* Avionics and mechanisms turn foam and carbon into an **instrumented test article**


---

# Flight-grade kit, off-design

<div class="only-html">
<iframe src="https://www.youtube-nocookie.com/embed/N57M-9iFxZ8?start=23&mute=1&rel=0&modestbranding=1&cc_load_policy=0&iv_load_policy=3" allow="autoplay; encrypted-media; fullscreen" allowfullscreen></iframe>
</div>

<div class="only-print">

[![](../../docs/assets/intro/wind-tunnel-video.jpg)](https://www.youtube.com/watch?v=N57M-9iFxZ8&t=23s)

</div>

<!--
Video starts at 23s, muted. In the PDF this is a still image linked to the
video, because Marp's PDF export cannot carry an iframe.

The Cube Orange+ runs ArduPilot and is the Flight Lab's standard research
autopilot - flown for volcano monitoring, conservation and search and rescue.
In AVDASI 2 it is bolted into a wind tunnel with no GPS, and you command
surfaces directly. That is deliberately off-design: much of the avionics work
is getting a flight controller to behave usefully on the ground.
-->

---

# What the spec asks of avionics

> "Aircraft control systems **shall** comprise a flight control system (FCS), radio control system (RCS), telemetry system (TMS), and ground control station (GCS), with associated power, wiring harnesses, antennae etc."

<div class="columns">
<div>

**Provided to you**

* The flight controller
* The radio control system
* The telemetry system
* Servos, from a set list

</div>
<div>

**Yours to design**

* Power distribution and harnesses
* Mounting and installation
* Logging, calibration, evidence
* Everything that connects them

</div>
</div>

<!--
Requirements Spec section 2.2, Electronics. Point at the word "shall": this is
a customer document, not advice. Almost none of the hardware is a choice, and
almost all of the engineering is in what joins it together.
-->

---

# What it has to do

* Every surface — elevator, rudder, aileron, flap — **commandable from both the radio and the telemetry link**, to specific angles
* **PID stability augmentation** in pitch, tuned on the provided flight controller, switchable on and off
* **Log flight data: 5 Hz minimum, 20 Hz preferred** — pitch angle and rate, servo demand, and whatever else your Company needs
* Everything **removable**, fixed with mechanical fasteners, for maintenance and recycling
* **Nothing above 15 V**, anywhere on or connected to the aircraft

<!--
Sections 2.2, 2.3, 2.4, 3.3 and 4.4. The logging rate is the one students
underestimate: it rules out the slow-and-simple approaches.
-->

---

# What "done" looks like — for now

> "A bench-top prototype of full FCS, RCS, TMS, GCS, and associated systems **shall be demonstrated working** at Gate 2a."

* The **step-by-step guide** takes you there: kit, autopilot, telemetry, power, servos, sensors, logging
* Mechanism prototypes are demonstrated with **servo testers**, not the flight controller
* **This is done for this teaching block only — integration comes next.** A bench that works is not an aircraft that works

<!--
Section 2.2 for the gate, 2.3 and 2.4 for the servo-tester route. Say plainly
that TB1 ends with two halves that each work on a bench, and that putting them
together is the harder job which starts in TB2 - that is the thing groups
leave too late.
-->

---

# Avionics depends on integration

<div class="compact">

| With | You need to agree |
|---|---|
| **Aerodynamics** | Surface sizes and deflections, and so hinge moments, and so servo torque |
| **Mechanisms** | Where the boundary sits: they own torque, servo choice and kinematics; **you supply the PWM** |
| **Structures** | Mounting, access, cable routes, mass |
| **Test** | Power, comms, what's logged, how it's handed over |

</div>

* Avionics is not only an integration job, but it **depends on integration more than most**
* This table is a **starting point, not the answer** — read the spec for your own remit, then **agree each interface** with the division opposite
* Interfaces agreed late are the ones that fail

---

# Interfaces to pin down early

* **Torque and travel**: what the surface needs, and what the servo gives with margin when it is **stalled — servo stall, not aerodynamic stall**
* **Power**: what each component draws, at what voltage, from which supply
* **Connectors and cables**: which plug, which route, and who crimps it
* **Data**: what's logged, at what rate, in what units, and who uses it
* **Command**: who moves which surface in the tunnel, and how you stop it
* Most of these depend on **other teams' work that hasn't happened yet**. Start with a rough number — theirs, or your own gut — and **track what has to be firmed up, and by when**
* **This list is not exhaustive.** Yours will be longer

<!--
Servo stall means the servo is driving against a stop or a jam and drawing its
maximum current - amps, from a rail sized for milliamps. Nothing to do with the
wing stalling, and the double meaning catches people every year.
-->

---

# The system on the bench

![center h:480](../../docs/assets/intro/bench-system.svg)

---

# Avionics workshops

<div class="compact">

| Week | When | Where | Focus |
|---|---|---|---|
| **1** | **Friday, 09:00–11:00** | Stack Room + M.003 | Kit issue; Cube, Mission Planner, telemetry, power |
| 2 | Friday, 09:00–11:00 | Stack Room | Servos and Lua scripting |
| 4 | Friday, 09:00–11:00 | Stack Room | Sensors: ADC and I²C |
| 5 | Friday, 09:00–11:00 | Stack Room | To be confirmed |

</div>

No session in week 3 — Company Day. Full schedule on SharePoint.

---

# Friday: kit day

1. **09:00** A short taught intro in the Stack Room: the kit, and the requirements in more depth
2. **From 09:30** Groups go up to **M.003**, one at a time, to collect a kit
3. **While you wait** Read the guide's first pages (*Kit*, *Cube*), with no hardware yet
4. **Kit in hand** Work through the guide to the Friday checkpoint
5. **To finish** How not to break each component

**Friday checkpoint:** Cube on Plane firmware, buzzer quiet, connected over Wi-Fi, running on bench power.

---

# Getting ready

* **Install Mission Planner on a Windows laptop** before Friday — one working laptop per group
* **Bring** that laptop, charged
* **Read** the guide's index, *Kit* and *Cube* pages

* Everything you need: **[avdasi2.github.io](https://avdasi2.github.io)** → Avionics → Getting ready
* The Cube setup, scripts and guidance are **being revised this month** — a more robust version is coming, with a one-step settings file

---

<!-- _class: section -->

# Part 2: Mechanisms

## From servo to surface

<!--
Handover point. Steve on theory and design tools; Mark and Vince on
implementation. Sessions start in week 3.
-->

---

# What mechanisms have to deliver

![bg right:40% contain](../../docs/assets/intro/uav-general-arrangement.png)

Every moving surface needs a mechanism designed, built and proved:

* **Flap** — plain, slotted or Fowler, 0° to 30°
* **Aileron**, **elevator**, **rudder** — four-bar linkages, ±40° to ±45°
* **Leading edge device** — droop or slat, starboard wing
* **Landing gear** — deployable, behind a door

* Each holds its angle **under aerodynamic load**, to a stated tolerance, within a stated time

<!--
Drawing is DRG A2 from the requirements spec. Tolerances: 2 degrees for
elevator and rudder, 5 for flap and aileron.
-->

---

# The design task

<div class="shots">

![](../../docs/assets/intro/four-bar.svg)
The parts of a **4-bar linkage**

![](../../docs/assets/intro/linkage-app.png)
A flap mechanism drawn and simulated in the Linkage app

</div>

<div class="columns">
<div>

* **Kinematics**: four-bar linkages, mobility, function generation
* Drawn and checked in the **Linkage app**

</div>
<div>

* **Then the real world**: bearings, slop, backlash, friction
* Materials, failure modes, and taking it apart again

</div>
</div>


---

# Where mechanisms meets avionics

<div class="shots small">

![](../../docs/assets/intro/servo-standard.jpg)
Standard servos — HJ and Parallax. The kit also has blue micro servos

![](../../docs/assets/intro/servo-inside.jpg)
Inside one: motor, gear train, board — and a pot reading the output shaft

![](../../docs/assets/intro/servo-tester.svg)
Proved on a **servo tester** before the flight controller

</div>

* **The boundary is the servo cable**
* **Mechanisms own** torque, servo selection, kinematics — and **sensor integration**
* **Avionics own** the PWM, servo rail power, commanding angles, logging
* **Sensor selection is joint**: readable as well as mountable

<!--
The cutaway: demand in on the signal wire, the pot measures the output angle,
the board drives the motor until the two agree. The loop is inside the servo -
which is why the cable, not the shaft, is where we draw the interface.

Photo credits: standard servos by Kborer (public domain); servo internals by
Jstapko, CC BY-SA 3.0; micro servo by Suyash Dwivedi, CC BY-SA 4.0 - all from
Wikimedia Commons. The tester is drawn.
No openly licensed photograph of an HJ or Parallax servo, or of a tester,
exists - the tester is drawn. A lab photograph would be better than both.
-->

<!--
Worth saying out loud: a hobby servo is itself electromechanical, with its own
closed loop inside - a potentiometer on the output shaft, compared against the
commanded pulse width, driving the motor until the error is zero. So the real
interface arguably sits *inside* the servo, and the cable is just where we
agreed to draw the line. Every interface is a choice like that.
-->

---

# Learn from what broke last year

<div class="shots">

![](../../docs/assets/intro/avoid-glued.jpg)
Actuator cable-tied **and glued** to the false rear spar

![](../../docs/assets/intro/avoid-nowashers.jpg)
Weak linkages, **no washers**, nothing to reduce friction

![](../../docs/assets/intro/avoid-threadedrod.jpg)
**Threaded rod** as a pivot, into an oversize hole and into the foam

</div>

* Start simple, prototype early, design for disassembly

---

# Mechanisms sessions

<div class="compact">

| Week | When | Where |
|---|---|---|
| 3 | Thu, 11:00–13:00 | [QB 1.59 Design Suite](https://link.mazemap.com/o5Xo8oWt) |
| 4 | Thu, 11:00–13:00 | [QB 1.59 Design Suite](https://link.mazemap.com/o5Xo8oWt) |
| 5 | Thu, 11:00–13:00 | [QB 1.59 Design Suite](https://link.mazemap.com/o5Xo8oWt) |

</div>

Install the **[Linkage app](https://blog.rectorsquid.com/linkage-mechanism-designer-and-simulator/)** before week 3 — **Windows only**; the macOS version is in early beta.

<!--
TODO(Steve): session content and who leads each - to be confirmed with Mark
and Vince.
-->

---

# Mechanisms — design realisation

<div class="realisation">

* **From kinematics to practical geometry** ![](../../docs/assets/intro/mech-kinematics.png)
* **Transferring torque and motion** ![](../../docs/assets/intro/mech-torque.svg)
* **Design of pivots and joints** ![](../../docs/assets/intro/mech-pivots.png)
* **Standard parts and their uses** ![](../../docs/assets/intro/mech-bearing-flanged.png) ![](../../docs/assets/intro/mech-bush-bronze.jpg) ![](../../docs/assets/intro/mech-bush-plastic.png) ![](../../docs/assets/intro/mech-bearing-plastic.png) ![](../../docs/assets/intro/mech-washer.png) ![](../../docs/assets/intro/mech-shoulder-screw.png)
* **Precision machining and metrology** ![](../../docs/assets/intro/mech-reaming.png)
* **Functional tolerancing and tolerance analysis** ![](../../docs/assets/intro/mech-tolerancing.png)
* **Examples and non-examples** ![](../../docs/assets/intro/mech-example-good.jpg) ![](../../docs/assets/intro/mech-example-bad.jpg)

</div>

<!--
Mark delivers this one. Seven clicks, one per topic, in the order of his own
slide: kinematics, torque and motion, pivots and joints, standard parts,
machining and metrology, tolerancing, then the examples.

The torque and motion sketch is redrawn from Mark's original: a flap carried
on a support at each end, driven from one end only, so the drive has to reach
across the whole span. The frowning face is his.

Source: Mark's "Mechanisms - Design realisation" slide, September 2026.
-->

---

<!-- _class: title-inverted -->

# Questions

## Avionics: Friday, 09:00, Stack Room

Mechanisms: week 3
