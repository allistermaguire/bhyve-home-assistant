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

def constant_program_id(device_id, program_id, is_smart_program: bool=False):
    """For devices with multiple zones, Smart program id changes depending on the zone/s that are included. 
        Generate a constant id so that it is updated on change."""
    if is_smart_program:
        program_id = hashlib.md5("{}:smart_program".format(device_id).encode('utf-8')).hexdigest()
    return program_id
