(1 + 2) * 3 / 4
dividend = 64 // 7
remainder = 64 % 7
power = 10 ** 5
sqrt2 = 2 ** 0.5

# string: immutable sequence of characters
s = "hello"
s[2:5]  # substring "llo"
s[::-1] # reversed: "olleh"
"abc" + "def"  # "abcdef"
"123 354".split()  # ["123", "354"]
"+".join(["123", "354", "abc"])  # "123+354+abc"
print(f"64 = {dividend} * 7 + {remainder}")
# prints: hello 64 = 9 * 7 + 1
print(f"sqrt(2) = {sqrt2:.5f}")  # prints 5 decimal places
int("123")  # str -> int
str(123)    # int -> str

# dict: has unique keys, maps each key to a value
empty_d = {}
d = {"a": 1, "b": 2}
d["hi"] = 111  # inserts "hi" -> 111
d["hi"] = 333  # remaps  "hi" -> 333
d["hi"]        # get value of "hi": 333
del d["hi"]    # removes "hi" from d

for k, v in d.items():
    ...  # do smth with each (key, value) pair

# list: ordered collection
empty_list = []
li = [1, 2, 3]
li.append(5)        # insert at the end
li.insert(0, 123)   # insert 123 in pos 0, incr indhello 64 = 9 * 7 + 1ices >= 0
li.pop(1)           # delete el at pos 1, decr indices > 1
li[0]               # get value at pos 0: 123
li[0] = 9           # set value at pos 0
len(li)             # get length

li2 = [1, 2] + [5, 6]  # concatenate lists
li2[1:3]  # sublist [2, 5]

for e in li:
    ...  # do smth with each element

# range is like a read-only list containing start..stop-1
start = 3
stop = 10
range(start, stop)

min([1,2,3])
max([1,2,3])
sum([1,2,3])

print()               # prints: (empty line)
print(start)          # prints: 3
print("stop =", stop) # prints: stop = 10

name = input("guess my name: ")
number = int(input("guess my number: "))

lines = open('input.txt').readlines()
print(lines)  # ['this is the first line\n', 'this is the second one\n']
joined_lines = '\n'.join(['my line1', 'my line2'])
open('output.txt', 'w').write(joined_lines)


def my_func(param1, param2):
    # reassigning params will not affect original variables
    # good practice:
    #  do not overwrite parameters
    #  avoid reading/setting values living outside function
    #  return a new value (or a copy of smth)
    result = param1 + param2
    # the variable result is local to this function
    return result

res_3_2 = my_func(3, 2)  # evaluate function

if 1 > 2:   # 1 if
    ...
elif 3 > 2: # 0 or more elif
    ...
else:       # 0 or 1 else
    ...

x = number  # our input
res = []
while x > 0:
    res.insert(0, x % 2)
    x = x // 2
print(res)  # binary repr of number

li = [1, 2, 3, 4, 5]
for x in li:
    if x == 1:
        continue  # skip this x
    if x == 4:
        break  # stop loop
    print(x)  # will print 2 and 3
# good practice:
#  do not modify x (loop variable)
#  do not modify li (loop container)
#  do not reuse last value of x after loop

from copy import deepcopy
# to safely copy a list or dict,
# esp. if it contains nested containers
dict_of_lists = {"list1": [1,2,3], "l2": [8,9,0]}
other = deepcopy(dict_of_lists)
# objects have the same value
assert dict_of_lists == other
assert dict_of_lists['l2'] == other['l2']
# but not same objects
assert dict_of_lists is not other
assert dict_of_lists['l2'] is not other['l2']

# += is evil, use a = a + 1
# arrows point to things
# arrows cannot point inside of things
# for generates "fresh" values from a predefined list
