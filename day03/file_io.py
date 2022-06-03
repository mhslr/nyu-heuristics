# file input / output

txt = open("sample.txt").read()  # 1 string
lines = open("sample.txt").readlines()  # list of strings
print('lines', lines)

for line in open("sample.txt"): 
    # same as
    # for line in open().readlines():
    print(f"{line!r}")

# modes
## [w]rite
## [a]ppend
## [r]ead

# 'rb' read binary

# fp file pointer
fp = open("output.txt", "w")
for line in lines[::-1]:
    fp.write(line)
fp.close()

# with will close fp automatically
with open('output.txt', 'a') as fp5:
    fp5.write('hi\n')

# context manager: auto cleanup

with open("sample.txt") as fp2:
    # a file pointer can only be read once
    print(len(fp2.read()))
    print(len(fp2.read()))
    # reset
    fp2.seek(30)
    print(len(fp2.read()))

