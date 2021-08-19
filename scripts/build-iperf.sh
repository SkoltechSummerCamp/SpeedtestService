#/bin/sh
cd iPerf
bash configure
make
cd ..
mv iPerf/src/iperf iperf.elf

