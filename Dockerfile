FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y python3 python3-pip

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY swagger_client/requirements.txt /usr/src/app
RUN pip3 install --no-cache-dir -r requirements.txt

COPY requirements.txt /usr/src/app
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000
EXPOSE 5001
EXPOSE 5001/udp

COPY swagger_client/ /usr/src/app/

CMD  python3 setup.py install --user

COPY iperf.elf /usr/src/app
COPY balancer_routine.py /usr/src/app
COPY server.py /usr/src/app
COPY iperf_wrapper.py /usr/src/app

CMD chmod +x iperf.elf
CMD chmod +x /usr/src/app/iperf.elf
CMD chmod a+rwx /usr/src/app/iperf.elf

ENTRYPOINT ["python3"]

CMD ["server.py"]
