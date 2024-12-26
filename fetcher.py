import os
import socket
import platform
import distro
import psutil
from datetime import datetime

def get_user_info():
    user_name = os.getenv("USER")
    return user_name

def get_hostname():
    hostname = socket.gethostname()
    return hostname

def get_os_distribution():
    os_distribution = distro.name()
    return os_distribution

def get_os_architecture():
    architecture = platform.machine()
    return architecture

def get_os_kernel_info():
    kernel = platform.release()
    return kernel

def get_os_uptime():
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.now() - boot_time
    
    # Convert to hours, minutes, seconds
    days = uptime.days
    hours, remainder = divmod(uptime.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return f"{days}d {hours}h {minutes}m {seconds}s"

    
def main_menu():
    try:
        menu_list = [
            ("👤 User:", f'{get_user_info()}@{get_hostname()}'),
            ("🖥️ OS:", f'{get_os_distribution()} {get_os_architecture()}'),
            ("⚙️ Kernel:", f'{get_os_kernel_info()}'),
            ("⏱️ Uptime:", f'{get_os_uptime()}'),
        ]
    
        # fixed table width
        table_width = 50  # you can adjust this value
        content_width = table_width - 4  # subtract space for the border
        
        # top line
        print("\n╭" + "─" * table_width + "╮")
        print("│" + "Software Information".center(table_width) + "│")
        print("├" + "─" * table_width + "┤")
        
        # display data
        for label, value in menu_list:
            print(f"│ {label + ' ' + value:<{table_width-1}}│")
            
        # bottom line
        print("╰" + "─" * table_width + "╯")
            
    except Exception as e:
        print(f"Error gathering system information: {str(e)}")

    
if __name__ == "__main__":
    main_menu()
