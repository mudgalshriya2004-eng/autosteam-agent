#  AutoStream – Social-to-Lead Agentic AI System

##  Project Overview

AutoStream is an agentic conversational AI system for a SaaS product that provides automated video editing tools for content creators.
## 1. How to Run the Project Locally

*###* Step 1: Install dependencies
```bash
pip install langgraph openai
### Step 2: Set API key (if using LLM)
set OPENAI_API_KEY=your_api_key
### Step 3: Run the project
python main.py
### Step 4: Start chatting
Type messages like "hi", "pricing", etc.
Type "exit" to stop the program

## 2. Architecture Explanation 

This project is built using LangGraph, which is a state-based framework for building structured AI agent workflows. I chose LangGraph over AutoGen because it provides better control over node-based execution flow, state transitions, and conditional routing, which is essential for building production-grade agentic systems.

The system consists of three main nodes: Intent Detection Node, RAG Node, and Lead Capture Node. The Intent Node classifies user input into categories such as greeting, pricing inquiry, or high-intent users. Based on this classification, the graph routes the execution to the appropriate node.

The RAG Node retrieves relevant information from a local JSON knowledge base containing pricing, features, and company policies. This ensures accurate and deterministic responses instead of hallucinated outputs.

State management is handled using a shared state dictionary that persists across all nodes. It stores user inputs, detected intent, responses, and lead information such as name, email, and platform. This enables multi-turn conversation memory across 5–6 interactions.

LangGraph’s stateful architecture allows the agent to behave like a real-world system rather than a simple chatbot by maintaining context, making decisions, and executing tools conditionally.

## 3. WhatsApp Deployment (Webhook Integration)

To integrate this agent with WhatsApp, we would use either Twilio WhatsApp API or Meta WhatsApp Cloud API.

Flow:
User sends a message on WhatsApp
Message is received via a webhook endpoint (Flask/FastAPI server)
Webhook forwards the message to the LangGraph agent
Agent processes the message (intent → RAG → lead flow)
Response is generated and sent back via WhatsApp API

Architecture:
WhatsApp User → WhatsApp API → Webhook Server → LangGraph Agent → Response → WhatsApp API → User

This allows real-time conversational automation where the AI agent can handle queries, qualify leads, and respond directly inside WhatsApp conversations.
