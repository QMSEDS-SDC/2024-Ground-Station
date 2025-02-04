"""
Has functions which aid in fetching information needed for the dashboard from the SBC (Single Board Computer).
"""

from typing import Dict


def get_comm_status() -> bool:
    """
    Fetches the communication status of the SBC.

    Returns:
        - The communication status of the SBC. True if the communication is active, False otherwise.
    """

    status = True
    return status


def get_cpu_usage() -> int:
    """
    Fetches the CPU usage of the SBC.

    Returns:
        - The CPU usage of the SBC in percentage.
    """

    percent = 25

    if percent >= 100 or percent <= 0:
        return None

    return percent


def get_ram_usage() -> int:
    """
    Fetches the RAM usage of the SBC.

    Returns:
        - The RAM usage of the SBC in percentage.
    """

    percent = 25

    if percent > 100 or percent < 0:
        return None

    return percent


def get_storage_usage() -> int:
    """
    Fetches the storage usage of the SBC.

    Returns:
        - The storage usage of the SBC in percentage.
    """

    percent = 75

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
        "error": 0,
        "warning": 0,
    }

    return count_dict


def get_battery_stats() -> Dict[str, int]:
    """
    Fetches the battery stats of the SBC.

    Returns:
        str: The battery stats of the SBC.
    """

    battery_dict = {
        "percentage": 100,
        "voltage": 12,
        "current": 1,
    }

    return battery_dict


def get_internal_temp() > int:
    """
    Fetches the internal temperature of the SBC.

    Returns:
        The internal temperature of the SBC in Celsius.
    """

    temp = 40

    return temp


def get_uptime() -> int:
    """
    Fetches the uptime of the SBC.

    Returns:
        str: The uptime of the SBC in seconds.
    """

    uptime = 1000

    return uptime


def get_cpu_temp() -> int:
    """
    Fetches the CPU temperature of the SBC.

    Returns:
        str: The CPU temperature of the SBC in Celsius.
    """

    cpu_temp = 50

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
        "x": 0,
        "y": 0,
        "z": 0,
        "rpm": 0,
        "mock sun sensor": True,
    }

    return aocs_dict


def get_camera_status() -> bool:
    """
    Fetches the camera status of the SBC.

    Returns:
        The camera status of the SBC in boolean. True if the camera is active, False otherwise.
    """

    status = True

    return status
