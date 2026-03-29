# HackPad

My Hackapd is a 3×3 macro keypad, which can be programmed to address all needs. It runs on a Seeed XIAO RP2040, and features Cherry MX mechanical switches, SK6812 RGB LEDs, a rotary encoder, and an OLED status display.

<img width="1086" height="828" alt="Screenshot 2026-03-29 at 20 05 30" src="https://github.com/user-attachments/assets/de9cacb0-417e-4028-9833-30e429d9bebb" />


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
## Schematic

<img width="1301" height="716" alt="Screenshot 2026-03-29 at 21 07 59" src="https://github.com/user-attachments/assets/ade425b4-9886-4544-840a-28b575bb7545" />

---

## PCB 

<img width="799" height="899" alt="Screenshot 2026-03-29 at 21 07 40" src="https://github.com/user-attachments/assets/216a88c9-6adb-4d03-a82a-bada28acb502" />

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
## Bill of Materials

| # | Component | Qty | Package | Supplier | Link | Price (€) |
|---|-----------|-----|---------|----------|------|-----------|
| 1 | Seeed XIAO RP2040 | 1 | DIP-14 (castellated) | AliExpress | [Buy](https://de.aliexpress.com/item/1005008200917480.html) | 5.49 |
| 2 | Cherry MX Compatible Switch | 9 | MX Hotswap 1U | Amazon | [Buy](https://www.amazon.de/Topiky-Mechanische-Tastaturschalter-Keyboard-Mounted-default/dp/B086MQXQW7) | 7.23 |
| 3 | SK6812 MINI-E RGB LED | 9 | Reverse-mount 3228 | AliExpress | [Buy](https://de.aliexpress.com/item/1005008308801366.html) | 4.82 |
| 4 | 1N4148 Diode | 9 | DO-35 (THT) | AliExpress | [Buy](https://de.aliexpress.com/item/1005009372401863.html) | 1.49 |
| 5 | EC11 Rotary Encoder | 1 | Alps EC11E, vertical, 20mm | AliExpress | [Buy](https://de.aliexpress.com/item/1005008036285937.html) | 5.18 |
| 6 | 0.91" OLED Display (SSD1306) | 1 | 4-pin I2C, 128×32 | AliExpress | [Buy](https://de.aliexpress.com/item/1005010665352578.html) | 7.11 |
| 7 | Encoder Knob | 1 | 6mm D-shaft | AliExpress | [Buy](https://de.aliexpress.com/item/4000027546987.html) | 3.76 |
| 8 | MX Keycaps (1U) | 9 | MX stem compatible | AliExpress | [Buy](https://de.aliexpress.com/item/1005010020786682.html) | 8.20 |
| 9 | M2.5×6mm Screws | 4 | M2.5 pan head | Moddiy | [Buy](https://www.moddiy.com/products/1268/M2.5-x-6mm-Black-Screws-CM2.5x6x4.5.html) | 0.69 |
| 10 | M2.5×4mm Standoffs | 4 | M2.5 female-female | Amazon | [Buy](https://www.amazon.de/Standoff-Schraube-Computer-Motherboard-Weiblich/dp/B0CCQBQHJQ) | 7.28 |
| 11 | Rubber Feet (adhesive) | 4 | ~8mm diameter | AliExpress | [Buy](https://de.aliexpress.com/item/1005007854664253.html) | 3.83 |
| 12 | USB-C Cable | 1 | USB-C to USB-A/C | AliExpress | [Buy](https://de.aliexpress.com/item/1005004784212304.html) | 1.93 |
| | | | | | **TOTAL** | **€32.80** |

---

*Built with ❤️ by Arseniy*
