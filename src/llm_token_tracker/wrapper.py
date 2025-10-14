import tiktoken

class TokenTracker:
    def __init__(self, llm, model_name):
        self.llm = llm
        self.encoding = tiktoken.encoding_for_model(model_name)
        self.total_tokens = 0

    def invoke(self, prompt):
        response = self.llm.invoke(prompt)
        prompt_tokens = len(self.encoding.encode(prompt))
        response_tokens = len(self.encoding.encode(str(response)))
        self.total_tokens += prompt_tokens + response_tokens
        print(f"Total tokens used in context: {self.total_tokens}")
        return response