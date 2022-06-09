import random

fname = "../day05/Diff2Mean.vals"
with open(fname) as fp:
    lines = fp.readlines()
    grpA = [float(nb) for nb in lines[1].split()]
    grpB = [float(nb) for nb in lines[3].split()]
    print("grpA", grpA)
    print("grpB", grpB)


def compute_mean_diff(grp1, grp2):
    return (sum(grp1) / len(grp1)) - (sum(grp2) / len(grp2))


real_mean_diff = compute_mean_diff(grpA, grpB)

results = []
n_samples = 10000
for test in range(n_samples):
    both = grpA + grpB

    A1 = random.choices(both, k=len(grpA))
    B1 = random.choices(both, k=len(grpB))
    mean_diff = compute_mean_diff(A1, B1)
    results.append(mean_diff)

sres = sorted(results)
ilow = int(0.05 * n_samples)
ihigh = int(0.95 * n_samples)
print("confidence interval:", sres[ilow], sres[ihigh])
print("real mean diff:", real_mean_diff)
