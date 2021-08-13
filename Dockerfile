FROM alpine:latest
RUN apk add --no-cache python3 py3-pip gcompat libstdc++6

WORKDIR /SpeedtestService
EXPOSE 5000
EXPOSE 5001
EXPOSE 5001/udp

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
# COPY iPerf/src/iperf iperf
# COPY server.py server.py
# COPY iperf_wrapper.py iperf_wrapper.py
# CMD python3 server.py
