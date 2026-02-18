n = int(input("Enter number of elements: "))
nums = []

for i in range(n):
    nums.append(float(input("Enter value: ")))

t = tuple(nums)
avg = sum(t) / n

print("Tuple:", t)
print("Average:", avg)
