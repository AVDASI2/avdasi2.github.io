# Status — AVDASI 2 Avionics

**Updated:** 20 Sep 2026 · **Repo:** `~/Documents/GitHub/avdasi2.github.io` (renamed from `docs`) · **Branch:** `zensical-migration`, nothing pushed

A scheduling summary for `steve-todo`, in chunks rather than tasks. The detail
lives in [PLAN.md](PLAN.md) and `private/reviews/`; this file says what state
each chunk is in, what it's waiting on, and what can't move. Rewritten, not
appended to. Keep it under a screen.

*Hard dates* and *Waiting on other people* are rewritten whenever they change;
the rest is refreshed weekly or at a review. The Updated stamp above moves
either way.

## One line

The site is rebuilt and ready; the guide isn't, and Friday's workshop is what makes that urgent.

**Paused, 20 Sep.** Steve is reviewing the unit requirements specification in a separate Claude project. The full curriculum review happens here afterwards, and the guide's outstanding fixes wait for it. Nothing here is blocked on anyone else.

## Hard dates

| Date | What | Must be true beforehand | State |
|---|---|---|---|
| Tue 22 Sep, 12:00–12:50 | Avionics intro, 25 min, then Mechanisms 25 min | Requirements slides filled | Deck drafted and timed to 25 min; blocked on Steve's requirements spec review, expected today. **Hard stop 12:50**: FDAC control lecture 1 follows at 13:00 in the same room and the rig goes in during the hour |
| Wed 23 or Thu 24 Sep | Bench check (a): the B1 arming question, 10 min | One kit, reset as a student would find it | Asked for either day, and requested even if (b) can't happen. Decides whether the servo workshop needs a calibration step, which is the answer George needs for 2 Oct |
| Wed 23 or Thu 24 Sep | Bench run (b): timed run of guide pages 00–05, 2 h | A kit and someone's uninterrupted morning | Valuable but sacrificeable. Gives page timings, every point a student would have to guess, and the wiring photo for B8 and the deck's system diagram. If it doesn't happen, Friday's Workshop 1 becomes the bench test: one kit through 00–05 at the front before groups start. Written down as the fallback, not the plan |
| Fri 25 Sep, 09:00–11:00 | Workshop 1, kit issue, Steve and George jointly | Guide's must-fix items done | Proceeding on the assumption that kits are ready and include BECs; Tim asked, no reply. |
| Fri 2 Oct, 09:00–11:00 | Workshop 2, George alone | George has draft curriculum and resources, with reading time; B1 answer | Blocked on Steve for the materials |

## Waiting on other people

| Who | What | Lead time |
|---|---|---|
| Steve → George | Draft curriculum and resources for workshop 2 to review | Well before Fri 2 Oct; George is confirmed and booked, and is blocked until this arrives |
| Steve | Requirements spec review, then curriculum review | Blocks the deck's two requirements placeholders for Tuesday, and the workshop plan after that |
| Tim | **Bench wiring (B8) first**: supply voltage, which XT60 goes where, and how the servo rail is powered | Chased ahead of the rest. If bench run (b) slips, Tim is the only source for B8, and B8 is the item that breaks kit rather than merely confusing people |
| Tim | The rest of K1–K9: large servo model, ADC headers, prep jobs done, RC issued | Can wait for Tim's convenience; none of it breaks anything on Friday |

## Chunks

| Chunk | State | Detail |
|---|---|---|
| Site rebuild: Zensical, theme, move to the root domain | Done, unpushed | PLAN.md |
| Publishing: draft and live split, ports, redirect for old links | Done, unpushed | README.md |
| Step-by-step guide review | Reviewed; B5 closed, K1 assumed; the rest awaiting Steve's decisions | private/reviews/2026-09-19-stepbystep.md |
| Guide must-fix items before Friday | Not started. A batch of independent decisions, splittable if you need finer scheduling | Review sections B and K |
| Intro deck | Drafted and cut to 25 min; blocked on the requirements spec for two placeholder slides | slides/intro/ |
| Kit pages | Done | docs/avionics/kit-list.md |
| Servos content, shared with Mechanisms | Not started. One piece of work serving both strands, so write it once | PLAN.md |
| Internal MWE requirements | Not started | PLAN.md |
| Push and go live | Blocked on the guide fixes; everything else is ready and Steve has approved pushing | PLAN.md |
| Annual update process | Done | teaching/annual-update.md |

## Parked, deliberately

- Workshop topics for weeks 2–5: provisional until the curriculum review.
- Toolchain decisions: after the requirements and curriculum reviews.
- Licence and contributor credit: before going public, not before Friday.
- Mechanisms as a whole: taught separately, and not in this repo. The exception
  is servos, above.

## Structural moves

Files that moved, so references elsewhere don't rot:

| When | Was | Now |
|---|---|---|
| 20 Sep | `slides/w01-intro/` | `slides/intro/` |
| 20 Sep | `docs/avionics/sessions/w01-intro.md` | `docs/avionics/intro.md` |
| 20 Sep | `docs/avionics/sessions/index.md` | Deleted; the schedule is canonical on SharePoint |
| 20 Sep | Kit list inside `stepbystep/00-kit.md` | `docs/avionics/kit-list.md` |
| 20 Sep | `docs/slides/` committed | Built by CI, no longer committed |
| 20 Sep | Local folder `~/Documents/GitHub/docs` | `~/Documents/GitHub/avdasi2.github.io`, matching the repo name |
| 20 Sep | Vendored `docs/stylesheets/flightlab.css` and brand SVGs | The `theme/` submodule (upstream Flight Lab theme) |
| 19 Sep | Site at `avdasi2.github.io/docs` | Root of `avdasi2.github.io` |
