from __future__ import annotations

from typing import Any, Dict, Optional


class EscalationService:
    def evaluate(self, response: Dict[str, Any], *, repeated_failures: int = 0, user_requested_human: bool = False, threshold: float = 0.6) -> Dict[str, Any]:
        confidence_score = float(response.get("confidence_score", 0.0))
        severity = response.get("response", {}).get("severity", "low")
        should_escalate = False
        escalation_level = "none"

        if user_requested_human or repeated_failures >= 2 or severity == "high" or confidence_score < threshold:
            should_escalate = True
            escalation_level = "human_support"

        return {
            "should_escalate": should_escalate,
            "escalation_level": escalation_level,
            "reason": "Confidence below threshold or escalation trigger present",
        }
