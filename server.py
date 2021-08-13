from flask import Flask
from flask import request
from iperf_wrapper import Iperf_wrapper


app = Flask(__name__)

iperf: Iperf_wrapper = Iperf_wrapper(verbose=True)


@app.route("/start-iperf", methods=['GET'])
def start_iperf_binary():
    global iperf

    iperf_parameters = request.args.get("args")
    if iperf_parameters is not None:
        iperf.iperf_parameters = iperf_parameters

    status = iperf.start()
    if status:
        return f"iPerf started with parameters {iperf.iperf_parameters}"

    iperf.stop()
    status = iperf.start()
    if status:
        return f"iPerf restarted with parameters {iperf.iperf_parameters}"

    return "Error"


@app.route("/stop-iperf", methods=['GET'])
def stop_iperf():
    global iperf

    if iperf.is_started:
        status = iperf.stop()
        return str(f"iPerf server stopped with status {status}")

    return "iPerf already stopped"


app.run()
