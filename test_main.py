import unittest
import main

class TestMain(unittest.TestCase):

    def test_calculate_score(self):
        self.assertEqual(main.calculate_score(["A", "A", "Q"]), 12)
        self.assertEqual(main.calculate_score([ "A", "Q"]), 21)
        self.assertEqual(main.calculate_score(["A", "A", "A", "A"]), 14)
        self.assertEqual(main.calculate_score(['2', '2']), 4)

if __name__ == "__main__":
    unittest.main()