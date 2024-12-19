from unittest import TestCase
from runner_and_tournament import *


def skip_if_frozen(method):
    def wrapper(self):
        if self.is_frozen == True:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            method(self)

    return wrapper

class RunnerTest(TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("Test Runner")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner("Test Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Runner 1")
        runner2 = Runner("Runner 2")
        for _ in range(10):
            runner1.run()
        for _ in range(10):
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

class TournamentTest(TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @skip_if_frozen
    def setUp(self):
        self.name1 = Runner('Усэйн', 10)
        self.name2 = Runner('Андрей', 9)
        self.name3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results.values():
            result = {}
            for key, value in i.items():
                result[key] = value.name
            print(result)

    @skip_if_frozen
    def test_tournament1(self):
        self.all_results = Tournament(90, self.name1, self.name3).start()
        self.assertTrue(self.all_results[max(self.all_results.keys())].name == 'Ник')
        TournamentTest.all_results[1] = self.all_results

    @skip_if_frozen
    def test_tournament2(self):
        self.all_results = Tournament(90, self.name2, self.name3).start()
        self.assertTrue(self.all_results[max(self.all_results.keys())].name == 'Ник')
        TournamentTest.all_results[2] = self.all_results

    @skip_if_frozen
    def test_tournament3(self):
        self.all_results = Tournament(90, self.name1, self.name2, self.name3).start()
        self.assertTrue(self.all_results[max(self.all_results.keys())].name == 'Ник')
        TournamentTest.all_results[3] = self.all_results


