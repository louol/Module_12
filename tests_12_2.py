import unittest
from runner_and_tournament import *

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

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

    def test_tournament1(self):
        self.all_results = Tournament(90, self.name1, self.name3).start()
        self.assertTrue(self.all_results[max(self.all_results.keys())].name == 'Ник')
        TournamentTest.all_results[1] = self.all_results

    def test_tournament2(self):
        self.all_results = Tournament(90, self.name2, self.name3).start()
        self.assertTrue(self.all_results[max(self.all_results.keys())].name == 'Ник')
        TournamentTest.all_results[2] = self.all_results

    def test_tournament3(self):
        self.all_results = Tournament(90, self.name1, self.name2, self.name3).start()
        self.assertTrue(self.all_results[max(self.all_results.keys())].name == 'Ник')
        TournamentTest.all_results[3] = self.all_results