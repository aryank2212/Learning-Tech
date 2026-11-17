# Setup guide

This guide targets **Omarchy / Arch Linux** (the machine this repo was prepared on). Commands are for Arch; Ubuntu/Fedora/macOS notes are at the bottom.

## 1. Base tools

```bash
sudo pacman -Syu
sudo pacman -S --needed base-devel git curl wget unzip \
    gcc clang gdb cmake make ninja valgrind \
    python uv nodejs npm go postgresql sqlite
```

| Tool | Used for |
|------|----------|
| `base-devel`, `gcc`, `clang` | C / C++ compilers |
| `gdb`, `valgrind` | debugging and memory checks |
| `cmake`, `ninja` | building C++ and CUDA projects |
| `uv` | fast Python version + package manager |
| `nodejs`, `npm` | web development |
| `go` | Go language |
| `postgresql`, `sqlite` | SQL practice |

## 2. Git and GitHub

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
gh auth login        # GitHub CLI – choose HTTPS, log in with the browser
```

## 3. Rust

Already installed on this machine via rustup. To install on a new machine:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
rustup component add clippy rustfmt rust-src rust-analyzer
cargo install rustlings
```

## 4. Python

```bash
uv python install 3.13
uv init my-first-project && cd my-first-project
uv add numpy matplotlib jupyter
uv run python -c "print('hello')"
```

## 5. CUDA (NVIDIA GPU needed)

```bash
nvidia-smi                 # check the driver and GPU are visible
sudo pacman -S cuda        # toolkit (nvcc)
nvcc --version
echo 'export PATH=/opt/cuda/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/opt/cuda/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
```

If `nvidia-smi` fails, install the driver first (`sudo pacman -S nvidia-open-dkms` or your current driver package) and reboot.

## 6. VS Code

```bash
sudo pacman -S code        # or the AUR "visual-studio-code-bin"
code --install-extension rust-lang.rust-analyzer
code --install-extension ms-python.python
code --install-extension ms-vscode.cpptools
code --install-extension ms-vscode.cmake-tools
code --install-extension ms-python.vscode-pylance
code --install-extension bradlc.vscode-tailwindcss
code --install-extension dbaeumer.vscode-eslint
```

## 7. Storage tip

Build output (`target/`, `.venv/`, `node_modules/`, CUDA caches) gets big. Keep practice projects on a larger drive and check space with:

```bash
df -h /
du -sh ~/.cache ~/.cargo ~/.rustup 2>/dev/null
```

## Other systems

- **Ubuntu / Debian:** `sudo apt install build-essential gcc g++ gdb cmake python3 python3-pip nodejs golang`. Install Rust and uv with the curl commands above.
- **macOS:** `xcode-select --install`, then `brew install rustup uv go node cmake`.
- **Windows:** use **WSL2** (Ubuntu) and follow the Ubuntu steps. CUDA works in WSL2 with the NVIDIA Windows driver.

## Verify everything

```bash
gcc --version && g++ --version && clang --version | head -1
rustc --version && cargo --version
python3 --version && uv --version
go version && node --version
nvcc --version || echo "CUDA not installed (optional)"
```

## 8. Extra packages for the other subjects

Install only what you need. Each subject's README lists its own commands. Check a name first with `pacman -Ss <name>`.

```bash
# Languages and core CS
sudo pacman -S --needed jdk-openjdk maven gradle flex bison llvm graphviz

# Digital electronics and hardware
sudo pacman -S --needed iverilog gtkwave verilator kicad yosys arduino-cli

# Networking and operating systems
sudo pacman -S --needed wireshark-qt tcpdump nmap bind mtr iperf3 openbsd-netcat socat qemu-full strace ltrace perf

# Security, statistics and data
sudo pacman -S --needed openssl gnupg age r docker docker-compose
```

`wrk` (load testing) is in the AUR, not the official repos: `yay -S wrk`.
