# Scroll pHAT Simulator

A Tk based server to simulate Scroll pHAT on your Windows, Linux or macOS PC.

![pacman running in Scroll pHAT simulator](simulator.gif)

Works by hijacking the `smbus` module imported by `scrollphat` and replacing it with a FIFO pipe to the Tk based simulator.

## Usage

Set the `PYTHONPATH` variable to the simulator directory and run an example. The fake `smbus` will be loaded instead of the real one and output will launch in a new window:

```
PYTHONPATH=simulator python3 examples/pacman.py
```
