import unittest

import functions
import functions_with_errors


class TestCorrectFunctions(unittest.TestCase):
    def test_greeting_by_name(self):
        self.assertEqual(
            functions.greeting_by_name("Dima"),
            "Hello Dima!"
        )

    def test_get_symbol_position_success(self):
        self.assertEqual(
            functions.get_symbol_position("Hello", "e"),
            2
        )

    def test_get_symbol_position_symbol_not_found(self):
        self.assertEqual(
            functions.get_symbol_position("Hello", "z"),
            "Not found"
        )

    def test_get_symbol_position_incorrect_symbol(self):
        self.assertEqual(
            functions.get_symbol_position("Hello", "ll"),
            "Error! Symbol can be string with only one letter"
        )

    def test_merge(self):
        dict1 = {"name": "Dima"}
        dict2 = {"age": 38}

        self.assertEqual(
            functions.merge(dict1, dict2),
            {"name": "Dima", "age": 38}
        )

    def test_merge_dict1_immutability(self):
        dict1 = {"name": "Dima"}
        dict2 = {"age": 38}

        functions.merge(dict1, dict2)

        self.assertEqual(dict1, {"name": "Dima"})

    def test_merge_dict2_immutability(self):
        dict1 = {"name": "Dima"}
        dict2 = {"age": 38}

        functions.merge(dict1, dict2)

        self.assertEqual(dict2, {"age": 38})


class TestFunctionsWithErrors(unittest.TestCase):
    def test_greeting_by_name(self):
        self.assertEqual(
            functions_with_errors.greeting_by_name("Dima"),
            "Hello Dima!"
        )

    def test_get_symbol_position_success(self):
        self.assertEqual(
            functions_with_errors.get_symbol_position("Hello", "e"),
            2
        )

    def test_get_symbol_position_symbol_not_found(self):
        self.assertEqual(
            functions_with_errors.get_symbol_position("Hello", "z"),
            "Not found"
        )

    def test_get_symbol_position_incorrect_symbol(self):
        self.assertEqual(
            functions_with_errors.get_symbol_position("Hello", "ll"),
            "Error! Symbol can be string with only one letter"
        )

    def test_merge(self):
        dict1 = {"name": "Dima"}
        dict2 = {"age": 38}

        self.assertEqual(
            functions_with_errors.merge(dict1, dict2),
            {"name": "Dima", "age": 38}
        )

    def test_merge_dict1_immutability(self):
        dict1 = {"name": "Dima"}
        dict2 = {"age": 38}

        functions_with_errors.merge(dict1, dict2)

        self.assertEqual(dict1, {"name": "Dima"})

    def test_merge_dict2_immutability(self):
        dict1 = {"name": "Dima"}
        dict2 = {"age": 38}

        functions_with_errors.merge(dict1, dict2)

        self.assertEqual(dict2, {"age": 38})


if __name__ == "__main__":
    unittest.main()