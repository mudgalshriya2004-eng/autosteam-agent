from langgraph.graph import StateGraph
from agent.nodes import intent_node, rag_node, lead_node


def build_graph():
    graph = StateGraph(dict)

    # ---------------- NODES ----------------
    graph.add_node("intent", intent_node)
    graph.add_node("rag", rag_node)
    graph.add_node("lead", lead_node)

    graph.set_entry_point("intent")

    # ---------------- ROUTER ----------------
    def router(state):
        intent = state.get("intent")

        # If lead flow already started, stay in lead
        if state.get("stage") in ["name", "email", "platform"]:
            return "lead"

        # High intent → lead capture
        if intent == "high_intent":
            return "lead"

        # Everything else → RAG
        return "rag"

    # ---------------- CONDITIONAL EDGES ----------------
    graph.add_conditional_edges(
        "intent",
        router,
        {
            "rag": "rag",
            "lead": "lead"
        }
    )

    # ---------------- IMPORTANT ----------------
    # DO NOT create cycles (this prevents recursion error)
    # NO graph.add_edge("rag", "intent")
    # NO graph.add_edge("lead", "intent")

    # ---------------- SAFE END STATES ----------------
    graph.set_finish_point("rag")
    graph.set_finish_point("lead")

    # ---------------- COMPILE GRAPH ----------------
    return graph.compile()