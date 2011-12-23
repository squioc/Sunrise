import unittest
from test import Test

class TestSunrise(unittest.TestCase):

    def setUp(self):
        self.test = Test()

    def test_get_all_commands(self):
        cmd_list = map(lambda f: f.func_name, self.test.get_all_commands())
        cmd_list.sort()
        self.assertListEqual(cmd_list, ['do_bye', 'do_hello', 'do_list_commands'])


    def test_parse_args_with_a_command_only(self):
        result1 = self.test.parse_args('hello'.split())
        self.assertSequenceEqual(result1, ('hello', {'single': None, 'multiple': None}, []))

    def test_parse_args_with_a_command_and_arguments(self):
        result1 = self.test.parse_args('hello world how are you?'.split())
        self.assertSequenceEqual(result1, ('hello', {'single': None, 'multiple': None}, ['world', 'how', 'are', 'you?']))

    def test_parse_args_with_a_command_and_arguments_plus_one_option(self):
        result1 = self.test.parse_args('--single well hello world  how are you?'.split())
        self.assertSequenceEqual(result1, ('hello', {'single':['well'], 'multiple': None}, ['world', 'how', 'are', 'you?']))

    def test_parse_args_with_a_command_and_arguments_plus_two_options(self):
        result1 = self.test.parse_args('hello world how are you? --multiple well fine '.split())
        self.assertSequenceEqual(result1, ('hello', {'single': None, 'multiple': ['well', 'fine']}, ['world', 'how', 'are', 'you?']))

if __name__ == '__main__':
    unittest.main()
