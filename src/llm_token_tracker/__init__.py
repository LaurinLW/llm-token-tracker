from .wrapper import TokenTracker

def wrap_llm(llm):
    return TokenTracker(llm)