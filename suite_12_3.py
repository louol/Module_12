import unittest
from tests_12_3 import RunnerTest, TournamentTest

loader = unittest.TestLoader()
test_suite = unittest.TestSuite()
test_suite.addTests(loader.loadTestsFromTestCase(RunnerTest))
test_suite.addTests(loader.loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)

if __name__ == "__main__":
    runner.run(test_suite)