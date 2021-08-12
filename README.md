# SpeedtestService
[![Build Status](https://github.com/SkoltechSummerCamp/SpeedtestService/workflows/Build%20iPerf/badge.svg)](https://github.com/SkoltechSummerCamp/SpeedtestService/actions)
## Usage

**iPerf binary is placed in the same directory as `start_iperf.py` script.**

Basic usage (iPerf runs with arguments `-s -u`):
```bash
python3 start_iperf.py 
```
Pass parameters to iPerf:
```bash
python3 start_iperf.py -p='-s -t 10'
```
Print logs to stdin:
```bash
python3 start_iperf.py -V 
```
Both:
```bash
python3 start_iperf.py -V -p='-s -t 10'
```
