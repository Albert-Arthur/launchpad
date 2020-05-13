import data2
from typing import List
from person import Person


def exercise2(person: Person, listed_people: List[Person]) -> List[Person]:
    return list(filter(lambda listed_person: is_in_team(listed_person, person), listed_people))


def is_in_team(listed_person: Person, person: Person) -> bool:
    if not listed_person.is_team:
        return False

    for member in listed_person.members:
        if person.id == member.id:
            return True

        if is_in_team(member, person):
            return True

    return False


if __name__ == "__main__":
    print([t.displayname for t in exercise2(data2.alice, data2.people)])
