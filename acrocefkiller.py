import psutil
import time

TARGET_PROCESS = "AcroCEF.exe"

def kill_process_by_name(process_name):
    for proc in psutil.process_iter(attrs=["pid", "name"]):
        if proc.info["name"] == process_name:
            try:
                proc.terminate()  # Try normal termination
                time.sleep(0.5)
                if proc.is_running():
                    proc.kill()  # Force kill if still running
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass  # Ignore errors

if __name__ == "__main__":
    while True:
        kill_process_by_name(TARGET_PROCESS)
        time.sleep(2)  # Run in the background, checking every 2 seconds
