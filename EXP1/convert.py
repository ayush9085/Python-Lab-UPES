# Taking input from user
seconds = int(input("Enter total seconds: "))

# Calculating hours, minutes and seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60

# Printing result
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", remaining_seconds)
