#!/usr/bin/env python

import typing as t


# GEN
# Use Case:

#   Heavy objects I want to iterate on and
#   I don't care about iterating a 2nd time

#   my client expects an Iterable interface


### BACKEND ###
ids_sequence: t.Sequence[str] = ['1', '2', '3']


# every id corresponds to a file with data


def get_data(id: str):
    return 'data' + id


# client wants to iterate over the data that each server brings

# in memory objet with the data (if data is 1GB -> then this is 3 x 1 = 3GB)
# data = [get_data(id) for id in ids_sequence]

at = (get_data(id) for id in ids_sequence)
print(type(at))
# this is 1MB
data_generator = iter(
    (get_data(id) for id in ids_sequence)
)
at = iter(ids_sequence)

print(type(at))

### Client Code ###

# i want just want sth i can iterate on

# data should be brought fro mthe backend to the Frontend

def server_content_to_ftont(one_data):
    return f'Rendered Data as HTML {str(one_data)}'


def consume_data(data: t.Sequence[str]) -> None:
    for one_data in data:
        print(server_content_to_ftont(one_data))


print("First Content)")
for i in at:
    print(server_content_to_ftont(i))


print("Second Content)")
# EMPTY GENERATOR
for i in at:
    print(server_content_to_ftont(i))


# for i in data:
#     server_content_to_ftont(i)