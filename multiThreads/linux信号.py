import signal
import subprocess

def itout():
    print("signal is end")

signal.signal(signal.SIGINT, itout)

ping_process = subprocess.Popen(args=["ping www.baidu.com"], shell=True)
ping_process.wait()
print(ping_process.pid)
print(ping_process.returncode)
