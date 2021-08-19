from flask import Flask
from flask import request
from iperf_wrapper import *

from balancer_routine import *

app = Flask(__name__)

iperf: Iperf_wrapper = Iperf_wrapper(verbose=True)


@app.route("/start-iperf", methods=['GET'])
def start_iperf_binary():
    global iperf

    iperf_parameters = request.args.get("args")
    if iperf_parameters is not None:
        iperf.iperf_parameters = iperf_parameters

    status = iperf.start(port=env_data['IPERF_PORT'])
    if status:
        return f"iPerf started with parameters {iperf.iperf_parameters}"

    iperf.stop()
    status = iperf.start(port=env_data['IPERF_PORT'])
    if status:
        return f"iPerf restarted with parameters {iperf.iperf_parameters}"

    return "Error"


@app.route("/stop-iperf", methods=['GET'])
def stop_iperf():
    global iperf

    if iperf.is_started:
        status = iperf.stop()
        balancer_routine.post_to_server(port=int(env_data['IPERF_PORT']))
        return str(f"iPerf stopped with status {status}")

    return "iPerf already stopped"

def TimeoutHandler():
    if iperf.is_started:
        status = iperf.stop()
    balancer_routine.post_to_server(port=int(env_data['IPERF_PORT']))
    watchdog.reset()


env_data = read_env_data()
#watchdog = Watchdog(env_data['CONNECTING_TIMEOUT'], TimeoutHandler)
balancer_routine.post_to_server(port=int(env_data['IPERF_PORT']))
app.run(host="0.0.0.0", port="5000")


