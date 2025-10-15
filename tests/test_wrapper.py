import unittest
from unittest.mock import Mock
from llm_token_tracker import wrap_llm

class TestTokenTracker(unittest.TestCase):
    def test_wrap_llm(self):
        mock_llm = Mock()
        mock_response = Mock()
        mock_response.content = "Hello world"
        mock_response.usage.total_tokens = 10
        mock_llm.invoke.return_value = mock_response
        wrapped = wrap_llm(mock_llm)
        response = wrapped.invoke("Hi")
        self.assertEqual(response, "Hello world")
        self.assertEqual(wrapped.total_tokens, 10)
        wrapped.original_invoke.assert_called_once_with("Hi")

if __name__ == '__main__':
    unittest.main()