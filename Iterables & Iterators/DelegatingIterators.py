"""
Delegating Iterators
"""

from collections import namedtuple

Person = namedtuple('Person', 'first last')

class PersonNames:
    def __init__(self, persons):
        try:
            self._persons = [person.first.capitalize()
                         + ' ' + person.last.capitalize()
                         for person in persons]
        except (TypeError, AttributeError):
            self.persons = []

    def __iter__(self):
        return iter(self._persons) # This is called delegating

persons = [Person('michaeL', 'paLin'), Person('eric', 'idLe'),
           Person('john', 'cLeese')]

person_names = PersonNames(persons)

print(person_names._persons)

for name in person_names:
    print(name)

