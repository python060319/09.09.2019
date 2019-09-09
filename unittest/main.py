import unittest

class Calculator:
    def add(self, a, b):
        return a + b

class TestCalculator(unittest.TestCase):
    def test(self):
        c = Calculator()
        a = 3
        b = 4
        exptected = 7
        result = c.add(a, b)
        self.assertEqual(result, exptected)

t = TestCalculator()
t.test()

# targil
# 1. add function multiply
# 2. add test function
# 3. try-except on each test method,
#    to avoid crash. print the error
#       or print test - succeeded!
