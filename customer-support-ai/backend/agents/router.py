from __future__ import annotations

from typing import Any, Dict, List, Optional

from backend.agents.aggregator import ResponseAggregator
from backend.agents.escalation import EscalationService
from backend.agents.executor import (
    BillingAgentExecutor,
    ComplaintAgentExecutor,
    FAQAgentExecutor,
    ProductAgentExecutor,
    TechnicalAgentExecutor,
)
from backend.agents.memory import ConversationMemory
from backend.agents.prompts import (
    BILLING_PROMPT,
    COMPLAINT_PROMPT,
    FAQ_PROMPT,
    INTENT_DETECTION_PROMPT,
    PRODUCT_PROMPT,
    TECHNICAL_PROMPT,
)


class IntentDetectionAgent:
    def __init__(self) -> None:
        self.prompt = INTENT_DETECTION_PROMPT

    def detect(self, query: str) -> Dict[str, Any]:
        lowered = query.lower()
        billing_keywords = {"billing", "charge", "invoice", "refund"}
        technical_keywords = {"technical", "error", "bug", "printer", "issue"}
        product_keywords = {"product", "feature", "manual", "device"}
        complaint_keywords = {"complaint", "angry", "bad", "frustrated"}

        billing_hit = any(keyword in lowered for keyword in billing_keywords)
        technical_hit = any(keyword in lowered for keyword in technical_keywords)
        product_hit = any(keyword in lowered for keyword in product_keywords)
        complaint_hit = any(keyword in lowered for keyword in complaint_keywords)

        if billing_hit and technical_hit:
            intent = "billing+technical"
        elif billing_hit and product_hit:
            intent = "billing+product"
        elif billing_hit:
            intent = "billing"
        elif technical_hit:
            intent = "technical"
        elif product_hit:
            intent = "product"
        elif complaint_hit:
            intent = "complaint"
        else:
            intent = "faq"

        return {
            "agent": "intent_detection",
            "intent": intent,
            "confidence": 0.84,
            "reason": "Keyword-based routing for mock workflow",
            "prompt": self.prompt,
        }


class AgentRouter:
    def __init__(self) -> None:
        self.intent_agent = IntentDetectionAgent()
        self.executors = {
            "billing": BillingAgentExecutor(),
            "technical": TechnicalAgentExecutor(),
            "product": ProductAgentExecutor(),
            "complaint": ComplaintAgentExecutor(),
            "faq": FAQAgentExecutor(),
        }
        self.aggregator = ResponseAggregator()
        self.memory = ConversationMemory()
        self.escalation = EscalationService()

    def route(self, query: str, *, session_id: Optional[str] = None, user_id: Optional[str] = None) -> Dict[str, Any]:
        intent_result = self.intent_agent.detect(query)
        intent = intent_result["intent"]
        selected_agents = self._select_agents(intent)
        executed_responses = []
        for agent_name in selected_agents:
            response = self.executors[agent_name].execute(query, session_id=session_id or "default", user_id=user_id or "anonymous")
            executed_responses.append(response)

        aggregated = self.aggregator.merge_responses(executed_responses)
        first_result = executed_responses[0] if executed_responses else {"confidence_score": 0.0, "response": {"severity": "low"}}
        escalation = self.escalation.evaluate(first_result, repeated_failures=0, user_requested_human=False, threshold=0.6)
        confidence_score = first_result.get("confidence_score", 0.0)
        final_response = aggregated["final_response"]
        if escalation["should_escalate"]:
            final_response = f"Escalation required: {final_response}"

        self.memory.store(
            session_id=session_id or "default",
            user_id=user_id or "anonymous",
            user_message=query,
            ai_response=final_response,
            selected_agents=selected_agents,
            timestamp="2026-01-01T00:00:00Z",
            confidence_score=confidence_score,
        )

        return {
            "intent": intent,
            "selected_agents": selected_agents,
            "workflow": [{"agent": "intent_detection", "result": intent_result}] + [{"agent": agent_name, "result": response} for agent_name, response in zip(selected_agents, executed_responses)],
            "final_response": final_response,
            "confidence_score": confidence_score,
            "selected_agent": selected_agents[0] if selected_agents else "faq",
            "reasoning_summary": "Merged and deduplicated responses from specialized agents",
            "escalation": escalation,
        }

    def _select_agents(self, intent: str) -> List[str]:
        if intent == "billing+technical":
            return ["billing", "technical"]
        if intent == "billing+product":
            return ["billing", "product"]
        if intent == "billing":
            return ["billing"]
        if intent == "technical":
            return ["technical"]
        if intent == "product":
            return ["product"]
        if intent == "complaint":
            return ["complaint"]
        return ["faq"]


router = AgentRouter()
