import unittest


import fuctions
import functions_with_errors


class BaseTestFunctions:


    target_module = None

    def test_greeting_by_name(self):
        # Перевірка коректності привітання за ім'ям
        result = self.target_module.greeting_by_name("Анатолій")
        self.assertEqual(result, "Hello, Анатолій!")

    def test_get_symbol_position_success(self):
        # Успішний пошук символу в тексті
        pos = self.target_module.get_symbol_position("тестування", "т")
        self.assertEqual(pos, 0)

    def test_get_symbol_position_incorrect(self):
        # Перевірка випадку, коли передано некоректний символ (наприклад, довжиною > 1)
        # або невірний тип даних
        with self.assertRaises((ValueError, TypeError, AssertionError)):
            self.target_module.get_symbol_position("тест", "ет")

    def test_get_symbol_position_not_found(self):
        # Перевірка, коли символ відсутній у тексті (очікується -1 або None)
        pos = self.target_module.get_symbol_position("тест", "z")
        self.assertIn(pos, (-1, None))

    def test_merge_success(self):
        # Перевірка злиття двох словників
        d1 = {"a": 1}
        d2 = {"b": 2}
        result = self.target_module.merge(d1, d2)
        self.assertEqual(result, {"a": 1, "b": 2})

    def test_merge_dict1_immutability(self):
        # Перевірка, чи не змінюється перший словник (dict1 immutability)
        d1 = {"a": 1}
        d2 = {"b": 2}
        d1_copy = d1.copy()
        self.target_module.merge(d1, d2)
        self.assertEqual(d1, d1_copy)

    def test_merge_dict2_immutability(self):
        # Перевірка, чи не змінюється другий словник (dict2 immutability)
        d1 = {"a": 1}
        d2 = {"b": 2}
        d2_copy = d2.copy()
        self.target_module.merge(d1, d2)
        self.assertEqual(d2, d2_copy)


# Тестування оригінального модуля
class TestFuctions(unittest.TestCase, BaseTestFunctions):
     @classmethod
     def setUpClass(cls):
         cls.target_module = fuctions


# Тестування модуля з помилками
class TestFunctionsWithErrors(unittest.TestCase, BaseTestFunctions):
     @classmethod
     def setUpClass(cls):
         cls.target_module = functions_with_errors


if __name__ == "__main__":
    unittest.main()