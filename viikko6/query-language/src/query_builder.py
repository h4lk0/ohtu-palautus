from matchers import All, And, HasFewerThan, HasAtLeast, PlaysIn

class QueryBuilder:
    def __init__(self, query = All()):
        self._query = query

    def build(self):
        return self._query

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._query, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._query, HasFewerThan(value, attr)))

    def playsIn(self, team):
        return QueryBuilder(And(self._query, PlaysIn(team)))