# SpeedtestService
## Usage

**iperf binary is placed in the same directory as `start_iperf.py` script.**

Basic usage:
```bash
python3 start_iperf.py 
```
Pass parameters to iperf:
```bash
python3 start_iperf.py -p='-s -t 10'
```
Print logs to stdin:
```bash
python3 start_iperf.py -v 
```
