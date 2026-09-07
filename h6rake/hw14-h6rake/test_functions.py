import unittest

import functions
import functions_with_errors


class FunctionsTestsMixin:
    module = None

    def test_greeting_by_name(self):
        self.assertEqual(
            self.module.greeting_by_name("John"),
            "Hello John!"
        )

    def test_get_symbol_position_incorrect_symbol(self):
        self.assertEqual(
            self.module.get_symbol_position("Python", "th"),
            "Error! Symbol can be string with only one letter"
        )

    def test_get_symbol_position_success(self):
        self.assertEqual(
            self.module.get_symbol_position("Python", "t"),
            3
        )
    
    def test_get_symbol_position_not_found(self):
        self.assertEqual(
            self.module.get_symbol_position("Python", "z"),
            "Not found"
        )

    def test_merge_result(self):
        dictionary1 = {"name": "John", "age": 20}
        dictionary2 = {"city": "London", "age": 25}

        self.assertEqual(
            self.module.merge(dictionary1, dictionary2),
            {"name": "John", "age": 25, "city": "London"}
        )

    def test_merge_does_not_change_dict1(self):
        dictionary1 = {"name": "John", "age": 20}
        dictionary2 = {"city": "London", "age": 25}
        original_dictionary1 = dictionary1.copy()

        self.module.merge(dictionary1, dictionary2)

        self.assertEqual(dictionary1, original_dictionary1)

    def test_merge_does_not_change_dict2(self):
        dictionary1 = {"name": "John", "age": 20}
        dictionary2 = {"city": "London", "age": 25}
        original_dictionary2 = dictionary2.copy()

        self.module.merge(dictionary1, dictionary2)

        self.assertEqual(dictionary2, original_dictionary2)


class TestCorrectFunctions(FunctionsTestsMixin, unittest.TestCase):
    module = functions


class TestFunctionsWithErrors(FunctionsTestsMixin, unittest.TestCase):
    module = functions_with_errors


if __name__ == "__main__":
    unittest.main(verbosity=2)