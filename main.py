from agent.graph import build_graph

# Build compiled graph
app = build_graph()

# Initial state (IMPORTANT: keep persistent memory)
state = {
    "user_input": "",
    "intent": None,
    "response": None,
    "stage": "start"
}

print("AutoStream AI Agent Started (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Thank you for using AutoStream 🚀")
        break

    # update input in state
    state["user_input"] = user_input

    # invoke graph
    result = app.invoke(state)

    # print bot response safely
    print("Bot:", result.get("response", "No response"))

    # IMPORTANT: persist full state for multi-turn memory
    state = result