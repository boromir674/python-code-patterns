#!/usr/bin/env python

import typing as t


class ALLGenerator:

    def __init__(self, files_list: t.Sequence[str]):
        self.files_list = files_list  # ['a.txt', 'b.txt', 'd.pdf']
        
        self._index = 0

    def __iter__(self) -> t.Iterator[int]:
        return iter(self.files_list)

o = ALLGenerator(
    ['a.txt', 'b.txt', None]
)

txt_gen = iter(o)

# print('FULL', [i for i in txt_gen])
# print('FULL', [i for i in txt_gen])


# skip 1st item and get 2nd from generator (not from list/tuple)
next(txt_gen)
second = next(txt_gen)
trito = next(txt_gen)
try:
    tetarto = next(txt_gen)
except StopIteration:
    tetarto = 'No more items'

print("2nd:", second)
print("3rd:", trito)
print("4th:", tetarto)

print('FULL', [i for i in iter(o)])
print('FULL', [i for i in o])
print('FULL', [i for i in o])