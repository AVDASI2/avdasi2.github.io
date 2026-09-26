# Power

Most remotely-piloted aircraft will require various different power distribution systems (you might hear these referred to as 'buses') for things like flight control computers (often 5V or 3.3V with minimal current draw), companion computers (e.g. Raspberry Pi 5V5A), sensors, and electronic speed controllers (ESCs) for electric motors.

!!! danger "Lithium Polymer batteries"
    For flying, you'd usually use a Lithium Polymer (LiPo) battery to power your aircraft - these require careful treatment as they can [decompose violently](https://www.youtube.com/watch?v=aZOKLpOn_W4) if they are dropped, dented, overcharged, undercharged, or looked at in the wrong way. We **do not** store or charge bare LiPos anywhere on University premises except in authorised charging bays by authorised people. For AVDASI2 we'll be using mains-powered double-insulated AC-to-DC power supplies.

The Cube includes a power module (small PCB with yellow XT60 connectors on) to measure battery voltage, regulate the supply to the flight controller, and pass through full battery power for motors etc. In your kit this is the **Power Brick Mini**, and its cable is labelled **POWER2** — that is the carrier board port it goes to. Your bench supply is **12 V DC**, and it feeds the power module through the XT60 connectors.


**Disconnect your USB cable** to avoid any funky dual-powering of your Cube or feeding power back into your laptop.

Head to the CubePilot instruction pages and follow the sections 'installing the microSD card', 'power supply', and 'power module connection'. **Don't do anything with ESCs, motors, sensors, or telemetry yet**.

* [:material-step-forward:CubePilot - Setup/Autopilot Module](https://docs.cubepilot.org/autopilot/the-cube/setup/autopilot-module).

Now you should be able to connect your power supply and talk to your Cube completely wirelessly!