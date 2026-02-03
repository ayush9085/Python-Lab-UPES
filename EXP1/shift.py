num = int(input("Enter a number: "))
shift = int(input("Enter number of positions to shift: "))

left_shift = num << shift
right_shift = num >> shift

print("Left Shift Result (num << shift):", left_shift)
print("Right Shift Result (num >> shift):", right_shift)
