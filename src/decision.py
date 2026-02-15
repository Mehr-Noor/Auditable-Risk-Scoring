def make_decision(score, age):
    if age < 18:
        return "FAIL", "LEGAL_CONSTRAINT"

    if score < 0.3:
        return "PASS", "LOW_RISK"
    if score < 0.6:
        return "REVIEW", "MEDIUM_RISK"
    return "FAIL", "HIGH_RISK"
