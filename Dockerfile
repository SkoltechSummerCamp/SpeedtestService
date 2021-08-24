FROM python:3.6-alpine

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

ENTRYPOINT ["python3"]

CMD ["server.py"]
