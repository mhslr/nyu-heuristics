# file input / output

txt = open("sample.txt").read()
lines = open("sample.txt").readlines()
breakpoint()

for line in open("sample.txt"):
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

# context manager: auto cleanup

with open("sample.txt") as fp2:
    # a file pointer can only be read once
    print(len(fp2.read()))
    print(len(fp2.read()))
    # reset
    fp2.seek(0)
    print(len(fp2.read()))
