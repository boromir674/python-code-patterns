#!/usr/bin/env python

import typing as t

# GEN
# Use Case:

#   Client wants to iterate over sth, doesn't want to know more details
#   if it list of tuple, or generator

# assume the items of the iterable are generate from an even more complex
# decision algorithm, and client wants abstractoin


class TXTGenerator:

    def __init__(self, files_list: t.Sequence[str]):
        self.files_list = files_list

    def __iter__(self) -> t.Iterator[int]:
        # OPT 1
        for f in self.files_list:
            if f.endswith('.txt'):
                # I want whenver sth is generated sth to happen
                # log f object into another system
                yield f

        # OPT 2
        # return iter([i for i in self.files_list if i.endswith('.txt')])


my_gen: t.Iterable[int] = TXTGenerator(
    ['a.txt', 'b.txt', 'd.pdf']
)

print('FULL', [i for i in my_gen])
print('FULL', [i for i in my_gen])
