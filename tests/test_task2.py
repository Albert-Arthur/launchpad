import unittest

import data2
from tasks import task2


class Data2Tests(unittest.TestCase):
    def test_exercise2_for_alice(self):
        expectation = [data2.a_team, data2.c_team]

        self.assertEqual(expectation, task2.exercise2(data2.alice, data2.people))

    def test_exercise1_for_peggy(self):
        expectation = [data2.b_team]

        self.assertEqual(expectation, task2.exercise2(data2.peggy, data2.people))

    def test_exercise1_for_bob(self):
        expectation = [data2.a_team, data2.b_team, data2.c_team]

        self.assertEqual(expectation, task2.exercise2(data2.bob, data2.people))


if __name__ == '__main__':
    unittest.main()
