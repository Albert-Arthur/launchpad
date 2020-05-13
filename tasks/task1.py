import data1
from typing import List
from person import Person


def exercise1(person: Person, listed_people: List[Person]) -> List[Person]:
    return [p for p in listed_people if p.is_team and person in p.members]


if __name__ == "__main__":
    print([t.displayname for t in exercise1(data1.alice, data1.people)])
