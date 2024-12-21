import logging
from unittest import TestCase
from rt_with_exceptions import Runner

logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class RunnerTest(TestCase):
    def test_walk(self):
        try:
            runner = Runner("Test Runner")
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except TypeError as err:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
    def test_run(self):
        try:
            runner = Runner("Test Runner")
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except ValueError as e:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_challenge(self):
        runner1 = Runner("Runner 1")
        runner2 = Runner("Runner 2")
        for _ in range(10):
            runner1.run()
        for _ in range(10):
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)
