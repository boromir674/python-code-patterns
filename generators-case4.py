#!/usr/bin/env python

import typing as t

# GEN
# Use Case:

#   Client wants to iterate over sth, doesn't want to know more details
#   if it list of tuple, or generator

# assume the items of the iterable are generate from an even more complex
# decision algorithm, and client wants abstractoin

# client just needs ONE time generation of items


class ALLGenerator:

    def __init__(self, files_list: t.Sequence[str]):
        self.files_list = files_list  # ['a.txt', 'b.txt', 'd.pdf']
        
        self._index = 0
    
    def __next__(self) -> int:
        if self._index >= len(self.files_list):
            raise StopIteration

        candidate_item: str = self.files_list[self._index]
        self._index += 1
        return                                                                                                        

    def __iter__(self) -> t.Iterator[int]:
        self._index = 0
        while True:
            try:
                item = self.__next__()
                if item.endswith('.txt'):
                    yield item
            except StopIteration:
                break


txt_iterator = ALLGenerator(
    ['a.txt', 'b.txt', 'a.pdf', 'asd.txt']
)

print('FULL', [i for i in iter(txt_iterator)])
# print('FULL', [i for i in txt_gen])

# skip 1st item and get 2nd from generator (not from list/tuple)
txt_gen = iter(txt_iterator)
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
