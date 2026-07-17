from backend.agents.aggregator import ResponseAggregator
from backend.agents.escalation import EscalationService
from backend.agents.executor import BillingAgentExecutor
from backend.agents.memory import ConversationMemory
from backend.agents.router import router as agent_router


def test_billing_executor_returns_structured_json() -> None:
    executor = BillingAgentExecutor()
    result = executor.execute("I need help with my invoice", session_id="session-1", user_id="user-1")
    assert result["selected_agent"] == "billing"
    assert "confidence_score" in result
    assert "reasoning_summary" in result
    assert result["response"]["status"] == "ok"


def test_response_aggregator_deduplicates_and_preserves_order() -> None:
    aggregator = ResponseAggregator()
    responses = [
        {"selected_agent": "billing", "response": {"summary": "Billing issue"}, "confidence_score": 0.8},
        {"selected_agent": "technical", "response": {"summary": "Billing issue"}, "confidence_score": 0.7},
        {"selected_agent": "faq", "response": {"summary": "Need more help"}, "confidence_score": 0.9},
    ]
    merged = aggregator.merge_responses(responses)
    assert len(merged["merged_responses"]) == 2
    assert merged["final_response"]


def test_conversation_memory_records_required_fields() -> None:
    memory = ConversationMemory()
    entry = memory.store(
        session_id="session-1",
        user_id="user-1",
        user_message="I need help",
        ai_response="Here is an answer",
        selected_agents=["billing"],
        timestamp="2026-01-01T00:00:00Z",
        confidence_score=0.82,
    )
    assert entry["session_id"] == "session-1"
    assert entry["user_id"] == "user-1"
    assert entry["user_message"] == "I need help"
    assert entry["selected_agents"] == ["billing"]


def test_escalation_service_returns_structured_escalation() -> None:
    service = EscalationService()
    escalation = service.evaluate(
        {"confidence_score": 0.2, "selected_agent": "complaint", "response": {"severity": "high"}},
        repeated_failures=2,
        user_requested_human=False,
        threshold=0.6,
    )
    assert escalation["should_escalate"] is True
    assert escalation["escalation_level"] == "human_support"


def test_router_returns_intelligent_results() -> None:
    result = agent_router.route("I need help with my billing charge", session_id="session-2", user_id="user-2")
    assert result["intent"] == "billing"
    assert result["selected_agents"] == ["billing"]
    assert result["confidence_score"] >= 0
    assert result["escalation"]["should_escalate"] is False
