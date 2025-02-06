"""
Has functions which aid in fetching information needed for the dashboard from the SBC (Single Board Computer).
"""

from typing import Dict
import random


def get_comm_status() -> bool:
    """
    Fetches the communication status of the SBC.

    Returns:
        - The communication status of the SBC. True if the communication is active, False otherwise.
    """

    status = random.choice([True, False])
    return status


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
        "x": random.randint(-180, 180),
        "y": random.randint(-180, 180),
        "z": random.randint(-180, 180),
        "rpm": random.randint(0, 1000),
        "mock sun sensor": random.choice([True, False]),
    }

    return aocs_dict


def get_camera_status() -> bool:
    """
    Fetches the camera status of the SBC.

    Returns:
        The camera status of the SBC in boolean. True if the camera is active, False otherwise.
    """

    status = random.choice([True, False])

    return status
