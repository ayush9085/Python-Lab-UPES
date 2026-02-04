marks = []
for i in range(5):
    marks.append(int(input(f"Enter marks of subject {i+1}: ")))

percentage = sum(marks) / 5
cgpa = percentage / 10

print("Percentage:", percentage)
print("CGPA:", cgpa)

if cgpa <= 3.4:
    print("Grade: F")
elif cgpa <= 5.0:
    print("Grade: C+")
elif cgpa <= 6.0:
    print("Grade: B")
elif cgpa <= 7.0:
    print("Grade: B+")
elif cgpa <= 8.0:
    print("Grade: A")
elif cgpa <= 9.0:
    print("Grade: A+")
else:
    print("Grade: O (Outstanding)")
