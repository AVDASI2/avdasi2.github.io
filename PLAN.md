# Plan: AVDASI 2 Avionics refresh, 2026-27

Working notes for the refresh. Everything is on branch `zensical-migration`; **nothing is pushed until the whole new site goes live at once**. The rollback tags `v2025-26-mkdocs` and `v2025-26-site` are local until then.

## Phases

1. ~~MkDocs → Zensical, Flight Lab theme~~ (done, 19 Sep)
2. Curriculum review: discussion, PowerPoint uploads, session design
3. Deploy the refreshed curriculum, with Marp slides

## Order of work

The unit requirements spec review comes **before** the curriculum review, because the curriculum depends on it. Claude: nudge Steve about the spec review before starting the curriculum review.

1. Unit requirements spec review (Steve, separate session)
2. Review `private/reviews/2026-09-19-stepbystep.md` together: all B (must fix) and C (should fix) items, the Friday session fit, and the "How not to break it" page
3. Provisional workshop topics for weeks 2–5 (the table on the intro deck and on Sessions 2026-27)
4. Intro lecture: plan the avionics content in more depth (25 minutes)
5. Curriculum review
6. Toolchain options: Mission Planner and macOS, Lua or pymavlink, MATLAB or Python for logs. After the spec and curriculum reviews

## Moving to avdasi2.github.io

The site moves from `AVDASI2/docs` (served at `avdasi2.github.io/docs`) to the
org Pages repository `AVDASI2/avdasi2.github.io`, so it is served at the root.
Its Jekyll landing page is replaced: that page's content is now on the Zensical
home page. Old `/docs` links redirect to the new root.

Old `/docs` links redirect to the new root: see `migration/README.md`.

Steps, all of which need Steve's GitHub access:

1. Push this branch to `AVDASI2/docs` first, so the work and the snapshot tags
   (`v2025-26-mkdocs`, `v2025-26-site`) are backed up
2. Clone `AVDASI2/avdasi2.github.io`, and replace its contents with this
   repository's, on a branch
3. Check the build, merge, and set Settings > Pages > Source to **GitHub Actions**
4. Confirm <https://avdasi2.github.io> serves the new site
5. In `AVDASI2/docs`: publish the redirect from `migration/docs-redirect/` on
   `gh-pages` (see `migration/README.md`), remove the CI workflow, add a note to
   the README pointing at the new home, and archive the repository. Keep the
   repository: it holds the snapshot tags
6. Move any open issues to the new repository first, if there are any

## Publishing model

Two sites from one source, as in CADE30008: the in-progress site is everything
in `docs/` and is local only; the live site is only what `publish.yaml` lists.
See the README. `publish.yaml` currently lists everything that was already
public on the old site, so the gate only holds back new or reworked pages.

## Scheduling

[STATUS.md](STATUS.md) is the scheduling summary that `steve-todo` reads: chunks,
hard dates and who we're waiting on, with the detail left here. Rewrite it when
this plan changes. Its format is being agreed with the steve-todo session.

## Curriculum rebuild

From-scratch curriculum defined by aims and learning outcomes, with the
step-by-step guide as the primary learning mode and slides plus written
instructions in parallel, as in CADE30008. Legacy slides reviewed in
`private/reviews/2026-09-20-legacy-slides.md`.

**Aims are agreed: see `private/aims-and-outcomes.md`.** The headline is that
technical outcomes are secondary — the unit is a vehicle for professional
practice, design, project management, teamwork and reflective practice. The
avionics target is a foolproof step-by-step to a full bench prototype.

**The unit is being streamlined, not extended: it is already crowded.** Nothing
below is settled, and no need is assumed until the requirements specification
is in and Steve's unstated aims have been talked through. Workshops as
currently sketched:

1. **Crimping and harnessing**, plus wider integration. George has a draft
2. **Servos**, at the agreed boundary: **Mechanisms own torque requirements,
   servo selection, kinematics and implementation; Avionics supply the input
   PWM** (settled 20 Sep). So avionics teaches the signal, the power path,
   stall current, and the servo tester as hand-over point — not servo sizing
3. **Sensors**: mechanism sensors stay this year (spec now says "sensor/sensors").
   **Pitot dropped for 2026-27** — no avionics students are in P&P, so nothing
   needs airspeed. Give teams *options* for sensing instead:
   - the **internal ADC**, now free, with the kit's shaft-mount potentiometers;
   - the **external ADS1115 over I2C**, already in the published example code.
   Plus **advice for Mechanisms on integrating sensors robustly** — mounting,
   backlash, cable routing and strain relief across the boundary. Mechanisms
   slide 7 ("Avoid") already has the failure photographs for this
4. **Displaying and logging sensor data**, then MATLAB's Flight Log Analyzer.
   A ready-made ground station is an extension activity for the keen

George's harnessing draft (23 slides, ~77 MB of video) is in the teaching share
and covered in the review: it is soldering and harnessing, with crimping still
to scope, and the video needs a home if it is to live on the site.

## To do

- [x] **Kit list on the site** (19 Sep). The *Kit List Print* sheet from `2025-26/.../lab/AVDASI2 Avionics kits.xlsx` is now on the Kit page (`00-kit.md`). Assumed correct until Tim confirms. Issue and return process still to add
- [ ] **Verify the kit assumptions with Tim** (review addendum K1–K9). Asked, no reply yet; we are proceeding on the assumption that the kits are ready and include BECs. Still to confirm: the supply voltage and which XT60 goes where, the large servo model, ADC header soldering, and whether the 2025-26 prep jobs are done
- [ ] **Review the data logging and display options together, after the spec.** Goal: simple and streamlined to start with, extensible for the keen. The options table is in the legacy-slides review; `logger:write()` and `gcs:send_named_float()` are the two ArduPilot routes the current CSV-on-SD and pymavlink approaches predate. Confirm on the bench that Mission Planner's tuning graph lists named floats
- [ ] **Scope change to agree in the requirements spec**: the old electronics deck required students to build a Python GCS, with wireframes and flow diagrams in the report. The plan is now a ready-made ground station as an extension
- [x] ~~Buy a pitot~~ — **dropped for 2026-27** (21 Sep): no avionics students in P&P, so nothing needs airspeed. Revisit if that changes
- [ ] **Write the sensing-options guidance**: internal ADC versus external ADS1115 over I2C, with the trade-offs teams need to choose between them, and how each is read and logged
- [ ] **Write sensor-integration advice for Mechanisms**: how to mount a position sensor so the reading survives the build — backlash, alignment, cable routing, strain relief, and what the failure looks like
- [x] **Student notice added** (21 Sep): the step-by-step index and Example Code pages now carry a note that the Cube configuration, scripts and guidance are being revised, with a more robust version and a parameter file coming. **This makes the work below time-limited: the notice promises something.**
- [ ] **Replace or justify `Mode_switch_example.lua`.** Review what stock ArduPilot does instead (flight modes, `RCn_OPTION` aux functions, `ARMING_CHECK`, RC override), then ship a pre-baked `.param` file plus a documented table of changes from defaults. Known faults in the current script: runtime parameter writes, a dead STABILIZE branch testing the wrong variable, SAS toggling only in manual, and a debug message every 100 ms
- [ ] **Review the provenance of `aircraft_pure_pitch_model.m`** before relying on it or teaching from it. Steve believes it came from another member of staff; it also models a 0.3 kg plate on a rod, not this year's fuselage test article. FDAC has been told to treat its numbers as an example of the right shape only
- [ ] **Internal MWE requirements.** A short requirements spec for the avionics minimum working example: a deliverable for the avionics stream, separate from the unit-level spec. The intro deck's "What done looks like" slide refers to it
- [ ] **Intro deck** (`slides/intro`): 25 minutes of avionics, then 25 on Mechanisms. **Hard stop 12:50**: FDAC control lecture 1 follows at 13:00 in the same room, and the rig is set up during the hour. Fill the requirements placeholders after the spec review
- [ ] **Servos, shared with Mechanisms.** Servo content serves both strands, so write it once. Mechanisms is otherwise taught separately: Steve on theory and design tools (Linkage app, cardboard prototyping) with the intro and Mech 2; Mark Graham and Vince Maes on implementation (2D to 3D, bearings) with Mech 4; Mech 3 proposed as joint
- [ ] **Bench check (a)**: the B1 arming question, 10 minutes, Wed 23 or Thu 24 Sep. Happens regardless; George needs the answer before 2 Oct
- [ ] **Bench run (b)**: timed run of guide pages 00–05, 2 hours, same window. Includes the wiring photo for B8 and the deck's system diagram. If it can't happen, Friday's workshop opens with one kit through 00–05 at the front (review, section H)
- [x] **Moved onto the upstream Flight Lab theme** (20 Sep). Site theme is the `flightlab-zensical-theme` submodule at v2.0.0 (`theme/`, `custom_dir = "theme/dist"`); slides take `flightlab-marp-template#v2.0.0`. Verified: a clone without submodules fails loudly (`Custom theme directory does not exist`, exit 1) rather than deploying an unbranded site. **Anyone cloning this repo needs `git clone --recurse-submodules`, or `git submodule update --init` afterwards**
- [ ] **Bump the theme deliberately, not automatically** (noted 20 Sep). The shared branding lives in `BristolFlightLab/flightlab-brand`, with `flightlab-zensical-theme` (v2.0.0) and `flightlab-marp-template` (v1.1.0, renamed from `marp-template`). Nothing here breaks: GitHub redirects the old URL and the npm package name is unchanged. When bumping, pin `github:BristolFlightLab/flightlab-marp-template#v1.1.0` (no visual change), and consider dropping this repo's copies of `docs/stylesheets/flightlab.css` and `docs/assets/brand/` in favour of the theme as a submodule, as CADE30008 has done. Its session has the gotchas: use theme **v2.0.0**, not v1.0.0, which published the theme's own README and LICENCE onto the site; point `custom_dir` at `theme/dist`; keep `stylesheets/` and `assets/` siblings; rewrite the path to `../theme/dist` for the `.live` config; set `submodules: true` in CI checkout; and test a clone *without* submodules too, confirming it fails loudly rather than quietly deploying an unbranded site
- [x] **Marp theme** (20 Sep). Published as `BristolFlightLab/marp-template`; `package.json` pins `#v1.0.0`, CI builds the decks, and `docs/slides/` is no longer committed. The CI slide build is untested until the first push; if it fails, commit `docs/slides/` again as a fallback
- [ ] Before going live: decide the licence (CC BY 4.0, as in the control course?) and how to credit past contributors
- [ ] Consider an AGENTS.md, as CADE30008 has, once the conventions settle
- [ ] Consider generating STATUS.md, as CADE30008 now does (`status_file()` in its `scripts/build_curriculum.py`, about 60 lines). Only worth it if the curriculum review produces structured session data; today there is none to derive from, because the schedule is canonical on SharePoint
- [ ] Run the [annual update](teaching/annual-update.md) each year; it starts with notes written while teaching is fresh

## Future

- Whole-unit context, and goals for sharing resources and external profile
- Parallel guidelines for the MSc Aerial Robotics Group Project (ARGP; Holybro X650, Cube autopilots). Overlaps with this guide; AVDASI 2 is wind-tunnel only

## Noticed in the teaching schedule

- Company Day is listed as "Friday 10-Oct"; the Friday of week 3 is 9 Oct
- TB2 dates are shown as 2026; they should be 2027
