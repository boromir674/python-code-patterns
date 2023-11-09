import typing as t


class DictOfImportantItems:
    def __init__(self):
        self._data: t.Dict[str, int] = {
            'a': 1,
            'b': 2,
            'c': 3,
        }

    def __getitem__(self, item: str):
        return self._data[item] * 2


# Client Code

reg_dict = DictOfImportantItems()

# get sth from registry

obj = reg_dict['c']

assert obj == 6

# 