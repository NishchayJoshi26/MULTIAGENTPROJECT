from __future__ import annotations

from typing import Any, Dict, List


class ConversationMemory:
    def __init__(self) -> None:
        self.entries: List[Dict[str, Any]] = []

    def store(self, *, session_id: str, user_id: str, user_message: str, ai_response: str, selected_agents: List[str], timestamp: str, confidence_score: float) -> Dict[str, Any]:
        entry = {
            "session_id": session_id,
            "user_id": user_id,
            "user_message": user_message,
            "ai_response": ai_response,
            "selected_agents": selected_agents,
            "timestamp": timestamp,
            "confidence_score": confidence_score,
        }
        self.entries.append(entry)
        return entry

    def get_session(self, session_id: str) -> List[Dict[str, Any]]:
        return [entry for entry in self.entries if entry.get("session_id") == session_id]
