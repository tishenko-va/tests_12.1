from unittest import TestCase
import runner


class RunnerTest(TestCase):

    def test_walk(self):
        runner1 = runner.Runner('name')
        for i in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    def test_run(self):
        runner2 = runner.Runner('name')
        for i in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    def test_challenge(self):
        runner1 = runner.Runner('runner1')
        runner2 = runner.Runner('runner2')
        for i in range(10):
            runner1.walk()
            runner1.run()
            runner2.walk()
            runner2.run()
        self.assertEqual(runner1.distance, runner2.distance)



if __name__ == '__main__':
    unittest.main