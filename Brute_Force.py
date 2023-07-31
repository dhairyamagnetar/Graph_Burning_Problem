import time
def check(burned):
    for i in burned:
        if not i:
            return False
    return True

def burn(v, burned):
    burned[v] = 1


def nextpermutation(a):
    # Find the largest index i such that a[i] < a[i + 1]. If no such
    # index exists, the permutation is the last permutation
    for i in reversed(range(len(a) - 1)):
        if a[i] < a[i + 1]:
            break  # found
    else:  # no break: not found
        return False  # no next permutation

    # Find the largest index j greater than i such that a[i] < a[j]
    j = next(j for j in reversed(range(i + 1, len(a))) if a[i] < a[j])

    # Swap the value of a[i] with that of a[j]
    a[i], a[j] = a[j], a[i]

    # Reverse sequence from a[i + 1] up to and including the final element a[n]
    a[i + 1:] = reversed(a[i + 1:])
    return True

def propagate(burned, g, v):
    for i in range(v):
        if burned[i] == 1:
            size = len(g[i])
            for j in range(size):
                if burned[g[i][j]] == 0:
                    burned[g[i][j]] = 2
    for i in range(v):
        if burned[i] == 2:
            burned[i] = 1

def rounds(seq, burned, g, v):
    for i in range(v):
        propagate(burned, g, v)
        burn(seq[i], burned)
        if check(burned):
            return i + 1
    return v

v, e = map(int, input("Enter the number of vertices and edges in the graph: ").split())

g = [[] for _ in range(v)]

if e:
    print("Enter the edges:")

for _ in range(e):
    edge = input().split()
    a, b = map(int, edge)
    g[a].append(b)
    g[b].append(a)

start_time = time.time()
seq = list(range(v))
b = v

while True:
    burned = [0] * v  # Reset the burned list before each call to rounds
    b = min(b, rounds(seq, burned, g, v))
    if not nextpermutation(seq):
        break

print("The burning number is:",b)

end_time = time.time()
print("Running time :",end_time-start_time)