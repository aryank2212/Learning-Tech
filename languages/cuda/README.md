# CUDA

NVIDIA's platform for running code on the GPU. Thousands of threads run the same kernel on different data. Used for AI training, image processing, simulation and scientific computing.

**Prerequisites:** C or C++ (you should be comfortable with pointers and arrays), and an NVIDIA GPU.

## Install

```bash
nvidia-smi                 # driver and GPU visible?
sudo pacman -S cuda        # toolkit (nvcc), already installed on this machine
nvcc --version

# Add to ~/.bashrc
export PATH=/opt/cuda/bin:$PATH
export LD_LIBRARY_PATH=/opt/cuda/lib64:$LD_LIBRARY_PATH
```

Compile: `nvcc hello.cu -o hello && ./hello`
Samples: `git clone https://github.com/NVIDIA/cuda-samples`

Note: CUDA on Arch needs a matching driver. If `nvcc` and `nvidia-smi` disagree, update the driver and reboot.

## Syllabus

### Level 1 – The GPU model
- [ ] What a GPU is and how it differs from a CPU
- [ ] Threads, blocks, grids; `threadIdx`, `blockIdx`, `blockDim`
- [ ] Your first kernel: vector addition
- [ ] Host (CPU) vs device (GPU) memory, `cudaMalloc`, `cudaMemcpy`
- [ ] Error checking with `cudaGetLastError`

### Level 2 – Performance basics
- [ ] Memory hierarchy: global, shared, registers, constant
- [ ] Coalesced memory access
- [ ] Shared-memory tiling (matrix multiplication)
- [ ] Synchronisation: `__syncthreads()`, atomic operations
- [ ] Occupancy and block sizing

### Level 3 – Libraries and tools
- [ ] cuBLAS (matrix ops), cuFFT, cuRAND
- [ ] Thrust (C++ parallel algorithms)
- [ ] Streams and async copies
- [ ] Profiling with **Nsight Systems** and **Nsight Compute**
- [ ] CMake with CUDA (`project(... LANGUAGES CXX CUDA)`)

### Level 4 – Advanced
- [ ] Warp-level primitives (`__shfl_sync`)
- [ ] Tensor cores and mixed precision (FP16, BF16)
- [ ] Multi-GPU with NCCL
- [ ] Writing a custom CUDA op for PyTorch (`torch.utils.cpp_extension`)
- [ ] Triton (Python-based GPU kernels) as an alternative

## Resources

| | Resource | Notes |
|---|---|---|
| ⭐🆓 | [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/) | Official, the main reference |
| ⭐🆓 | [CUDA Toolkit documentation](https://docs.nvidia.com/cuda/) | All CUDA docs |
| 🆓 | [NVIDIA cuda-samples (GitHub)](https://github.com/NVIDIA/cuda-samples) | Working examples to read and modify |
| 🆓 | [NVIDIA Developer Blog – CUDA posts](https://developer.nvidia.com/blog/) | Optimisation articles |
| 🆓 | [NVIDIA Deep Learning Institute](https://www.nvidia.com/en-us/training/) | Free and paid courses, some free for beginners |
| 🆓 | [Triton language docs](https://triton-lang.org/) | Python GPU kernels |
| 💲 | *Programming Massively Parallel Processors* – Kirk & Hwu | The classic textbook |
| 💲 | *CUDA by Example* – Sanders & Kandrot | Hands-on intro |

## Projects

1. 🛠️ **Vector add** on the GPU, measure speed vs CPU
2. 🛠️ **Matrix multiplication**: naive, then tiled with shared memory
3. 🛠️ **Image grayscale / blur** kernel with PNG input (`stb_image`)
4. 🛠️ **Monte Carlo pi** with cuRAND
5. 🛠️ **Custom PyTorch op** that runs your CUDA kernel

## Tips

- Use `compute-sanitizer` to find memory errors in kernels.
- Measure before optimising. Use Nsight Systems first.
- A kernel with a bug can silently produce wrong numbers. Always test against a CPU version.
