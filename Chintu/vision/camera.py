from __future__ import annotations

from pathlib import Path

from utils.logger import get_logger

logger = get_logger(__name__)

try:
    from picamera2 import Picamera2
except Exception:
    Picamera2 = None


class Camera:
    """Safe Picamera2 wrapper.

    Handles Raspberry Pi camera-missing cases gracefully so app startup does not crash.
    """

    def __init__(self) -> None:
        self.cam = None
        self.available = False

        if not Picamera2:
            logger.warning("Picamera2 is not installed; camera module running in fallback mode")
            return

        try:
            cameras = Picamera2.global_camera_info()
            if not cameras:
                logger.warning("No Pi Camera detected")
                return

            self.cam = Picamera2(camera_num=0)
            cfg = self.cam.create_still_configuration(main={"size": (640, 480)})
            self.cam.configure(cfg)
            self.cam.start()
            self.available = True
            logger.info("Camera initialized successfully")
        except Exception as exc:
            logger.exception("Camera init failed, continuing without camera: %s", exc)
            self.cam = None
            self.available = False

    def capture_jpeg(self) -> bytes:
        if not self.cam or not self.available:
            raise RuntimeError("Camera unavailable")

        path = "/tmp/chintu_latest.jpg"
        self.cam.capture_file(path)
        return Path(path).read_bytes()

    def close(self) -> None:
        if self.cam:
            try:
                self.cam.stop()
            except Exception:
                pass
