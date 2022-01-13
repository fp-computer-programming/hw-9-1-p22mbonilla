# Author MB 01/10/2022

def only_list(lst):
    for i, v in enumerate(lst):
        if i % 2 != 0:
            print(v)

print(only_list([1, 2, 3, 4, 5]))