import unittest
from english_trainner_with_chatgpt.english_trainner_with_chatgpt.models.english_word import EnglishWord
from english_trainner_with_chatgpt.english_trainner_with_chatgpt.models.grammar_rule import GrammarRule
from english_trainner_with_chatgpt.english_trainner_with_chatgpt.models.user import User
from english_trainner_with_chatgpt.english_trainner_with_chatgpt.routes.chatbot import ChatBot


class TestChatBot(unittest.TestCase):
    """
    Unit tests for the ChatBot class.
    """

    def setUp(self):
        self.chat_bot = ChatBot()
        self.english_word = EnglishWord(word='test_word', definition='a word for testing')
        self.grammar_rule = GrammarRule(rule='test_rule', example='This is a test rule.')
        self.user = User(username='test_user')

    def test_get_definition(self):
        definition = self.chat_bot.get_definition(self.english_word)
        self.assertEqual(definition, 'a word for testing')

    def test_get_example(self):
        example = self.chat_bot.get_example(self.grammar_rule)
        self.assertEqual(example, 'This is a test rule.')

    def test_register_user(self):
        response = self.chat_bot.register_user('test_user')
        self.assertEqual(response, 'User "test_user" registered successfully!')

    def test_register_existing_user(self):
        self.chat_bot.register_user('test_user')
        response = self.chat_bot.register_user('test_user')
        self.assertEqual(response, 'User "test_user" already exists!')

    def test_validate_input(self):
        self.assertTrue(self.chat_bot.validate_input('what is the definition of test_word?'))
        self.assertTrue(self.chat_bot.validate_input('what is a test rule?'))
        self.assertFalse(self.chat_bot.validate_input('hello world'))

    def tearDown(self):
        self.chat_bot = None
        self.english_word = None
        self.grammar_rule = None
        self.user = None


if __name__ == '__main__':
    unittest.main()
