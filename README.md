<div align="center">

# IronBCI-32

**32 channels of EEG over a single USB cable.**

Low-cost, open-source 32-channel, 24-bit biosignal acquisition board with four AD7771 converters and an STM32H7.

[📖 Documentation](https://docs.pieeg.com/hardware/devices/ironbci-32/) ·
[🚀 How to Start](https://docs.pieeg.com/hardware/devices/ironbci-32/setup/) ·
[🛒 Buy](https://www.elecrow.com/ironbci-32.html) ·
[💬 Discord](https://discord.gg/5Ps24p47)

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/ironbci32_board.jpg" alt="IronBCI-32 board" width="460">

</div>

> [!WARNING]
> IronBCI-32 is **not a medical device** and has not been certified by any regulator for use with the human body. It is a tool for research, education and engineering. You use it at your own risk.

> [!CAUTION]
> **Battery only, for everything.** Power the board from a **5 V USB battery**, and run the laptop on the data cable **on its own battery, unplugged from the wall**. No desktop PCs, no wall chargers. The board has **no isolation**. Read the [Safety page](https://docs.pieeg.com/hardware/devices/ironbci-32/safety/) and the [liability notice](https://pieeg.com/liability/).

## At a glance

| | |
|---|---|
| **Channels** | 32 biosignal inputs, plus reference and bias |
| **Converters** | 4 × AD7771, 8 channels each, 24-bit |
| **Noise** | Ultra-low-noise sources and references, below 0.22 µV |
| **Microcontroller** | STM32H743 (Arm Cortex-M7), real-time pre-processing |
| **Sample rate** | About 500 SPS (BrainFlow reports 512 Hz) |
| **Signals** | EEG, EMG, ECG, EOG |
| **Link** | USB serial (virtual COM port), 921,600 baud |
| **Electrodes** | Dry or wet Ag/AgCl, 4 × 2.54 mm double-row headers |
| **Power** | 5 V USB battery only, on its own USB port |
| **PCB** | 70 × 70 mm, 4 layers, 1.6 mm FR4 |
| **Software** | [BrainFlow](https://brainflow.readthedocs.io/en/stable/SupportedBoards.html#ironbci32) (`IRONBCI_32_BOARD`), [PiEEG Server](https://github.com/pieeg-club/PiEEG-server), [PiEEG Cloud](https://cloud.pieeg.com) |

## How it works

```
 32 electrodes ──► 4 × AD7771 ──► STM32H7 ──USB──► Laptop (on battery)
 Ref + bias (ears)  (8 ch each)      ▲                ├ BrainFlow
                                     │                ├ PiEEG Server
           5 V USB battery ──USB─────┘                └ cloud.pieeg.com
```

Two Micro USB ports: **Power** (from the battery) and **Data Stream** (to the laptop). The board starts streaming as soon as it is powered.

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/ironbci32_power_data.jpg" alt="Power and data USB ports on IronBCI-32" width="400">

## Quick start

1. **Unplug the laptop** from its charger and run it on battery.
2. **Connect the electrodes** to the four headers (bottom row, see below). Reference and bias ear clips go on the **CH 1–8** header.
3. **Plug the 5 V USB battery** into the **Power** port.
4. **Plug a data cable** (not charge-only) from the **Data Stream** port to the laptop. Note the serial port (`COM3`, `/dev/ttyACM0`…).
5. **Stream:**

```bash
pip install "pieeg-server[ironbci32]"
pieeg-server --device ironbci32 --serial-port COM3            # Windows
pieeg-server --device ironbci32 --serial-port /dev/ttyACM0    # Linux / macOS
```

Then open `http://localhost:1617`. You should see 32 channels.

Full walkthrough: **[docs.pieeg.com → IronBCI-32 → How to Start](https://docs.pieeg.com/hardware/devices/ironbci-32/setup/)**

## Wiring

Four headers, one per AD7771:

| Header | Channels | Also carries |
|---|---|---|
| Bottom left | **1–8** | **Reference and bias ear clips** |
| Top left | 9–16 | |
| Top right | 17–24 | |
| Bottom right | 25–32 | |

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/ironbci32_wiring.jpg" alt="IronBCI-32 wiring: four headers, reference and bias on the CH 1–8 header" width="700">

> [!IMPORTANT]
> Each header has **two rows**. Electrodes go on the **bottom row** (closest to the board). The **top row** is the reference row: an electrode there is shorted to REF and shows a **flat, dead channel**. Never connect anything to the AVSS / AVDD power pins at the end of each header.

**Pin order on each header** (looking into the connector, chips up, left → right):

| Header | Bottom-row pins | Pin-1 end |
|---|---|---|
| CH 1–8 | AVDD · 8 · 7 · 6 · 5 · 1 · 2 · 3 · 4 | BIAS |
| CH 9–16 | AVDD · 16 · 15 · 14 · 13 · 9 · 10 · 11 · 12 | BIAS |
| CH 17–24 | AVDD · 20 · 19 · 18 · 17 · 21 · 22 · 23 · 24 | BIAS |
| CH 25–32 | AVDD · 28 · 27 · 26 · 25 · 29 · 30 · 31 · 32 | BIAS |

The reference ear clip goes on the **top row, pin 1** of the CH 1–8 header; the bias clip on the **bottom row, pin 2**.

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/ironbci32_connectors.png" alt="IronBCI-32 connector diagram: top, side and front views with channel numbers" width="800">

### Electrode layout

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/ironbci32_electrode_map.png" alt="32-channel electrode layout on the 10-20 system" width="420">

| Ch | Pos | Ch | Pos | Ch | Pos | Ch | Pos |
|---|---|---|---|---|---|---|---|
| 1 | F7 | 9 | C3 | 17 | Pz | 25 | Fp2 |
| 2 | FT7 | 10 | FC3 | 18 | Oz | 26 | F8 |
| 3 | T7 | 11 | F3 | 19 | O2 | 27 | FT8 |
| 4 | TP7 | 12 | Fp1 | 20 | P4 | 28 | T8 |
| 5 | P7 | 13 | Fz | 21 | CP4 | 29 | TP8 |
| 6 | O1 | 14 | FCz | 22 | C4 | 30 | P8 |
| 7 | P3 | 15 | Cz | 23 | FC4 | 31 | Fpz |
| 8 | CP3 | 16 | CPz | 24 | F4 | 32 | POz |

Matches the [PiEEG 32-channel wet cap](https://www.pieeg.com/hardware/32ch-wet-cap).

## Software

### BrainFlow

IronBCI-32 is supported in [BrainFlow](https://brainflow.readthedocs.io/en/stable/SupportedBoards.html#ironbci32) as `BoardIds.IRONBCI_32_BOARD` (ID 65):

```python
import time
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds

params = BrainFlowInputParams()
params.serial_port = "COM3"              # or "/dev/ttyACM0"

board = BoardShim(BoardIds.IRONBCI_32_BOARD, params)
board.prepare_session()
board.start_stream()
time.sleep(10)
data = board.get_board_data()
board.stop_stream()
board.release_session()
```

### Example scripts (this repo)

All in [`SDK`](SDK), using BrainFlow (tested with BrainFlow 5.20.1, Python 3.12.4):

| Script | What it does |
|---|---|
| [`Real_time_visualisation/1.One_ch_plot.py`](SDK/Real_time_visualisation/1.One_ch_plot.py) | Live plot of one channel |
| [`Real_time_visualisation/2.All_channels.py`](SDK/Real_time_visualisation/2.All_channels.py) | Live plot of all 32 channels |
| [`Save_data/1.Save_5_sec_1ch.py`](SDK/Save_data/1.Save_5_sec_1ch.py) | Record 5 seconds of one channel |
| [`Save_data/2.All_ch.py`](SDK/Save_data/2.All_ch.py) | Record 10 seconds of all 32 channels to Excel |
| [`Not_real_time/Plot_data.py`](SDK/Not_real_time/Plot_data.py) | Plot a saved file with an 8–12 Hz filter and wavelet view |

```bash
pip install brainflow pyqtgraph PyQt5 pandas openpyxl scipy matplotlib PyWavelets
cd SDK/Real_time_visualisation
python 2.All_channels.py --serial-port COM3       # or /dev/ttyACM0
```

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/ironbci32_brainflow.png" alt="32 channels streaming in BrainFlow" width="600">

### PiEEG Server and PiEEG Cloud

- **PiEEG Server:** `pip install "pieeg-server[ironbci32]"`, then `pieeg-server --device ironbci32 --serial-port COM3`. Dashboard, recording, WebSocket, LSL.
- **PiEEG Cloud:** open [cloud.pieeg.com](https://cloud.pieeg.com) in Chrome or Edge → **PiEEG Devices** → **IronBCI-32** (Web Serial, no install).

All options: **[Software docs](https://docs.pieeg.com/hardware/devices/ironbci-32/software/)**

## Example signals

**EEG: alpha test** (eyes closed and open, dry Ag/AgCl electrodes, no gel)

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/ironbci32_alpha.png" alt="Alpha test with wavelet power spectrum" width="650">

**Dataset:** [`dataset/eeg_32ch_20s.xlsx`](dataset): 32 channels, about 20 s, recorded with the PiEEG 32-channel wet cap.

## Firmware

The board ships with firmware installed. To update it, connect an **ST-Link** to the SWD header (GND, RST, SWDIO, SWCLK), power the board from the battery, and flash [`hex/ironbci32.hex`](hex) with STM32CubeProgrammer.

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/ironbci32_stlink.jpg" alt="ST-Link wiring to IronBCI-32" width="380">

Step by step: [Firmware docs](https://docs.pieeg.com/hardware/devices/ironbci-32/firmware/). STM32H743 source (beta): [`Framework`](Framework).

## What's in this repository

| Folder | Content |
|---|---|
| [`SDK`](SDK) | BrainFlow example scripts: real-time plots, saving, plotting saved data |
| [`dataset`](dataset) | 32-channel, 20-second EEG recording |
| [`hex`](hex) | Ready-to-flash firmware and ST-Link wiring photo |
| [`Framework`](Framework) | STM32H743 firmware project (Makefile, GCC, OpenOCD) |
| [`Electrical`](Electrical) | KiCad schematic and PDF |
| [`Gerber`](Gerber) | Gerber files for PCB manufacturing |
| [`images`](images), [`start`](start) | Images used in the original README |

## Documentation

| Page | |
|---|---|
| [IronBCI-32 Intro](https://docs.pieeg.com/hardware/devices/ironbci-32/) | Overview, comparison with other boards |
| [What's in the Box](https://docs.pieeg.com/hardware/devices/ironbci-32/required-equipment/) | What you need besides the board |
| [How to Start](https://docs.pieeg.com/hardware/devices/ironbci-32/setup/) | Step-by-step setup and first signal checks |
| [Electrodes & Pinout](https://docs.pieeg.com/hardware/devices/ironbci-32/connections/) | Headers, top/bottom rows, pin order, electrode layout |
| [Software](https://docs.pieeg.com/hardware/devices/ironbci-32/software/) | PiEEG Server, BrainFlow, PiEEG Cloud, scripts |
| [Signals & Datasets](https://docs.pieeg.com/hardware/devices/ironbci-32/examples/) | Example recordings and dataset |
| [Firmware](https://docs.pieeg.com/hardware/devices/ironbci-32/firmware/) | Flashing with ST-Link, building from source |
| [Specification](https://docs.pieeg.com/hardware/devices/ironbci-32/specification/) | Hardware, serial frame format, µV conversion |
| [Troubleshooting](https://docs.pieeg.com/hardware/devices/ironbci-32/troubleshooting/) | USB, serial, software and signal fixes |
| [Safety](https://docs.pieeg.com/hardware/devices/ironbci-32/safety/) | Battery-only operation for the board and the laptop |

## Video

[IronBCI-32 demo on YouTube](https://youtu.be/HehUNOKghSM) · 3D-printable boxes on [Thingiverse](https://www.thingiverse.com/PiEEG/designs)

## Acknowledgements

Thank you to [Dmitry](https://github.com/dmitry-sukhoruchkin) for supporting this project.

## Contact

- 🌐 [pieeg.com](https://pieeg.com/)
- 📖 [docs.pieeg.com](https://docs.pieeg.com/)
- 💬 [Discord](https://discord.gg/5Ps24p47)
- ✉️ [pieeg@pieeg.com](mailto:pieeg@pieeg.com)
