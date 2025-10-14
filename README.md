# llm-token-tracker

A Python package to track token usage in LLM interactions.

## Installation

```bash
pip install llm-token-tracker
```

## Usage

```python
from llm_token_tracker import wrap_llm

# Assuming you have an LLM object with an invoke(prompt) method that returns a string
wrapped_llm = wrap_llm(llm, "gpt-3.5-turbo")

response = wrapped_llm.invoke("Hello, how are you?")
# Console will log: Total tokens used in context: X
```
