from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class DisplayConfig:
    width: int = 800
    height: int = 480
    fps: int = 60
    fullscreen: bool = True


@dataclass(frozen=True)
class MotorConfig:
    ena_pin: int = 12
    in1_pin: int = 5
    in2_pin: int = 6
    enb_pin: int = 13
    in3_pin: int = 20
    in4_pin: int = 21
    pwm_hz: int = 1000


@dataclass(frozen=True)
class AIConfig:
    ollama_url: str = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434/api/generate")
    ollama_model: str = os.getenv("OLLAMA_MODEL", "phi3:mini")
    gemini_model: str = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
    gemini_api_key: str | None = os.getenv("GEMINI_API_KEY")
    request_timeout_s: int = int(os.getenv("AI_TIMEOUT", "20"))


@dataclass(frozen=True)
class VoiceConfig:
    wake_word: str = os.getenv("WAKE_WORD", "hey chintu")
    inactivity_sleep_s: int = 120


@dataclass(frozen=True)
class CameraConfig:
    width: int = 640
    height: int = 480


@dataclass(frozen=True)
class AppConfig:
    display: DisplayConfig = DisplayConfig()
    motor: MotorConfig = MotorConfig()
    ai: AIConfig = AIConfig()
    voice: VoiceConfig = VoiceConfig()
    camera: CameraConfig = CameraConfig()


CONFIG = AppConfig()
