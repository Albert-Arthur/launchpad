import unittest

import data1
from tasks import task1


class Data1Tests(unittest.TestCase):
    def test_exercise1_for_alice(self):
        expectation = [data1.a_team, data1.c_team]

        self.assertEqual(expectation, task1.exercise1(data1.alice, data1.people))

    def test_exercise1_for_peggy(self):
        expectation = [data1.b_team]

        self.assertEqual(expectation, task1.exercise1(data1.peggy, data1.people))

    def test_exercise1_for_bob(self):
        expectation = [data1.a_team, data1.b_team, data1.c_team]

        self.assertEqual(expectation, task1.exercise1(data1.bob, data1.people))


if __name__ == '__main__':
    unittest.main()
