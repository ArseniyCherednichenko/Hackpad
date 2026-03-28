# HackPad

A 3×3 macro keypad built for [Hack Club's Hackpad grant programme (Blueprint)](https://hackclub.com/hackpad/). Features Cherry MX mechanical switches, per-key SK6812 RGB LEDs, a rotary encoder, and an OLED status display — all driven by a Seeed XIAO RP2040.

---

## Features

- **3×3 mechanical key matrix** — Cherry MX PCB-mount switches with 1N4148 anti-ghosting diodes
- **9× SK6812 MINI-E** reverse-mount RGB LEDs, individually addressable (NeoPixel-compatible)
- **EC11 rotary encoder** — volume control on layer 0, hue control on layer 1
- **0.91″ SSD1306 OLED** — shows "HackPad" and the active layer name
- **Seeed XIAO RP2040** MCU — USB-C, 264 KB RAM, 2 MB Flash
- **KMK firmware** (CircuitPython) — 2 layers, encoder support, RGB animations
- **Custom 3D-printed case** — 2-part snap/screw design, M3 heat-set inserts

---

## Pin Assignments

| Signal       | XIAO Pin | Description                       |
|-------------|----------|-----------------------------------|
| ROW0        | D0       | Switch matrix row 0               |
| ROW1        | D1       | Switch matrix row 1               |
| ROW2        | D2       | Switch matrix row 2               |
| COL0        | D3       | Switch matrix column 0            |
| COL1        | D6       | Switch matrix column 1            |
| COL2        | D7       | Switch matrix column 2            |
| OLED SDA    | D4       | I²C data for SSD1306 display      |
| OLED SCL    | D5       | I²C clock for SSD1306 display     |
| ENC_A       | D8       | Rotary encoder channel A          |
| ENC_B       | D9       | Rotary encoder channel B          |
| LED_DATA    | D10      | SK6812 data chain                 |

---

## Key Map

### Layer 0 — Media
| Prev Track | Play/Pause | Next Track |
|:-----------:|:----------:|:----------:|
| Vol Down   | Mute        | Vol Up     |
| Copy       | Paste       | **Hold → Layer 1** |

Encoder: rotate = Volume Down / Up

### Layer 1 — RGB Control
| Hue −  | Hue +  | Sat −  |
|:-------:|:------:|:------:|
| Sat +  | Brt −  | Brt +  |
| Anim   | RGB Toggle | *(held)* |

Encoder: rotate = Hue − / +

---

## Bill of Materials

All parts sourced from the Hackpad Kit.

| Qty | Reference       | Part                             | Package / Notes               |
|----:|-----------------|----------------------------------|-------------------------------|
|  1  | U1              | Seeed XIAO RP2040                | Castellated module            |
|  9  | SW1–SW9         | Cherry MX PCB-mount switch       | 3-pin PCB mount               |
|  9  | D1–D9           | 1N4148 diode                     | SOD-123 SMD                   |
|  9  | LED1–LED9       | SK6812 MINI-E                    | 3.5×3.5 mm, reverse-mount     |
|  1  | ENC1            | EC11 rotary encoder with shaft   | Vertical, 20 mm shaft         |
|  1  | J1              | 4-pin 2.54 mm header             | OLED connector (GND/VCC/SCL/SDA) |
|  1  | OLED1           | 0.91″ SSD1306 OLED module        | 128×32, I²C, 4-pin GND-VCC-SCL-SDA |
|  1  | C1              | 100 nF ceramic capacitor         | 0805 SMD — LED decoupling     |
|  4  | —               | M3×8 socket-head screws          | Case assembly                 |
|  4  | —               | M3 heat-set inserts              | For bottom tray bosses        |

---

## Project Layout

```
PCB/
  hackpad.kicad_pro     KiCad project
  hackpad.kicad_sch     Schematic
  hackpad.kicad_pcb     PCB layout (80×70 mm, 2-layer)
CAD/
  hackpad_assembly.step Full case + PCB assembly
Firmware/
  main.py               KMK CircuitPython firmware
production/
  gerbers.zip           Gerber + drill files for fab
  Top.step              Top plate for 3D printing
  Bottom.step           Bottom tray for 3D printing
  main.py               Firmware (copy for flashing)
images/
  (screenshots go here)
README.md
```

---

## Photos / Renders

![Schematic](images/schematic.png)
![PCB](images/pcb.png)
![Case](images/case.png)

---

## Firmware — Quick Start

1. Install [CircuitPython 9.x](https://circuitpython.org/board/seeeduino_xiao_rp2040/) on the XIAO RP2040.
2. Install [KMK](https://github.com/KMKfw/kmk_firmware) — copy the `kmk/` folder to `CIRCUITPY/`.
3. Copy `production/main.py` to `CIRCUITPY/code.py`.
4. The keyboard will enumerate immediately over USB.

---

## PCB Fabrication Notes

- Board size: **80 × 70 mm**, 2 layers, 1.6 mm FR4
- Min trace width: 0.2 mm (signal), 0.5 mm (power)
- Min via: 0.8 mm drill, 0.4 mm annular ring
- Surface finish: HASL or ENIG
- Send `production/gerbers.zip` to your preferred fab (JLCPCB, PCBWay, etc.)

---

## Case Printing Notes

- Print `Top.step` and `Bottom.step` in PLA or PETG, 0.2 mm layer height, 3–4 perimeters.
- Insert M3 heat-set inserts into the four corner bosses of the bottom tray using a soldering iron.
- PCB sits on the 2 mm standoffs inside the tray.
- Top plate secures with 4× M3×8 screws through the corner holes.

---

*Built with ❤️ for Hack Club Blueprint*
