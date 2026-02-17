from __future__ import annotations

from pathlib import Path

from utils.logger import get_logger

logger = get_logger(__name__)

try:
    from picamera2 import Picamera2
except Exception:
    Picamera2 = None


class Camera:
    def __init__(self):
        self.cam = None
        if Picamera2:
            self.cam = Picamera2()
            cfg = self.cam.create_still_configuration()
            self.cam.configure(cfg)
            self.cam.start()

    def capture_jpeg(self) -> bytes:
        if not self.cam:
            raise RuntimeError("Camera unavailable")
        path = "/tmp/chintu_latest.jpg"
        self.cam.capture_file(path)
        return Path(path).read_bytes()
