from agent.tools import mock_lead_capture


# ---------------- INTENT NODE ----------------
def intent_node(state):
    text = state["user_input"].lower()
 

    # 1. Greeting
    if any(w in text for w in ["hi", "hello", "hey"]):
        state["intent"] = "greeting"

    # 2. HIGH INTENT (MUST BE FIRST PRIORITY)
    elif (
        "i want pro" in text or
        "pro plan" in text or
        "want to buy" in text or
        "subscribe" in text or
        "buy" in text or
        "youtube" in text
    ):
        state["intent"] = "high_intent"

    # 3. Pricing (AFTER high intent)
    elif any(w in text for w in ["price", "pricing", "cost", "features"]):
        state["intent"] = "pricing"

    else:
        state["intent"] = "general"


    if "stage" not in state:
        state["stage"] = "start"

    return state


# ---------------- RAG NODE (FULL 10 QUESTIONS COVERED) ----------------
def rag_node(state):
    query = state["user_input"].lower()

    # 1. Greeting (START)
    if state["intent"] == "greeting":
        state["response"] = (
            "Hi! Welcome to AutoStream.\n"
            "I can help you with pricing, features, refunds, and more.\n"
            "Just ask!"
        )
        return state

    # 2. Features
    if "feature" in query:
        state["response"] = (
            "Features:\n"
            "- AI video editing\n"
            "- Auto captions\n"
            "- Auto resizing\n"
            "- Social media optimization"
        )
        return state

    # 3. Refund policy
    if "refund" in query:
        state["response"] = "No refunds after 7 days."
        return state

    # 4. Video limit
    if "how many" in query or "videos" in query:
        state["response"] = "Basic: 10 videos/month, Pro: Unlimited videos"
        return state

    # 5. YouTube support
    if "youtube" in query:
        state["response"] = "Yes, supports YouTube creators."
        return state

    # 6. Free trial
    if "free" in query or "trial" in query:
        state["response"] = "No free trial, but Basic is affordable."
        return state

    # 7. Basic vs Pro
    if "basic vs pro" in query or "difference" in query:
        state["response"] = (
            "Basic vs Pro:\n"
            "- Basic: $29/month, 10 videos, 720p\n"
            "- Pro: $79/month, Unlimited, 4K, AI captions"
        )
        return state

    # 8. Video quality
    if "quality" in query or "resolution" in query:
        state["response"] = "720p (Basic), 4K (Pro)"
        return state

    # 9. Captions
    if "caption" in query:
        state["response"] = "AI captions available in Pro plan"
        return state

    # 10. Help
    if "help" in query:
        state["response"] = "Ask me about pricing, features, or plans"
        return state

    # 11. Pricing
    if "price" in query or "pricing" in query:
        state["response"] = (
            "Pricing:\n"
            "Basic - $29/month (10 videos)\n"
            "Pro - $79/month (Unlimited + 4K + captions)"
        )
        return state
    
    # ---------------- THANK YOU ----------------
    if "thank" in query:
        state["response"] = "You're welcome! Happy to help you with AutoStream."
        return state

    # DEFAULT
    state["response"] = "Ask me about pricing, features, or plans."
    return state


# ---------------- LEAD NODE ----------------
from agent.tools import mock_lead_capture

def lead_node(state):
    stage = state.get("stage", "start")
    text = state.get("user_input", "")

    if stage == "start":
        state["stage"] = "name"
        state["response"] = "What's your name?"
        return state

    if stage == "name":
        state["name"] = text
        state["stage"] = "email"
        state["response"] = "Your email?"
        return state

    if stage == "email":
        state["email"] = text
        state["stage"] = "platform"
        state["response"] = "Platform? (YouTube/Instagram)"
        return state

    if stage == "platform":
        state["platform"] = text

        mock_lead_capture(
            state["name"],
            state["email"],
            state["platform"]
        )

        state["response"] = "Lead captured successfully!"
        state["stage"] = "done"
        return state

    return state