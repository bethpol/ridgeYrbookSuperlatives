candidates = open("candidates.txt", "r")
counter = dict()

for line in candidates:
    l = line.rstrip().upper()
    counter[l] = counter.get(l, 0) + 1

print(counter)
