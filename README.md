# llm-token-tracker

A Python package to track token usage in LLM interactions.

## Installation

```bash
pip install llm-token-tracker
```

## Usage

```python
from llm_token_tracker import wrap_llm

# Wrap an xAI model for token tracking
wrapped_llm = wrap_llm("grok-3")

response = wrapped_llm.invoke("Hello, how are you?")
# Console will log: Total tokens used in context: X

# Advanced: Pass your own chat for conversation context
from xai_sdk import Client
client = Client()
chat = client.chat.create(model="grok-3")
response = wrapped_llm.invoke("Hello", chat=chat)
response2 = wrapped_llm.invoke("How are you?", chat=chat)  # Continues the conversation
```

Note: Requires XAI_API_KEY environment variable set for authentication.
