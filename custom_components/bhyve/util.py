import hashlib
from homeassistant.util import dt


def orbit_time_to_local_time(timestamp: str):
    if timestamp is not None:
        return dt.as_local(dt.parse_datetime(timestamp))
    return None


def anonymize(device):
    device["address"] = "REDACTED"
    device["full_location"] = "REDACTED"
    device["location"] = "REDACTED"
    return device


def pesudo_id_if_smart_program(
    device_id, program_id, is_smart_program: bool = False
):
    """
    Compute a pesudo ID to ensure the Smart program has a constant ID for events.

    Devices with multiple zones can change the `program_id` used by the Smart
    Watering program based on which zones are included in the program.
    return: pesudo `program_id` for Smart program, otherwise real `program_id`.
    """
    if is_smart_program:
        program_id = hashlib.md5(
            f"{device_id}:smart_program".encode('utf-8')
        ).hexdigest()
    return program_id
