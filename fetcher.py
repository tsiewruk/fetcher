from datetime import datetime
import platform
import os
import socket
import distro
import psutil
import wmi

def get_user_name():
    user_name = os.getenv("USERNAME") or os.getenv("USER")
    return user_name or "Unknown"  # Added fallback value

def get_hostname():
    hostname = socket.gethostname()
    return hostname

def get_os_info():
    if platform.system() == "Linux":
        os_name = distro.name(pretty=True)
    elif platform.system() == "Windows":
        os_name = f"Windows {platform.win32_ver()[0]}"  # Added "Windows" prefix
    elif platform.system() == "Darwin":
        os_name = f"macOS {platform.mac_ver()[0]}"
    else:
        os_name = platform.system()
    return os_name

def get_hardware_model():
    try:
        if platform.system() == "Linux":
            with open("/sys/devices/virtual/dmi/id/product_family", "r") as f:
                return f.read().strip()
        elif platform.system() == "Darwin":
            import subprocess
            cmd = "system_profiler SPHardwareDataType | grep 'Model Name'"
            result = subprocess.check_output(cmd, shell=True).decode()
            return result.split(":")[1].strip()
        elif platform.system() == "Windows":
            c = wmi.WMI()
            system = c.Win32_ComputerSystem()[0]
            return f"{system.Manufacturer} {system.Model}"
        return "Unknown"
    except Exception as e:
        return f"Unable to determine hardware model: {str(e)}"

def get_architecture():
    architecture = platform.machine()
    return architecture

def get_kernel_version():
    kernel_version = platform.uname().release
    return kernel_version

def get_uptime():
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.now() - boot_time
    
    # Convert to hours, minutes, seconds
    days = uptime.days
    hours, remainder = divmod(uptime.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    if days > 0:
        return f"{days}d {hours}h {minutes}m {seconds}s"
    else:
        return f"{hours}h {minutes}m {seconds}s"

def main_menu():
    try:
        print(f"\nSystem Information")
        print("-" * 30)
        print(f"Host: {get_hostname()}@{get_user_name()}")
        print(f"OS: {get_os_info()} ({get_architecture()})")
        print(f'Hardware: {get_hardware_model()}')
        print(f"Kernel: {get_kernel_version()}")
        print(f"Uptime: {get_uptime()}")
        print("-" * 30)
    except Exception as e:
        print(f"Error gathering system information: {str(e)}")

if __name__ == "__main__":
    main_menu()