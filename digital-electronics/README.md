# Digital Electronics

How logic is built from transistors and gates, and how gates become memory, adders and CPUs. It is the bridge between physics and computer architecture, and the most hands-on subject in this repo.

## Prerequisites
- Boolean algebra (see [maths/discrete-maths.md](../maths/discrete-maths.md), Phase 8)
- Basic electricity: voltage, current, resistance (helpful, not required)

## Install — simulate first
```bash
sudo pacman -S --needed iverilog gtkwave verilator kicad yosys
iverilog -V | head -1
verilator --version
```
- `iverilog` simulates Verilog; `gtkwave` shows waveforms; `verilator` is a fast simulator.
- `kicad` designs schematics and circuit boards.
- `yosys` is an open-source synthesis tool for FPGAs.

Browser and GUI tools (nothing to install):
- [Falstad circuit simulator](https://www.falstad.com/circuit/) — drag gates and watch signals
- [Logisim Evolution](https://github.com/logisim-evolution/logisim-evolution/releases) — desktop logic simulator, download from the releases page
- [HDLBits](https://hdlbits.01xz.net/) — Verilog exercises in the browser
- [EDA Playground](https://www.edaplayground.com/) — run Verilog and VHDL online

## Hardware kit (optional, cheap)
- Breadboard, jumper wires, LEDs, resistors, push buttons
- 74HC-series logic chips: 7400 (NAND), 7408 (AND), 7432 (OR), 7474 (D flip-flop), 74161 (4-bit counter)
- Microcontroller: Raspberry Pi Pico, ESP32, or Arduino Uno. `arduino-cli` is in the official repos: `sudo pacman -S arduino-cli`.
- FPGA board later: Digilent Basys 3 or iCEBreaker.

## Weekly rhythm
- Design the circuit on paper, simulate it, then build it on a breadboard (if you have one).
- Write the same circuit in Verilog and check it against the simulation.

## Files
- [syllabus.md](syllabus.md) — topics, with projects
- [resources.md](resources.md) — books, videos, practice tools
