from __future__ import annotations

from ai.gemini_api import GeminiAPI
from core.state_manager import Emotion, StateManager
from utils.logger import get_logger
from vision.camera import Camera
from voice.speak import Speaker

logger = get_logger(__name__)


class SceneScanner:
    def __init__(self, camera: Camera, gemini: GeminiAPI, speaker: Speaker, state: StateManager):
        self.camera = camera
        self.gemini = gemini
        self.speaker = speaker
        self.state = state

    def scan_and_describe(self) -> str:
        self.state.set_emotion(Emotion.SCANNING)
        try:
            img = self.camera.capture_jpeg()
            text = self.gemini.ask_vision("Describe surroundings for a home robot.", img)
        except Exception as exc:
            logger.warning("Scan failed: %s", exc)
            text = "I could not scan right now because the camera or AI vision service is unavailable."
        self.speaker.say(text)
        self.state.set_emotion(Emotion.HAPPY)
        return text
