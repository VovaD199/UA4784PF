import unittest
import functions
import functions_with_errors


class TestFunctions(unittest.TestCase):
    def test_greeting_by_name(self):
        self.assertEqual(
            functions.greeting_by_name("Layne"),
            "Hello Layne!"
        )
        self.assertEqual(
            functions_with_errors.greeting_by_name("Layne"),
            "Hello Layne!"
        )
    def test_get_symbol_position_success(self):
        self.assertEqual(
            functions.get_symbol_position("bebra", "r"),
            4
        )
        self.assertEqual(
            functions_with_errors.get_symbol_position("bebra", "r"),
            4
        )
    def test_get_symbol_position_not_found(self):
        self.assertEqual(
            functions.get_symbol_position("bebra", "k"),
            "Not found"
        )
        self.assertEqual(
            functions_with_errors.get_symbol_position("bebra", "k"),
            "Not found"
        )
    def test_get_symbol_position_incorrect(self):
        self.assertEqual(
            functions.get_symbol_position("bebra", "ab"),
            "Error! Symbol can be string with only one letter"
        )
        self.assertEqual(
            functions_with_errors.get_symbol_position("bebra", "ab"),
            "Error! Symbol can be string with only one letter"
        )
    def test_merge(self):
        self.assertEqual(
            functions.merge({"a": 1, "b": 2}, {"c": 3}),
            {"a": 1, "b": 2, "c": 3}
        )
        self.assertEqual(
            functions_with_errors.merge({"a": 1, "b": 2}, {"c": 3}),
            {"a": 1, "b": 2, "c": 3}
        )
    def test_merge_dict1_immutability(self):
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3}

        functions.merge(dict1, dict2)

        self.assertEqual(
            dict1,
            {"a": 1, "b": 2}
        )

        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3}

        functions_with_errors.merge(dict1, dict2)

        self.assertEqual(
            dict1,
            {"a": 1, "b": 2}
        )
    def test_merge_dict2_immutability(self):
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3}

        functions.merge(dict1, dict2)

        self.assertEqual(
            dict2,
            {"c": 3}
        )

        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3}

        functions_with_errors.merge(dict1, dict2)

        self.assertEqual(
            dict2,
            {"c": 3}
        )


if __name__ == "__main__":
    unittest.main()