import typing as t

class CollectionOfImportantItems:
    # this is a frozen class
    # it is not supposed to be changed at runtime
    # it is supposed to be used as a parameter to the business logic
    # it is supposed to be used as a parameter to the business logic

    def __init__(self):
        self._list: t.list[str] = [
            'a',
            'b',
            'c',
        ]
    
    def __getitem__(self, item: int) -> str:
        return self._list[item].upper()

    def __iter__(self):
        for i in [0, 1, 2]:
            yield str(i) + self._list[i]


    def buisness_logic(self, params=None):
        # do something with the getitem method 
        return self[0]
   


# Client Code

things_collection = CollectionOfImportantItems()

# I want the 1st for some treadosn

# first = things_collection[0]
# assert first == 'A'

# I know the index, I want item

# i want representation of collection as plain list
thing_list: t.List = list(things_collection)

assert thing_list == ['A', 'B', 'C']

res = [i for i in things_collection]

assert res == ['0a', '1b', '2c']



# second_obj_in_list_v2 = second_obj_in_list.__getitem__(1)

second_obj_in_list_v2 == second_obj_in_list


# second_obj_in_list = things_list._list[1]

assert second_obj_in_list == 'b'
 