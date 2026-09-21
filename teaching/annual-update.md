# Annual update

*Drafted with AI assistance (Claude Code). Final versions of all process documents are checked manually.*

What to do each year to roll these materials over to the next cohort. It exists because the same handful of things go stale every year — dates, kit, firmware, external links — and because they go stale quietly: the site keeps working while it slowly stops being true.

Not student-facing. Owner: the avionics lead, with the TSR for anything kit-related.

## Where the truth lives

Nothing in this list is authoritative here. Each item is copied from somewhere else, so the update is really a re-copy.

| What | Source | Who holds it |
|---|---|---|
| Session dates, times and rooms | The unit teaching schedule spreadsheet, and SharePoint | Unit coordinators |
| Kit contents | The avionics kit spreadsheet | TSR |
| What the avionics system must do | The unit requirements specification | Unit team |
| What the MWE must do | The avionics internal requirements | Avionics lead |
| Everything about the hardware and ArduPilot | The vendors' own documentation | External |

The site links to external documentation rather than copying it, so most external drift fixes itself. What doesn't is the links themselves, which move.

## The cycle

### After teaching, while it's fresh (November)

The most valuable half-hour of the year, and the easiest to skip.

- [ ] Write down what actually went wrong in the workshops, in the review file for that year: what students got stuck on, what took longer than planned, what the guide didn't say.
- [ ] Note anything that only worked because someone in the room knew a trick. That trick belongs in the guide.
- [ ] Log kit failures and shortages, so next year's order isn't a guess.

### End of the teaching year (June)

- [ ] Tag the year as taught: `git tag -a v<year>-as-taught -m "AVDASI 2 avionics as taught in <year>"`, and push the tag. This is the snapshot you can always go back to.
- [ ] Kit return: check the kit list against what actually came back, and order replacements.
- [ ] Confirm with the TSR whether the kit changes next year. If it does, the kit list page, the Kit page and step 05's servo figures all follow.

### Before the new year is planned (July to August)

- [ ] Re-read the unit requirements specification. If the avionics requirements changed, the intro deck, the guide's scope and the MWE's internal requirements follow.
- [ ] Review the avionics internal requirements for the MWE against last year's experience.
- [ ] Check the ArduPilot firmware version the guide assumes, and decide whether to move. If you move, re-test every Lua script: the scripting API changes between releases.
- [ ] Check Mission Planner: the installer, the Windows-only position, and whether the macOS build has become usable.
- [ ] Run the link check over the whole site (see below). External documentation gets reorganised silently, most recently CubePilot dropping `/user-guides/` from every URL.

### Once the schedule is out (September, before teaching)

- [ ] Update the workshop dates on the intro slides from the teaching schedule. The site deliberately doesn't carry the schedule: SharePoint is canonical.
- [ ] Update the people on the intro slides: who teaches, who issues kit, who covers the lab.
- [ ] Update the room names, which move more often than you'd think.
- [ ] Bench-test the guide end to end on a freshly reset kit, as a student would (see the review's bench-test section). Do this every year, whatever changed: it's the only test that catches what the guide assumes but never says.
- [ ] Ask the TSR to pre-configure anything that causes a room-wide clash, such as telemetry SSIDs.
- [ ] Read the guide once, in order, as a student who has never seen it.

### After each workshop, during teaching

- [ ] Fix what confused people, that week, while you remember it. A pull request from a student is a legitimate fix, and worth encouraging.

## The mechanical checks

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./scripts/fetch-example-code.sh
.venv/bin/zensical build --clean      # warns about broken internal links
npm run slides                        # rebuild the decks
```

For external links, extract and check them:

```bash
grep -rhoE '\]\(https?://[^) ]+\)' --include='*.md' docs | sed -E 's/^\]\(//; s/\)$//' | sort -u > /tmp/urls.txt
while read -r u; do printf '%s %s\n' "$(curl -s -o /dev/null -L --max-time 20 -w '%{http_code}' "$u")" "$u"; done < /tmp/urls.txt | grep -v '^200'
```

Sites that block automated requests report 403 or 000 rather than 404; check those by hand rather than deleting them.

## Writing it down

Each year's review goes in `private/reviews/<date>-<scope>.md`, and each year's plan in `PLAN.md`. The review is the memory: it's what tells next year's version of you why a page says what it says.
