n = int(input("Enter number of values: "))
values = []

print("Enter values (0 to 3):")
for i in range(n):
    values.append(int(input()))

count = {0: 0, 1: 0, 2: 0, 3: 0}

for v in values:
    if v in count:
        count[v] += 1

print("Occurrences:")
for k in count:
    print(k, "occurred", count[k], "times")
