# Operating Systems

How a computer manages processes, memory, files, devices and security. Every program you write runs on an OS, so this subject makes your code faster and your debugging sharper.

## Prerequisites
C at Level 2 or better (pointers, structs, `malloc`), and comfortable Linux command-line use. Rust helps for the "OS in Rust" route.

## Install — use a safe lab
Don't experiment on your main system. Run practice kernels in a virtual machine with QEMU.
```bash
sudo pacman -S --needed qemu-full gcc make gdb binutils
sudo pacman -S --needed strace ltrace perf htop
```

To build xv6 (MIT's teaching OS), clone it and follow its README for the RISC-V toolchain:
```bash
git clone https://github.com/mit-pdos/xv6-riscv.git
cd xv6-riscv && make qemu
```
The RISC-V cross-compiler is not in the official Arch repos. The xv6 README lists the packages to use, and on Arch they come from the AUR.

Rust route: follow [os.phil-opp.com](https://os.phil-opp.com/) with a nightly toolchain.

Explore Linux as you read: `uname -a`, `cat /proc/cpuinfo`, `ls /proc/$$/`, `cat /proc/meminfo`.

## Weekly rhythm
- Read one OSTEP chapter and do its homework (the OSTEP projects include simulators).
- Then one lab: a shell, a malloc, threads, or an xv6 lab.
- Trace a real program every week with `strace` and write what you see.

## Files
- [syllabus.md](syllabus.md) — topics, with projects
- [resources.md](resources.md) — books, courses, papers, tools
