# Cube Orange+ Autopilot

The University's [Flight Lab](http://flightlab.bristol.ac.uk) uses the [:material-information:CubePilot Cube Orange+](https://docs.cubepilot.org/autopilot/the-cube) as its standard research-grade flight controller. We'll just call it "the Cube".

The Cube is a high-performance open-source flight controller designed for professional UAVs and robotics. It is designed to run [:material-information:Ardupilot](https://ardupilot.org) open-source flight control software. There are a wide range of other open and closed options, but Ardupilot is well-established, well-supported, and flexible.

!!! warning
    The Cube is one of the more expensive components of your UAVs, sometimes with long lead-times for replacements. Please take care of them and be sure to follow instructions below, particularly regarding voltages, servo current, etc.

We'll be using Ardupilot's documentation for a lot of our setup. They have a nice overview page - here's your first mandatory external link to go and check out. 

!!! info "Reminder - link labels"
    Some of the steps require you to follow instructions on external sites, but there are also links included for wider reference. These are labelled with icons:

    * :material-step-forward: Follow this link as part of the current step, then come back to this page to continue.
    * :material-information: This link is for reference, you don't need to follow it right now.
    * (no icon): assume it's just for reference unless it's obviously essential, then let us know so we can fix the docs.
    
Go and take a look, feel free to click around, but **don't do any hardware stuff until you come back and read more instructions here**.

* [:material-step-forward:Ardupilot - Cube Orange+ overview](https://ardupilot.org/plane/docs/common-thecubeorange-overview.html).

Ardupilot is open-source flight control software that runs on a wide range of hardware. The Cube is open hardware from one provider, and they have their own documentation pages that should be considered the authoritative source for hardware documentation. Go and check out the Cube Orange+'s specification pages. You don't need to remember these, but I want you to know where they are. **Don't do any hardware stuff yet!**.

* [:material-step-forward:CubePilot - key specifications](https://docs.cubepilot.org/autopilot/the-cube/introduction/specifications)
* [:material-step-forward:CubePilot - interface ports](https://docs.cubepilot.org/autopilot/the-cube/introduction/interface-specifications).

Right, we're almost at the hands-on bit. The actual 'Cube' is the beautiful orange bit, which has a high-density 80-pin connector on its base **(don't try to pull it off to see, there are some screws through the bottom)**. The 'carrier board' is the black part which breaks out pins from the high-density connector into something a bit more useable. Your kit should contain several wiring harnesses that connect to the ports on the carrier board.

!!! info "Cube connectors"
    The data connectors on the top of the carrier board are 1.25mm-pitch [:material-information:JST-GH](https://www.jst.co.uk/productSeries.php?pid=11517&cat=30), the power connectors are 2mm-pitch [:material-information:Molex CLIK-Mate](https://www.molex.com/en-us/products/connectors/wire-to-board-connectors/clik-mate-connectors), and the servo pins on the side are 2.54mm (0.1") Harwin M20 (often referred to as 'DuPont', or 'servo' connectors).
    
    There are other very similar, often seemingly compatible connector systems, but there are subtle differences that make mixing them non-ideal, particularly for safety-critical applications (in fact, for proper safety-critical applications you wouldn't use simple friction-fit, you'd pick a locking connector). Matt Millman has some great pages on [:material-information:connector naming](https://www.mattmillman.com/why-do-we-call-these-dupont-connectors/) and [:material-information:proper crimping](https://www.mattmillman.com/info/crimpconnectors/dupont-and-dupont-connectors/) (note we have the fancy official JST and Harwin tools in the lab), and [:material-information:even more on crimping](https://www.mattmillman.com/info/crimpconnectors/).

    You have all the wiring you need for the minimum working example in your kits. When you get past that you might want to create custom harnesses - see the unit team for instructions, there's some technique and particularly the tiny JST-GH crimps can be fiddly.

Ok, it's time to get hands-on. Head to the next step using the links below or to the left.
