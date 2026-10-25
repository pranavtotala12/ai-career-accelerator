def build_triage_prompt(ticket: str) -> str:
    return f"""
            ROLE
            You are a support-triage assistant for an e-commerce app.

            TASK
            Classify the customer ticket.

            CONTEXT
            Allowed categories: payment, delivery, account, other.
            Ticket: {ticket}

            CONSTRAINTS
            Use one allowed category. If unclear, use other.
            Reason must be one sentence.

            OUTPUT FORMAT
            Return JSON only with keys: category, reason.
            """