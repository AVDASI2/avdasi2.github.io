# Mission Planner

Mission Planner is a full-featured ground station application for the ArduPilot open source autopilot project. We will use it to set up the Cube and for initial learning and operation.

!!! info
    Mission Planner requires Windows - I've had some success running it via [Whisky](https://getwhisky.app) on my Mac (update: Whisky is being discontinued, try [WINE](https://www.winehq.org) either directly or via [CrossOver](https://www.codeweavers.com/crossover), or use [Parallels](https://www.parallels.com), [VirtualBox](https://www.virtualbox.org) or [VMWare](https://www.vmware.com/products/desktop-hypervisor/workstation-and-fusion)), but the uni cannot offer support for this approach. **Never** use virtualisation for flight (and wind tunnel) operations.

    Update: there is a [macOS dev build](https://github.com/ArduPilot/MissionPlanner/releases/tag/osxlatest), but it's not an official release yet, and can't flash firmware at the moment. [QGroundControl](https://qgroundcontrol.com) is a cross-platform alternative but the Flight Lab focuses on Mission Planner on Windows.

Take a look at Ardupilot's overview page, then install Mission Planner.

* [:material-step-forward:Ardupilot - Mission Planner Overview](https://ardupilot.org/planner/docs/mission-planner-overview.html)
* [:material-step-forward:Ardupilot - Installing Mission Planner](https://ardupilot.org/planner/docs/mission-planner-installation.html)

!!! info "Mission Planner/Altitude Angel"
    Updated Sept 2025. Mission Planner now prompts you to log in to Altitude Angel - you don't need to do this. Altitude Angel is a flight-restriction update service, which is handy for outdoor flying but their scope does not cover our wind tunnels. Update: Altitude Angel went bankrupt in Oct 2025.

## Connecting

For this first stage we'll power the Cube from your computer's USB port.

!!! warning "A really important note on power"
    **Be careful what you plug into the Cube if you're just powering from USB**. Your laptop's USB port is limited in the current it can supply, and servos can draw significant current when stalled (more on this in later steps). The Cube shouldn't try to pull too much from the USB port, and you should power servos from a separate supply connected to the servo rail (see later section). In short, if you plug stuff in and do the wrong thing you can at best **fry the Cube** (putting your Team, Division, and Company's success at risk), and at worst **fry your laptop** (possibly putting your degree and life at risk - back things up, kids!).

!!! warning "Another important note on connectors"
    The micro-USB connector on the side of the Cube is notoriously fragile. To prevent *expensive* damage, please use the USB port on the socket/buzzer assembly supplied (these are much cheaper to replace).

Connect the USB/buzzer assembly to the carrier board's `USB` port. Follow the Ardupilot instructions, making sure you use that USB socket. When you are asked to select firmware, choose ArduPlane. Connect Mission Planner to the Autopilot and check things work as expected (ignore the parts about telemetry and multiple vehicles).

* [:material-step-forward:Ardupilot - Installing Firmware](https://ardupilot.org/planner/docs/common-loading-firmware-onto-pixhawk.html)
* [:material-step-forward:Ardupilot - Connect Mission Planner to AutoPilot](https://ardupilot.org/planner/docs/common-connect-mission-planner-autopilot.html)

!!! info "CubeOrange+"
    When uploading firmware, you are given a choice between "CubeOrange+" and "CubeOrange+ bdsht". Select "CubeOrange+" to upload firmware.

!!! info "Restoring Ardupilot firmware"
    There are some parameters that don't get reset when you re-flash the same firmware. To do a full 'factory settings' reset the easiest way we've found is to flash a different firmware. We like making our UAVs think they're a submarine then re-re-flashing one of the airborne versions.


## Parameters

In Mission Planner, a parameter is a configurable setting that tells the flight controller how to behave. Parameters control everything from flight modes, sensor settings, failsafes, and PID tuning, to things like which servo does what and how fast a drone should climb or descend.

Many parameters can be adjusted via the various Mission Planner graphical interface screens, but you can also edit them directly, and some are only available in the full parameter list. It's a little intimidating at first, and you need to be careful not to inadvertently break things!

Let's turn down the very loud (by design - you want to be able to hear it outdoors) buzzer that beeps on startup. To access parameters, go to 'config' and then 'full parameter list'. Scroll or search for `NTF_BUZZ_VOLUME` and set it to a low number (1-5). Click `write params` and settings should take effect immediately. 

| Parameter           | Recommended value     | Description                                                      |
|---------------------|-----------|--------------------------------------------------------------|
| `NTF_BUZZ_VOLUME`   | 1–5       | Sets buzzer volume level. Default is LOUD!                                     |
