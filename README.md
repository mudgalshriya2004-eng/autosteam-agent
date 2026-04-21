# AutoStream – Social-to-Lead Agentic AI System

## 1. How to Run the Project Locally

step 1: Install dependencies
pip install langgraph openai

step 2: Set API Key
set OPENAI_API_KEY=your_api_key

Step 3: Run the project
python main.py

Step 4: Start chatting
Type messages like:

hi
pricing
I want Pro plan
thank you

Type exit to stop.


## 2. Architecture Explanation 

This project is built using LangGraph, a state-based framework designed for building structured and production-grade AI agent workflows. I chose LangGraph over AutoGen because it provides better control over node-based execution, explicit state transitions, and conditional routing between different parts of the agent. This makes it easier to design deterministic and reliable AI systems instead of free-flow chatbots.

The system is divided into three main components: Intent Node, RAG Node, and Lead Capture Node. The Intent Node classifies user input into categories such as greeting, pricing-related queries, or high-intent users who are ready to convert. Based on this classification, LangGraph routes the flow to the appropriate node.

The RAG Node retrieves accurate responses from a local knowledge base (JSON file) containing pricing, features, and policies of the AutoStream product. This ensures responses are grounded and consistent.

State management is handled using a shared dictionary that persists across all nodes. This state stores user input, detected intent, conversation stage, and collected lead details such as name, email, and platform. Because the state is passed between nodes, the system maintains memory across multiple turns (5–6 interactions), making the conversation feel natural and contextual.


## 3. WhatsApp Deployment (Webhook Integration)

To integrate this agent with WhatsApp, we can use either the Twilio WhatsApp API or Meta WhatsApp Cloud API.

### Flow:

User sends a message on WhatsApp → Message is received by a webhook (Flask or FastAPI server) → Webhook forwards the message to the LangGraph agent → Agent processes it (intent detection → RAG → lead capture) → Response is generated → Sent back to WhatsApp via API.

### Architecture:

WhatsApp User → WhatsApp API → Webhook Server → LangGraph Agent → Response → WhatsApp API → User

This setup enables real-time conversational automation where the AI agent can answer queries, detect intent, and capture leads directly inside WhatsApp conversations.
