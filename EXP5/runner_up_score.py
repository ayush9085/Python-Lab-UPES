n = int(input("Enter number of students: "))
scores = []

print("Enter scores one by one:")
for i in range(n):
    scores.append(int(input()))

unique_scores = list(set(scores))
unique_scores.sort(reverse=True)

if len(unique_scores) > 1:
    print("Runner-up score:", unique_scores[1])
else:
    print("No runner-up score")
