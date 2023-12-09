from matchers import *

class QueryBuilder:
    def __init__(self, query=All()):
        self._query_obj = query

    def playsIn(self, team):
        return QueryBuilder(And(self._query_obj, PlaysIn(team)))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._query_obj, HasAtLeast(value, attr)))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._query_obj, HasFewerThan(value, attr)))

    def oneOf(self, *matchers):
        choices = [And(self._query_obj, matcher) for matcher in matchers]

        return QueryBuilder(Or(*choices))

    def build(self):
        return self._query_obj
