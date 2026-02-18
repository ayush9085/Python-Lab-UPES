n = int(input("Enter number of students: "))
students = {}

for i in range(n):
    name = input("Enter name: ")
    city = input("Enter city: ")
    students[name] = city

print("\nAll Names:")
for name in students.keys():
    print(name)

print("\nAll Cities:")
for city in students.values():
    print(city)

print("\nStudent Details:")
for name, city in students.items():
    print(name, "-", city)

city_count = {}
for city in students.values():
    city_count[city] = city_count.get(city, 0) + 1

print("\nStudents in each city:")
for city, count in city_count.items():
    print(city, ":", count)
