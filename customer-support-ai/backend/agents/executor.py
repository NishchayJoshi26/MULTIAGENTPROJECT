from __future__ import annotations

import json
from typing import Any, Dict

from backend.agents.llm_service import service as gemini_service
from backend.agents.prompts import BILLING_PROMPT, COMPLAINT_PROMPT, FAQ_PROMPT, PRODUCT_PROMPT, TECHNICAL_PROMPT


class BaseAgentExecutor:
    def __init__(self, agent_name: str, prompt: Dict[str, Any]) -> None:
        self.agent_name = agent_name
        self.prompt = prompt
        self.llm = gemini_service

    def execute(self, query: str, *, session_id: str, user_id: str) -> Dict[str, Any]:
        prompt_text = self._build_prompt(query)
        response = self.llm.generate(prompt_text, system_instruction=self._system_instruction())
        payload = self._parse_response(response)
        return {
            "selected_agent": self.agent_name,
            "confidence_score": payload.get("confidence_score", 0.8),
            "reasoning_summary": payload.get("reasoning_summary", "Generated from shared Gemini service"),
            "response": payload,
            "session_id": session_id,
            "user_id": user_id,
        }

    def _build_prompt(self, query: str) -> str:
        return json.dumps({"query": query, "prompt": self.prompt})

    def _system_instruction(self) -> str:
        return f"You are the {self.agent_name} agent. Follow the supplied prompt contract."

    def _parse_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "status": "ok",
            "summary": response.get("content", "No response"),
            "confidence_score": 0.82,
            "reasoning_summary": "Structured response generated from shared Gemini-backed service",
            "agent": self.agent_name,
        }


class BillingAgentExecutor(BaseAgentExecutor):
    def __init__(self) -> None:
        super().__init__("billing", BILLING_PROMPT)


class TechnicalAgentExecutor(BaseAgentExecutor):
    def __init__(self) -> None:
        super().__init__("technical", TECHNICAL_PROMPT)


class ProductAgentExecutor(BaseAgentExecutor):
    def __init__(self) -> None:
        super().__init__("product", PRODUCT_PROMPT)


class ComplaintAgentExecutor(BaseAgentExecutor):
    def __init__(self) -> None:
        super().__init__("complaint", COMPLAINT_PROMPT)


class FAQAgentExecutor(BaseAgentExecutor):
    def __init__(self) -> None:
        super().__init__("faq", FAQ_PROMPT)
