import typing as t


class A:

    _data: t.Sequence[str]

    def __init__(self, items_collection: t.Sequence[int] | None = None) -> None:
        if not items_collection:
            self._data = ['1', '2', '3']
        else:
            self._data = [str(x) for x in items_collection]

    def business_logic(self, params=None):
        # do sth with sencapsulated data possibly parametrized at runtime
        print(self._data)

    @property
    def correct_data(self) -> t.Sequence[str]:
        return [str(x) +'asasd' for x in self._data]

    @correct_data.setter
    def correct_data(self, items_collection: t.Sequence[int]) -> None:
        # ie: notify an external log system
        self._data = [str(x) for x in items_collection]



# Client Code

first_user_data = [1, 2, 3]

ao = A(first_user_data)

# I call business logic with some params
ao.business_logic()

# this code needs to know the colletion of items used internally

exported_data = ao.correct_data

second_user_data = [4, 5, 6]

ao.correct_data = second_user_data

ao.business_logic()