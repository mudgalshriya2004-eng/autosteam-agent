def intent_node(state):
    text = state["user_input"].lower()

    print("DEBUG INPUT:", text)

    if any(w in text for w in ["hi", "hello", "hey"]):
        state["intent"] = "greeting"

    elif any(w in text for w in ["price", "pricing", "plan", "cost", "features"]):
        state["intent"] = "pricing"

    elif any(w in text for w in ["pro", "buy", "subscribe", "youtube", "i want"]):
        state["intent"] = "high_intent"

    else:
        state["intent"] = "general"

    print("DEBUG INTENT:", state["intent"])

    return state