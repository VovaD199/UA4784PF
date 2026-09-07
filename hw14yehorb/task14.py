import unittest
import functions


class TestFunctions(unittest.TestCase):

    def test_greeting_by_name(self):
        self.assertEqual(
            functions.greeting_by_name("John"),
            "Hello John!"
        )

    def test_get_symbol_position_success(self):
        self.assertEqual(
            functions.get_symbol_position("Hello", "e"),
            2
        )

    def test_get_symbol_position_incorrect_symbol(self):
        self.assertEqual(
            functions.get_symbol_position("Hello", "ll"),
            "Error! Symbol can be string with only one letter"
        )

    def test_get_symbol_position_not_found(self):
        self.assertEqual(
            functions.get_symbol_position("Hello", "x"),
            "Not found"
        )

    def test_merge(self):
        dict1 = {"a": 1}
        dict2 = {"b": 2}

        self.assertEqual(
            functions.merge(dict1, dict2),
            {"a": 1, "b": 2}
        )

    def test_merge_dict1_immutability(self):
        dict1 = {"a": 1}
        dict2 = {"b": 2}

        functions.merge(dict1, dict2)

        self.assertEqual(dict1, {"a": 1})


if __name__ == "__main__":
    unittest.main()