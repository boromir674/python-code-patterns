import typing as t

class ListOfImportantItems:
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
        # notify if index is 0
        if item == 0:
            print('index 0 is requested')
        return self._list[item].toUpperCase()

    def buisness_logic(self, params=None):
        # do something with the getitem method 
        return self[0]
   


# Client Code

things_list = ListOfImportantItems()

# I know the index, I want item
second_obj_in_list = things_list[1]

# second_obj_in_list_v2 = second_obj_in_list.__getitem__(1)

second_obj_in_list_v2 == second_obj_in_list


# second_obj_in_list = things_list._list[1]

assert second_obj_in_list == 'b'
 