import unittest

import data2
import data3
from tasks import task3


class Data2Tests(unittest.TestCase):
    def test_get_people_with_data_2(self):
        scenarios = [
            {
                "team": data2.a_team,
                "expectation": [data2.alice, data2.bob, data2.carlos],
            },
            {
                "team": data2.b_team,
                "expectation": [data2.peggy, data2.trent, data2.victor, data2.bob],
            },
            {
                "team": data2.c_team,
                "expectation": [data2.alice, data2.bob, data2.carlos, data2.charlie, data2.eve],
            },
        ]

        for scenario in scenarios:
            expectation = sorted(p.displayname for p in scenario['expectation'])
            actual = sorted(p.displayname for p in task3.get_people(scenario['team']))

            self.assertEqual(expectation, actual)

    def test_get_people_with_data_3(self):
        teams = [data3.a_team, data3.b_team, data3.c_team]

        people = [
            data3.alice, data3.bob, data3.carlos,
            data3.peggy, data3.trent, data3.victor, data3.charlie,
            data3.eve,
        ]

        expectation = sorted(p.displayname for p in people)

        for team in teams:
            actual = sorted(p.displayname for p in task3.get_people(team))

            self.assertEqual(expectation, actual)


if __name__ == '__main__':
    unittest.main()
