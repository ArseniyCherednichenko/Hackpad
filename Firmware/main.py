"""
HackPad — KMK firmware for Seeed XIAO RP2040
3×3 macro keypad + EC11 rotary encoder + SK6812 RGB LEDs + SSD1306 OLED

Hardware wiring
---------------
  D0  = Row 0            D6  = Col 1
  D1  = Row 1            D7  = Col 2
  D2  = Row 2            D8  = Encoder A
  D3  = Col 0            D9  = Encoder B  (encoder click not wired)
  D4  = OLED SDA         D10 = SK6812 data chain
  D5  = OLED SCL
  3V3 = OLED VCC / LED VDD
  GND = common ground

Switch matrix: COL2ROW, 1N4148 diode per switch
  Anode → row   Cathode → column
"""

import board
import busio
import supervisor

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306Driver
from kmk.modules.layers import Layers

# ── Keyboard object ────────────────────────────────────────────────────────────
keyboard = KMKKeyboard()

# ── Matrix ────────────────────────────────────────────────────────────────────
keyboard.col_pins   = (board.D3, board.D6, board.D7)          # COL0, COL1, COL2
keyboard.row_pins   = (board.D0, board.D1, board.D2)          # ROW0, ROW1, ROW2
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ── Layers module ─────────────────────────────────────────────────────────────
layers_mod = Layers()
keyboard.modules.append(layers_mod)

# ── RGB LEDs (SK6812 on D10, 9 pixels) ────────────────────────────────────────
rgb = RGB(
    pixel_pin   = board.D10,
    num_pixels  = 9,
    hue_default = 0,
    sat_default = 255,
    val_default = 50,
    animation_mode   = AnimationModes.BREATHING,
    animation_speed  = 1,
    breathe_center   = 1.5,
    knight_effect_length = 3,
)
keyboard.extensions.append(rgb)

# ── OLED Display (SSD1306, 128×32, I2C on D4=SDA / D5=SCL) ──────────────────
i2c_bus = busio.I2C(scl=board.D5, sda=board.D4)

oled_driver = SSD1306Driver(i2c=i2c_bus, device_address=0x3C)
display = Display(
    display     = oled_driver,
    width       = 128,
    height      = 32,
    flip        = False,
    flip_left   = False,
    flip_right  = False,
    brightness  = 1.0,
    brightness_step = 0.1,
    entries     = [
        TextEntry(text='HackPad', x=0, y=0,  x_anchor='L', y_anchor='T', inverted=False),
        TextEntry(text='Layer: ', x=0, y=16, x_anchor='L', y_anchor='T'),
        # Dynamic layer name — updated in on_runtime_enable callback below
    ],
)
keyboard.extensions.append(display)

# ── Encoder ───────────────────────────────────────────────────────────────────
encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.D8, board.D9, None, False),)   # A, B, btn=None, reverse=False
keyboard.modules.append(encoder_handler)

# ── Key map ───────────────────────────────────────────────────────────────────
# 9 switches, 2 layers
#
# Physical layout (looking down at the keypad):
#   SW1  SW2  SW3      →  row 0, cols 0-2
#   SW4  SW5  SW6      →  row 1, cols 0-2
#   SW7  SW8  SW9      →  row 2, cols 0-2  (SW9 = MO(1) hold)
#
# Layer 0 — Media / macro layer
#   [Prev]   [Play]   [Next]
#   [VolDn]  [Mute]   [VolUp]
#   [Copy]   [Paste]  [MO(1)]     ← hold SW9 to activate layer 1
#   Encoder CW = Volume Up, CCW = Volume Down
#
# Layer 1 — RGB control layer
#   [Hue-] [Hue+]  [Sat-]
#   [Sat+] [Brt-]  [Brt+]
#   [Anim] [TOG ]  [TRNS]
#   Encoder CW = Hue+, CCW = Hue-

keyboard.keymap = [
    # ── Layer 0 ──────────────────────────────────────────────────────────────
    [
        KC.MPRV,  KC.MPLY,  KC.MNXT,
        KC.VOLD,  KC.MUTE,  KC.VOLU,
        KC.COPY,  KC.PASTE, KC.MO(1),
    ],
    # ── Layer 1 ──────────────────────────────────────────────────────────────
    [
        KC.RGB_HUD, KC.RGB_HUI, KC.RGB_SAD,
        KC.RGB_SAI, KC.RGB_VAD, KC.RGB_VAI,
        KC.RGB_ANI, KC.RGB_TOG, KC.TRNS,
    ],
]

# ── Encoder key bindings ──────────────────────────────────────────────────────
# encoder_handler.map format: list-of-layers, each layer is a tuple per encoder:
#   (counter_clockwise_key, clockwise_key)
encoder_handler.map = [
    # Layer 0: volume
    ((KC.VOLD, KC.VOLU),),
    # Layer 1: hue
    ((KC.RGB_HUD, KC.RGB_HUI),),
]

# ── Display layer name helper ─────────────────────────────────────────────────
LAYER_NAMES = {
    0: "Media",
    1: "RGB Ctrl",
}

# Simple runtime hook to update the layer name on the OLED
_last_layer = -1

def update_display():
    global _last_layer
    current = keyboard.active_layers[0] if keyboard.active_layers else 0
    if current != _last_layer:
        _last_layer = current
        name = LAYER_NAMES.get(current, f"Lyr {current}")
        display.entries[1] = TextEntry(
            text=f'Layer: {name}',
            x=0, y=16, x_anchor='L', y_anchor='T'
        )

# Attach hook — KMK calls this each matrix scan
keyboard._post_hid_hooks = [update_display]

# ── Go! ───────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    keyboard.go()
