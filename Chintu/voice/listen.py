from __future__ import annotations

from utils.logger import get_logger

logger = get_logger(__name__)


class Listener:
    """Speech-to-text adapter.

    Uses console text fallback when offline speech stack is unavailable.
    """

    def listen(self, prompt: str = "You> ") -> str:
        try:
            return input(prompt).strip()
        except EOFError:
            logger.warning("No stdin available for listener")
            return ""
