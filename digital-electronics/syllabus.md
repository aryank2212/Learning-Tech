# Digital electronics syllabus

Tick items in [progress/TRACKER.md](../progress/TRACKER.md).

### Phase 1 – Number systems and Boolean algebra
- [ ] Binary, octal, hexadecimal, BCD
- [ ] Two's complement and overflow
- [ ] Boolean laws; De Morgan's theorems
- [ ] Truth tables

🛠️ Project: a 4-bit binary-to-hex converter in the Falstad simulator.

### Phase 2 – Logic gates and minimisation
- [ ] AND, OR, NOT, NAND, NOR, XOR, XNOR
- [ ] Universal gates: building everything from NAND
- [ ] Karnaugh maps (K-maps)
- [ ] Sum-of-products and product-of-sums

🛠️ Project: minimise a four-variable function with a K-map, then build it with only NAND gates.

### Phase 3 – Combinational circuits
- [ ] Half and full adders; ripple-carry and carry-lookahead adders
- [ ] Subtractors and comparators
- [ ] Multiplexers, demultiplexers, encoders, decoders

🛠️ Project: a 4-bit adder/subtractor in Logisim Evolution.

### Phase 4 – Sequential circuits
- [ ] Latches (SR, D) and flip-flops (D, JK, T)
- [ ] Clocks; setup and hold time
- [ ] Registers and shift registers
- [ ] Synchronous vs asynchronous counters

🛠️ Project: a 4-bit counter driving a seven-segment display.

### Phase 5 – Finite state machines
- [ ] Moore and Mealy machines
- [ ] State diagrams and state minimisation
- [ ] Sequence detectors

🛠️ Project: a vending-machine controller as a Moore machine.

### Phase 6 – Memory and datapath
- [ ] RAM and ROM organisation; address decoding
- [ ] Register files
- [ ] ALU design with flags (zero, carry, overflow, negative)

🛠️ Project: an 8-bit ALU with a control unit that selects its operation.

### Phase 7 – Hardware description languages (Verilog)
- [ ] Modules, `wire` and `reg`
- [ ] Combinational and sequential `always` blocks
- [ ] Testbenches
- [ ] Simulating with Icarus Verilog; viewing waveforms in GTKWave

🛠️ Project: write a testbench for your ALU and check the waveforms.

### Phase 8 – Timing and reliability
- [ ] Propagation delay; clock skew
- [ ] Metastability and synchronisers
- [ ] Debouncing push buttons

🛠️ Project: a button debouncer in Verilog, tested in simulation.

### Phase 9 – Microcontrollers and interfaces
- [ ] GPIO, timers, PWM
- [ ] Interrupts
- [ ] UART, SPI, I²C

🛠️ Project: blink an LED, then read a sensor over I²C and print the values over UART.

### Phase 10 – From gates to a CPU (capstone)
- [ ] Build the Nand2Tetris "Hack" computer step by step, or
- [ ] Design a simple 8-bit or 16-bit CPU in Verilog

🛠️ Project: run a small program on your CPU and show it on screen or in simulation.
