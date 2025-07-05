from pathlib import Path

from sunspec2.file.client import FileClientDevice  # type: ignore
from sunspec2.device import Device  # type: ignore


example_device_file = Path(__file__).parent / "example_devices" / "device_1547.json"


def get_example_device() -> Device:
    return FileClientDevice(example_device_file)
