"""
Has functions which aid in fetching information needed for the dashboard from the SBC (Single Board Computer).
"""


def get_comm_status():
    """
    Fetches the communication status of the SBC.

    Returns:
        str: The communication status of the SBC.
    """
    return "Connected"


def get_cpu_usage():
    """
    Fetches the CPU usage of the SBC.

    Returns:
        str: The CPU usage of the SBC.
    """
    return "25%"


def get_ram_usage():
    """
    Fetches the RAM usage of the SBC.

    Returns:
        str: The RAM usage of the SBC.
    """
    return "50%"


def get_storage_usage():
    """
    Fetches the storage usage of the SBC.

    Returns:
        str: The storage usage of the SBC.
    """
    return "75%"


def get_error_count():
    """
    Fetches the error count of the SBC.

    Returns:
        str: The error count of the SBC.
    """
    return "0"


def get_battery_stats():
    """
    Fetches the battery stats of the SBC.

    Returns:
        str: The battery stats of the SBC.
    """
    return "100%"


def get_internal_temp():
    """
    Fetches the internal temperature of the SBC.

    Returns:
        str: The internal temperature of the SBC.
    """
    return "40°C"


def get_uptime():
    """
    Fetches the uptime of the SBC.

    Returns:
        str: The uptime of the SBC.
    """
    return "2 days"


def get_cpu_temp():
    """
    Fetches the CPU temperature of the SBC.

    Returns:
        str: The CPU temperature of the SBC.
    """
    return "50°C"


def get_aocs():
    """
    Fetches the AOCS (Attitude and Orbit Control System) of the SBC.

    Returns:
        str: The AOCS of the SBC.
    """
    return "Stable"


def get_camera_status():
    """
    Fetches the camera status of the SBC.

    Returns:
        str: The camera status of the SBC.
    """
    return "Connected"
