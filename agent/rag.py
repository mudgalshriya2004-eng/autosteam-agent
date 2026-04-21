import json

def load_kb():
    with open("data/knowledge.json", "r") as f:
        return json.load(f)


def get_rag_answer(query):
    kb = load_kb()
    q = query.lower()

    # Pricing
    if "price" in q or "plan" in q or "pricing" in q:
        basic = kb["plans"]["basic"]
        pro = kb["plans"]["pro"]

        return f"""
    AutoStream Pricing:

🔹 Basic:
- {basic['price']}
- {basic['features'][0]}
- {basic['features'][1]}

🔹 Pro:
- {pro['price']}
- {pro['features'][0]}
- {pro['features'][1]}
- {pro['features'][2]}
"""

    # Policies
    if "refund" in q:
        return kb["policies"][0]

    if "support" in q:
        return kb["policies"][1]

    return "Ask about pricing, features or policies."