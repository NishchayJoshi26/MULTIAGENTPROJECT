from __future__ import annotations

from typing import Any, Dict, List


class ResponseAggregator:
    def merge_responses(self, responses: List[Dict[str, Any]]) -> Dict[str, Any]:
        seen = set()
        merged = []
        for response in responses:
            summary = response.get("response", {}).get("summary")
            if summary and summary not in seen:
                seen.add(summary)
                merged.append(response)
        order = [item.get("selected_agent") for item in merged]
        final_response = " | ".join([item.get("response", {}).get("summary", "") for item in merged if item.get("response", {}).get("summary")])
        return {
            "merged_responses": merged,
            "response_order": order,
            "final_response": final_response or "No response generated",
        }
