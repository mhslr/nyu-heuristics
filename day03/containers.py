# list: ordered collection

## insert
li = [1, 2, 10, 10, 3, 3]
li.append(4)
li.insert(2, 6)
print("li", li)

## remove
last_el = li.pop()
print("pop", last_el, li)
first_el = li.pop(0)
print("pop 0", first_el, li)

li.remove(3)  # removes the first 3
print("remove 3", li)
print()

# set: unordered, distinct items

my_empty_set = set()
my_set = {1, 2, 2, 2, 3}
print("my_set", my_set)
my_set.add(5)
print("add 5", my_set)
my_set.add(2)
my_set.add(2)
my_set.remove(2)
print("remove 2", my_set)

# dict: mapping key -> value

my_empty_dict = {}  # or dict()
my_dict = {
    1: 4,
    6: "hey",
    "hello": 3
}
print(my_dict)

print()
# records

## tuple
point1 = (1,2)
point1[0] == 1
point1[1] == 2

# point[0] = 3  # Error!
print('point1', point1)


## namedtuple
from collections import namedtuple
from dataclasses import dataclass

PointNT = namedtuple('Point', ['x','y'])
point2 = PointNT(1,2)
point2.x == 1
point2.y == 2
print('point2', point2)

## dataclasses
@dataclass
class PointData:
    x: int
    y: int

## these are mutable
point3 = PointData(1,2)
point3.x = 3
print('point3', point3)
