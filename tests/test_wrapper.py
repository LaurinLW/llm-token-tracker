import unittest
from unittest.mock import Mock
from llm_token_tracker import wrap_llm

class TestTokenTracker(unittest.TestCase):
    def test_wrap_llm(self):
        mock_llm = Mock()
        mock_llm.invoke.return_value = "Hello world"
        wrapped = wrap_llm(mock_llm, "gpt-3.5-turbo")
        response = wrapped.invoke("Hi")
        self.assertEqual(response, "Hello world")
        self.assertGreater(wrapped.total_tokens, 0)
        mock_llm.invoke.assert_called_once_with("Hi")

if __name__ == '__main__':
    unittest.main()