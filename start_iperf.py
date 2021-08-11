import shlex
import argparse
import subprocess
from threading import Thread
from queue import Queue


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-p', '--parameters', type=str, action="store", default='-s')

    return parser


def logger_thread(stream, file, verbose):

    def logger(stream, file, verbose):
        for stdout_line in iter(stream.readline, ""):
            file.writelines(stdout_line)
            if verbose:
                print(stdout_line.replace('\n', ""))
        stream.close()
        file.close()

    t = Thread(target=logger, args=(stream, file, verbose))
    t.daemon = True
    t.start()
    return t


def start_iperf(parameters: str, verbose=False):
    output_file = open("iperf_log.txt", 'w')
    error_file = open("iperf_errors.txt", 'w')

    cmd = shlex.split("./iperf " + parameters)
    iperf_process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    print("Iperf sever is started")

    threads = []
    if iperf_process.stdout is not None:
        threads.append(logger_thread(iperf_process.stdout, output_file, verbose))

    if iperf_process.stderr is not None:
        threads.append(logger_thread(iperf_process.stderr, error_file, verbose))

    try:
        return_code = iperf_process.wait()
    except:
        iperf_process.kill()
        return_code = iperf_process.returncode
        for t in threads:
            t.join()
    print(f"Iperf server stopped with status {return_code}")
    return return_code


if __name__ == "__main__":
    arg_parser = create_arg_parser()
    namespace = arg_parser.parse_args()

    out = start_iperf(namespace.parameters, namespace.verbose)