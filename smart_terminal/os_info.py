import platform
import os

# Basic OS type and architecture
OPERATING_SYSTEM = platform.system()            # OS Type (Linux, Windows, macOS, etc.)
ARCHITECTURE = platform.machine()               # Architecture (x86_64, ARM, etc.)

# Retrieve a simplified OS name and version
if OPERATING_SYSTEM == "Linux":
    try:
        # Get distribution name and version from /etc/os-release
        with open("/etc/os-release") as f:
            os_info = dict(line.strip().split('=') for line in f if '=' in line)
            OS_NAME = os_info.get("NAME", "Linux")  # e.g., "Ubuntu"
            OS_VERSION = os_info.get("VERSION_ID", "Unknown")  # e.g., "22.04"
    except FileNotFoundError:
        OS_NAME, OS_VERSION = "Linux", "Unknown"
elif OPERATING_SYSTEM == "Windows":
    OS_NAME = "Windows"
    OS_VERSION = platform.release()               # e.g., "10" or "11"
elif OPERATING_SYSTEM == "Darwin":
    OS_NAME = "macOS"
    OS_VERSION = platform.mac_ver()[0]            # e.g., "10.15.7"
else:
    OS_NAME, OS_VERSION = OPERATING_SYSTEM, "Unknown"

# Store all information in a dictionary for easy access
SYSTEM_INFO = {
    "Operating System": OPERATING_SYSTEM,
    "OS Name": OS_NAME,           # e.g., "Ubuntu", "Windows", "macOS"
    "OS Version": OS_VERSION,     # Simplified version, e.g., "22.04", "10"
    "Architecture": ARCHITECTURE,
}

def print_system_info():
    """Prints the system information for debugging or logging."""
    for key, value in SYSTEM_INFO.items():
        print(f"{key}: {value}")
