#!/usr/bin/env python
#
# the simpsons
# more on dictionaries

relatives = {"Lisa": "daughter", "Bart": "son", "Marge": "mother", "Homer": "father"}

for member in list(relatives.keys()):
    print(member, "is a", relatives[member])

print("Now we'll add in the dog")

if not "Dennis" in list(relatives.keys()):
    relatives["Santa"] = "dog"

for member in list(relatives.keys()):
    print(member, "is a", relatives[member])

print("Now we'll add more properties of Bart:")

relatives["Bart"] = relatives["Bart"] + " Not such a good student"
print(relatives["Bart"])


inname = input("Please give me the name of a family member. ")
if inname in list(relatives.keys()):
    print("Family member", inname, "is a", relatives[inname])
else:
    print(inname, " is not a family member")

print("Now for an unrelated example:")

bank = {"Nicol": 50, "Connie": 60, "Dennis": 5}
print(bank["Nicol"])
