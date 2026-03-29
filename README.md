# HackPad

My Hackapd is a 3×3 macro keypad, which can be coded to address all needs. It runs on a Seeed XIAO RP2040, and features Cherry MX mechanical switches, SK6812 RGB LEDs, a rotary encoder, and an OLED status display.


## Why I built this

I wanted to have a custom keypad on my desk and use shortcuts assigned to each key.

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

## Files Layout

```
PCB/
  hackpad.kicad_pro     
  hackpad.kicad_sch
  hackpad.kicad_prl
  hackpad.kicad_pcb
  gerbers.zip    
CAD/
  Hackpad Keyboard Outline.step
  Hackpad PCB.step
  Hackpad case BOTTOM.step
  Hackpad case TOP.step
  Hackpad case FULL.step
Firmware/
  main.py               
images/
  (screenshots)
BOM.csv
README.md
```

---

## PCB Fabrication Notes

- Board size: **80 × 70 mm**, 2 layers, 1.6 mm FR4
- Min trace width: 0.2 mm (signal), 0.5 mm (power)
- Min via: 0.8 mm drill, 0.4 mm annular ring
- Surface finish: HASL or ENIG

---

## Case Printing Notes

- Print `Top.step` and `Bottom.step` in PLA or PETG, 0.2 mm layer height, 3–4 perimeters.
- Insert M3 heat-set inserts into the four corner bosses of the bottom tray using a soldering iron.
- PCB sits on the 2 mm standoffs inside the tray.
- Top plate secures with 4× M3×8 screws through the corner holes.

---

*Built with ❤️ by Arseniy*
