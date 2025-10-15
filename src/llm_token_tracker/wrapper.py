class TokenTracker:
    def __init__(self, llm):
        self.llm = llm
        self.original_invoke = llm.invoke
        self.total_tokens = 0
        llm.invoke = self._patched_invoke

    def _patched_invoke(self, prompt, *args, **kwargs):
        response = self.original_invoke(prompt, *args, **kwargs)
        self.total_tokens += response.usage.total_tokens
        print(f"Total tokens used in context: {self.total_tokens}")
        return response.content

    def invoke(self, prompt, *args, **kwargs):
        return self.llm.invoke(prompt, *args, **kwargs)
