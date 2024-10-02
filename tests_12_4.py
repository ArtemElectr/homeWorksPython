import logging
import rt_with_exceptions as runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_test.log', encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            new_runner = runner.Runner('Mike', -5)
            for i in range(10):
                new_runner.walk()

            self.assertEqual(new_runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            new_runner = runner.Runner(10)
            for i in range(10):
                new_runner.run()

            self.assertEqual(new_runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner1, runner2 = runner.Runner('Ann'), runner.Runner('Alex')
        for i in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':

    #unittest.main()
    test = RunnerTest()

    test.test_walk()


