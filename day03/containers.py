# list: ordered collection

## insert
li = [1, 2, 10, 10, 3, 3]
li.append(4)
li.insert(2, 6)
print("li", li)

## remove
last_el = li.pop()
print("pop", last_el, li)

# by index
first_el = li.pop(0)
print("pop 0:", first_el, li)

# by value
li.remove(3)  # removes the first 3
print("remove 3", li)
print()

# set: unordered, distinct items

my_empty_set = set()
my_set = {1, 2, 2, 2, 3}
print("my_set", my_set)
my_set.add(5)
print("add 5", my_set)
# adding multiple times is ignored
print(1, my_set)
my_set.add(2)
print(2, my_set)
my_set.add(2)
print(3, my_set)
my_set.remove(2)
print("remove 2", my_set)
print()


# dict: mapping key -> value

my_empty_dict = {}  # or dict()
my_dict = {1: 4, 6: "hey", "hello": 3}
print(my_dict)
is_6_in_dict = 6 in my_dict
print("test membership ", is_6_in_dict)
print("keys are indices: hello ->", my_dict["hello"])

my_dict[1] = "alice"
print("1alice", my_dict)
my_dict["bob"] = "alice"
print("bob", my_dict)
del my_dict["bob"]
print("del", my_dict)

print()

# records

## tuple
point1 = (1, 2)
assert point1[0] == 1
assert point1[1] == 2

# can have arbitrary nb of items
point1 = ()  # or tuple()
point1 = (3 * 4,)  # 1 item
point1 = (1, 1, 2, 3, 45)
# point1[0] = 3  # Error!
print("point1", point1)


## namedtuple  # same as tuple, but w names
from collections import namedtuple
from dataclasses import dataclass

PointNT = namedtuple("PointNT", ["x", "y"])
point2 = PointNT(1, 2)
assert point2.x == 1
assert point2.y == 2
print("point2", point2)

## dataclasses  # mutable
@dataclass
class PointData:
    x: int
    y: int


## these are mutable
point3 = PointData(1, 2)
point3.x = 3
print("point3", point3)
