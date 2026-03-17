from dataclasses import dataclass


@dataclass
class EscalationResult:
    should_escalate: bool
    reason: str
    priority: str


def decide_escalation(ai_confidence: float, network_status: str, complaint_count: int) -> EscalationResult:
    
    # Rule 1: Low AI confidence
    if ai_confidence < 0.5:
        return EscalationResult(
            should_escalate=True,
            reason="Low AI confidence",
            priority="high"
        )

    # Rule 2: Network is down
    if network_status == "down":
        return EscalationResult(
            should_escalate=True,
            reason="Network issue detected",
            priority="high"
        )

    # Rule 3: Repeated complaints
    if complaint_count >= 3:
        return EscalationResult(
            should_escalate=True,
            reason="Multiple complaints from customer",
            priority="medium"
        )

    # Default: No escalation
    return EscalationResult(
        should_escalate=False,
        reason="No escalation needed",
        priority="low"
    )


# Test run
if __name__ == "__main__":
    result = decide_escalation(
        ai_confidence=0.4,
        network_status="down",
        complaint_count=2
    )

    print(result)

# Example integration
ai_confidence = 0.85
network_status = "down"
complaint_count = 1

result = decide_escalation(ai_confidence, network_status, complaint_count)
print(result)