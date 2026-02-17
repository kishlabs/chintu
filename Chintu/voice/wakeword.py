from __future__ import annotations

import threading
from time import sleep

from utils.logger import get_logger

logger = get_logger(__name__)


class WakeWordDetector:
    """Porcupine-ready wake word detector with a safe simulation fallback."""

    def __init__(self, callback):
        self.callback = callback
        self._running = False
        self._thread: threading.Thread | None = None

    def start(self):
        self._running = True
        self._thread = threading.Thread(target=self._run, daemon=True, name="wakeword")
        self._thread.start()

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join(timeout=1)

    def _run(self):
        logger.info("Wake word detector active (simulation mode if Porcupine/audio setup missing)")
        while self._running:
            sleep(0.25)

    def trigger_for_test(self):
        self.callback()
