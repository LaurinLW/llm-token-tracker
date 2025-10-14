from .wrapper import TokenTracker

def wrap_llm(llm, model_name):
    return TokenTracker(llm, model_name)