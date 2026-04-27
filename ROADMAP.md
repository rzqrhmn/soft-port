# Roadmap — Embedded & Firmware Portfolio

**Goal**: Build a credible public portfolio for testing / commissioning / lab engineer roles in Germany, with daily 15-30 minute commits.

**Strategy**: Start with Python on laptop (no hardware), slowly add embedded simulation (Wokwi.com — free, runs in browser), only buy hardware when comfortable.

**Total horizon**: 6 months. Daily small steps. Skip days OK — consistency over perfection.

---

## Level 1 — Foundations (Week 1-4) — Python + Git basics

No hardware needed. Goal: comfortable with Git, Python, sensor data files.

| Day | Task | Skill |
|-----|------|-------|
| 01 | Hello, embedded world — print sensor name from list | Python lists, git basics |
| 02 | Read CSV: simulated motor temperature log | csv module, file I/O |
| 03 | Compute mean / max / min from CSV | numpy basics |
| 04 | Plot temperature over time | matplotlib |
| 05 | CLI tool: pass CSV path as argument | argparse |
| 06 | Detect threshold crossings (alarm logic) | conditionals, logic |
| 07 | **Mini-project**: motor temp analyzer (combine day 1-6) | refactoring, README |
| 08 | Generate fake sensor data (random + trend) | random, numpy |
| 09 | Save sensor data to CSV with timestamps | datetime, csv writer |
| 10 | Detect anomalies: rolling average + 2σ | numpy rolling stats |
| 11 | Plot anomalies highlighted in red | matplotlib styling |
| 12 | Multi-sensor: temperature + vibration + current | dict / class |
| 13 | Class-based sensor reader | OOP basics |
| 14 | **Mini-project**: 3-sensor anomaly detector | OOP + analysis |
| 15-21 | Pick 1: build a temperature-monitor CLI dashboard with `rich` library | TUI |
| 22-28 | Refactor week: clean code, add tests with `pytest`, write README | testing, docs |

End of Level 1 goal: 1 polished GitHub repo (`motor-data-analyzer`) with README, tests, screenshots.

---

## Level 2 — Industrial Protocols (Week 5-8) — talking like real equipment

Still no hardware. Implement protocols in pure Python — this is a HUGE differentiator for industrial roles.

| Week | Topic | Deliverable |
|------|-------|-------------|
| 5 | Modbus RTU frame parser | Decode raw bytes → register values, with CRC check |
| 6 | Modbus TCP server simulator | Pretend to be a sensor, respond to client requests |
| 7 | CAN bus message decoder (DBC files) | Parse motor controller CAN frames |
| 8 | MQTT pub/sub: sensor → broker → dashboard | Use Mosquitto broker locally |

End of Level 2 goal: 2nd repo `industrial-protocols-sandbox` — shows you understand factory floor communication.

---

## Level 3 — Firmware Simulation (Week 9-14) — write actual C/C++

No hardware needed — use **Wokwi.com** (online Arduino/ESP32 simulator). Code runs in browser, you copy to repo.

| Week | Topic | Deliverable |
|------|-------|-------------|
| 9 | Arduino blink + serial print (Wokwi) | First C code in repo |
| 10 | Read DHT22 temp sensor in Wokwi | Sensor interfacing |
| 11 | PWM control — fade LED | Timer/PWM concepts |
| 12 | State machine in C — traffic light | Embedded patterns |
| 13 | PID controller in C (compile + run on PC) | Control systems theory → code |
| 14 | Modbus slave on Arduino (Wokwi) | Combine Level 2 + 3 |

End of Level 3 goal: 3rd repo `firmware-fundamentals` — shows you can write and reason about firmware code.

---

## Level 4 — Real Hardware (Week 15-20) — optional but huge boost

Buy: **ESP32 dev board (~10 EUR) + DHT22 sensor (~3 EUR) + breadboard kit (~10 EUR)**. Total ~25-30 EUR from Reichelt or Amazon.de.

Why this matters in Germany: real hardware photos in your README = recruiter sees you actually built things.

| Week | Topic | Deliverable |
|------|-------|-------------|
| 15 | ESP32 + DHT22 — read temperature | Photo + serial output in README |
| 16 | Send via WiFi to MQTT broker | Networking on embedded |
| 17 | Web dashboard (Flask) showing live data | Full stack mini |
| 18 | Log data to SQLite | Persistence |
| 19 | Email alert on threshold (SMTP) | Real-world usefulness |
| 20 | Open Source: publish as proper repo with docs | Polish |

End of Level 4 goal: 4th repo `iot-temp-monitor` — your strongest portfolio piece. With photos.

---

## Level 5 — Capstone (Week 21-26) — predictive maintenance edge device

This is the project that gets you interviews.

**Concept**: ESP32 reads vibration (accelerometer MPU6050, ~5 EUR) from a small motor (you can use an old fan), runs simple ML on edge (TensorFlow Lite Micro), classifies: normal / unbalanced / bearing wear. Alerts via MQTT.

Direct connection to your 10 years at Krakatau Posco with synchronous motors → this is your story.

| Week | Task |
|------|------|
| 21 | Collect baseline vibration data from a fan (your laptop fan works!) |
| 22 | Label data: normal vs simulated faults |
| 23 | Train tiny ML model (scikit-learn → TF Lite) |
| 24 | Deploy model on ESP32 |
| 25 | Build alert system + dashboard |
| 26 | Write proper README + LinkedIn post explaining the project |

End of Level 5 goal: capstone repo `motor-condition-monitor` + LinkedIn article + portfolio website (GitHub Pages, free).

---

## After 6 months you have:

- 5 public GitHub repos with real code, tests, READMEs
- ~150-180 days of green squares (real)
- Portfolio website
- LinkedIn article showing engineering thinking
- Story for German interviews: "I built X to apply my motor experience"

This is what gets you past CV screening for Werkstudent / Praktikum / Junior testing roles.

---

## Adjustments

- Stuck on a day? Skip and come back. Better than burning out.
- Day too easy? Push to next day same session — banking days for thesis crunch time is fine.
- Concept unclear? Each day's `README.md` has links to free resources.
- Need to pause? Disable scheduled tasks (see SETUP.md). Resume any time.
