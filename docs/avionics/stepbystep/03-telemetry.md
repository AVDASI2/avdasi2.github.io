# Telemetry

Let's start to free you from the shackles of the USB cable.

So far, you've been talking to your Cube over a USB-Serial connection, either with Mission Planner auto-connecting or you manually choosing the correct COM port. They can communicate over various other protocols, including WiFi.

We'll use a common WiFi chip called an ESP8266. It works in two modes, and **both are usable for practical testing and for flight**:

* **Point-to-point** (access point mode): the board runs its own network and your laptop joins it directly. Nothing else is needed, so it works anywhere — including out in the field.
* **Station mode**: the board joins an existing network, along with your ground station and anything else that needs to talk to it. Use this when several devices have to share one network, or when you need device-to-device communication.

We'll start point-to-point, because it needs nothing but the kit in front of you.

When you power on your telemetry board it will broadcast a Wi-Fi SSID (network name); check your kit number for what SSID to expect.

**Your telemetry board Wi-Fi SSID and passcode is:** SSID: 'AVDASI2 - Kit X', Passcode: 'beyondrobotixX' where X is kit number (1-12)

!!! warning "Do NOT change the telemetry board Wi-Fi SSID or passcode"

    If SSIDs are changed, it may be hard to identify which wi-fi signal belongs to which kit, and you may end up clashing with someone else's wi-fi signal. It is a pain to reset the telemetry board if you change the passcode and can no longer gain access.

!!! info "The lab has its own network: not eduroam"

    When you use station mode, join the lab's **autonomous network**, not eduroam. Eduroam deliberately stops devices talking directly to one another, which is exactly what a ground station and an autopilot need to do.

    The SSID and password are displayed in the lab. They aren't published here, and you don't need them for the point-to-point step above.

* [:material-step-forward:Beyond Robotix Kahuna](https://beyond-robotix.gitbook.io/docs/kahuna/quick-start-guide) - the ESP8266 board we use. Connect to the TELEM1 port.
* [:material-information:Ardupilot Telemetry](https://ardupilot.org/copter/docs/common-telemetry-landingpage.html#common-telemetry-landingpage) - lots more options, but not needed for AVDASI2.

Now you're talking to the Cube wirelessly, all the USB cable is doing is providing power!

!!! tip
    Mission Planner should connect automatically - if not, set the comms protocol to UDP, baud 57600.
    
    If not working, make sure your laptop is still connected to your telemetry board's own network — not eduroam, and not the lab's autonomous network — and that your GCS isn't also connected to the Cube over USB-Serial.
