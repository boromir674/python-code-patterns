#!/usr/bin/env python

import typing as t

# GEN
# Use Case:

#   Client wants to iterate over sth, doesn't want to know more details
#   if it list of tuple, or generator

# assume the items of the iterable are generate from a complex
# decision algorithm, and client wants abstractoin


class Generator:

    def __init__(self, a):
        self.a = a

    def __iter__(self) -> t.Iterator[int]:
        # return 1
        if self.a > 1:
            return iter([1,2,3])
        return iter([4,5,6])


my_gen: t.Iterable[int] = Generator(0)

print('FULL', [i for i in my_gen])
print('FULL', [i for i in my_gen])

my_gen: t.Iterable[int] = Generator(5)

print('FULL', [i for i in my_gen])
print('FULL', [i for i in my_gen])


my_itter = iter(i for i in Generator(0))

print('FULL, iter magic func', [i for i in my_itter])
print('EMPTY, iter magic func', [i for i in my_itter])
