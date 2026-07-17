from __future__ import annotations

from typing import Any, Dict

from langgraph.graph import END, StateGraph

from backend.agents.router import router as agent_router


class AgentWorkflow:
    def __init__(self) -> None:
        self.router = agent_router
        self.graph = self._build_graph()

    def _build_graph(self) -> StateGraph:
        workflow = StateGraph(dict)
        workflow.add_node("route", self._route)
        workflow.add_node("aggregate", self._aggregate)
        workflow.set_entry_point("route")
        workflow.add_edge("route", "aggregate")
        workflow.add_edge("aggregate", END)
        return workflow.compile()

    def _route(self, state: Dict[str, Any]) -> Dict[str, Any]:
        query = state.get("query", "")
        route_result = self.router.route(query)
        return {**state, **route_result}

    def _aggregate(self, state: Dict[str, Any]) -> Dict[str, Any]:
        workflow_output = state.get("workflow", [])
        final_response = state.get("final_response", "No response generated")
        return {
            **state,
            "workflow": workflow_output,
            "final_response": final_response,
        }

    def run(self, query: str) -> Dict[str, Any]:
        return self.graph.invoke({"query": query})


workflow = AgentWorkflow()
