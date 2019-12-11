import subprocess
import platform

# Get operating system of current platform
host_os = platform.system()

if host_os == "Darwin":
    # Replace arg in following line with path to .app file on Mac
    # subprocess.call("")
    print("I'm a Mac!")
elif host_os == "Linux":
    # Replace arg in following line with path to executable file on Linux
    # subprocess.call("")
    print("I run Linux!")
elif host_os == "Windows":
    subprocess.call("./data-vis-win32-x64/data-vis.exe")
