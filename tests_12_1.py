import runner
from unittest import TestCase as tc


class RunnerTest(tc):
    def test_walk(self):
        new_runner = runner.Runner('Mike')
        for i in range(10):
            new_runner.walk()

        tc.assertEqual(self, new_runner.distance, 50)

    def test_run(self):
        new_runner = runner.Runner('Kate')
        for i in range(10):
            new_runner.run()

        tc.assertEqual(self, new_runner.distance, 100)

    def test_challenge(self):
        runner1, runner2 = runner.Runner('Ann'), runner.Runner('Alex')
        for i in range(10):
            runner1.run()
            runner2.walk()

        tc.assertNotEqual(self, runner1.distance, runner2.distance)


if __name__ == '__main__':
    runner_test = RunnerTest
    runner_test.test_walk()
    runner_test.test_run()


