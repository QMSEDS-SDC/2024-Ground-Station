"""
Has functions which aid in fetching information needed for the dashboard from the SBC (Single Board Computer).
"""

from typing import Dict
import random


def get_comm_status() -> bool:
    """
    Fetches the communication status of the SBC.

    Returns:
        dict: A dictionary containing:
            - time (int): Time when it was last checked (for now lets not care but should be UNIX timestamp)
            - status (bool): A random boolean value indicating the communication status. True means ok

    """

    time = random.randint(1739083186, 1739083186 + 3600 * 24 * 7)
    status = random.choice([True, False])

    return {"time": time, "status": status}


def get_cpu_usage() -> int:
    """
    Fetches the CPU usage of the SBC.

    Returns:
        - The CPU usage of the SBC in percentage.
    """

    percent = random.randint(25, 100)

    if percent >= 100 or percent <= 0:
        return None

    return percent


def get_ram_usage() -> int:
    """
    Fetches the RAM usage of the SBC.

    Returns:
        - The RAM usage of the SBC in percentage.
    """

    percent = random.randint(15, 100)

    if percent > 100 or percent < 0:
        return None

    return percent


def get_storage_usage() -> int:
    """
    Fetches the storage usage of the SBC.

    Returns:
        - The storage usage of the SBC in percentage.
    """

    percent = random.randint(40, 100)

    if percent > 100 or percent < 0:
        return None

    return percent


def get_error_count() -> Dict[str, int]:
    """
    Fetches the error count of the SBC.

    Returns:
        The error count of the SBC. The error count is a dictionary with the following keys:
        - error: The number of errors.
        - warning: The number of warnings
    """

    count_dict = {
        "error": random.randint(0, 5),
        "warning": random.randint(0, 5),
    }

    return count_dict


def get_battery_stats() -> Dict[str, int]:
    """
    Fetches the battery stats of the SBC.

    Returns:
        str: The battery stats of the SBC.
    """

    battery_dict = {
        "percentage": random.randint(0, 100),
        "voltage": random.randint(0, 12),
        "current": round(random.random() * 4, 2),
        "temp": random.randint(0, 40),
    }

    return battery_dict


def get_internal_temp() -> int:
    """
    Fetches the internal temperature of the SBC.

    Returns:
        The internal temperature of the SBC in Celsius.
    """

    temp = 25 + random.randint(0, 20)

    return temp


def get_uptime() -> int:
    """
    Fetches the uptime of the SBC.

    Returns:
        str: The uptime of the SBC in seconds.
    """

    uptime = random.randint(0, 1000000)

    return uptime


def get_cpu_temp() -> int:
    """
    Fetches the CPU temperature of the SBC.

    Returns:
        str: The CPU temperature of the SBC in Celsius.
    """

    cpu_temp = 50 + random.randint(0, 20)

    return cpu_temp


def get_aocs() -> Dict[str, int]:
    """
    Fetches the AOCS (Attitude and Orbit Control System) of the SBC.

    Returns:
        The AOCS of the SBC in a dictionary with the following keys
        - x: The x position of the SBC.
        - y: The y position of the SBC.
        - z: The z position of the SBC.
        - rpm: The RPM of the SBC.
        - mock sun sensor: The status of the mock sun sensor
    """

    aocs_dict = {
        "x_ang_rate": random.randint(0, 360),
        "y_ang_rate": random.randint(0, 360),
        "z_ang_rate": random.randint(0, 360),
        "x_pos": random.randint(0, 360),
        "y_pos": random.randint(0, 360),
        "z_pos": random.randint(0, 360),
        "rpm": random.randint(0, 1000),
        "mock_sun_sensor": random.choice([True, False]),
    }

    return aocs_dict


def get_comms_data() -> Dict[str, int]:
    """
    Fetches the communication data of the SBC.

    Returns:
        The communication data of the SBC in a dictionary with the following keys
        - uplink: The uplink data of the SBC.
        - downlink: The downlink data of the SBC.
        - signal_strength: The signal strength of the SBC.
        - data_rate: The data rate of the SBC.
    """

    comms_dict = {
        "uplink": random.randint(0, 100),
        "downlink": random.randint(0, 100),
        "signal_strength": random.randint(0, 100),
        "data_rate": random.randint(0, 100),
    }

    return comms_dict


def get_camera_status() -> bool:
    """
    Fetches the camera status of the SBC.

    Returns:
        The camera status of the SBC in boolean. True if the camera is active, False otherwise.
    """

    status = random.choice([True, False])

    return status
