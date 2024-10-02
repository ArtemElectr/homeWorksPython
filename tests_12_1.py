import unittest

import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        new_runner = runner.Runner('Mike')
        for i in range(10):
            new_runner.walk()

        self.assertEqual( new_runner.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        new_runner = runner.Runner('Kate')
        for i in range(10):
            new_runner.run()

        self.assertEqual(new_runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner1, runner2 = runner.Runner('Ann'), runner.Runner('Alex')
        for i in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()



