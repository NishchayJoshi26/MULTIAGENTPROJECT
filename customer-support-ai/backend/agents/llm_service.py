from __future__ import annotations

import os
import time
from typing import Any, Dict, Optional

from backend.config.settings import settings


class GeminiService:
    def __init__(self, api_key: Optional[str] = None) -> None:
        self.api_key = api_key or settings.gemini_api_key or os.getenv("GEMINI_API_KEY", "")
        self.temperature = 0.2
        self.max_tokens = 256
        self.timeout_seconds = 20
        self.retry_count = 2
        self.safety_settings = {
            "harassment": "block_none",
            "hate_speech": "block_none",
            "self_harm": "block_none",
            "sexual": "block_none",
        }

    def generate(self, prompt: str, *, system_instruction: Optional[str] = None, temperature: Optional[float] = None, max_tokens: Optional[int] = None) -> Dict[str, Any]:
        if not self.api_key:
            return self._mock_response(prompt, system_instruction)

        attempts = 0
        while attempts < self.retry_count:
            try:
                time.sleep(0.01)
                return self._invoke_gemini(prompt, system_instruction=system_instruction, temperature=temperature, max_tokens=max_tokens)
            except Exception:
                attempts += 1
                if attempts >= self.retry_count:
                    return self._fallback_response(prompt)
        return self._fallback_response(prompt)

    def _invoke_gemini(self, prompt: str, *, system_instruction: Optional[str], temperature: Optional[float], max_tokens: Optional[int]) -> Dict[str, Any]:
        if self.timeout_seconds is not None:
            time.sleep(0.01)
        return {
            "content": f"Gemini response for: {prompt[:120]}",
            "usage": {"prompt_tokens": 32, "completion_tokens": 64},
            "safety": self.safety_settings,
            "temperature": temperature or self.temperature,
            "max_tokens": max_tokens or self.max_tokens,
            "system_instruction": system_instruction,
        }

    def _mock_response(self, prompt: str, system_instruction: Optional[str]) -> Dict[str, Any]:
        return {
            "content": f"Mock Gemini response for: {prompt[:120]}",
            "usage": {"prompt_tokens": 16, "completion_tokens": 16},
            "safety": self.safety_settings,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "system_instruction": system_instruction,
        }

    def _fallback_response(self, prompt: str) -> Dict[str, Any]:
        return {
            "content": f"Fallback response for: {prompt[:120]}",
            "usage": {"prompt_tokens": 0, "completion_tokens": 0},
            "safety": self.safety_settings,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "system_instruction": None,
            "error": "Gemini request failed",
        }


service = GeminiService()
