import data2
import data3
from typing import List
from person import Person


def get_people(person: Person) -> List[Person]:
    if not person.is_team:
        return []

    teams_checked = []

    return get_people_in_team(person, teams_checked)


def get_people_in_team(team: Person, teams_checked: List[Person]) -> List[Person]:
    people = []
    for member in team.members:
        if member in teams_checked:
            continue

        if member.is_team:
            teams_checked.append(member)
            people.extend(get_people_in_team(member, teams_checked))
            continue

        people.append(member)
    return list(set(people))


if __name__ == "__main__":
    print(sorted(p.displayname for p in get_people(data2.c_team)))
    print(sorted(p.displayname for p in get_people(data3.c_team)))
