empty_list = []
empty_constructor = list()
numbers = [1, 2, 3]
mixed_types = [1, "hello", 3.14]
from_tuple = list(("apple", "banana"))
from_string = list("Python")
from_set = list({10, 20, 20, 30})
print("Empty Lists:", empty_list, empty_constructor)
print("Direct Init:", numbers)
print("From tuple:", from_tuple)
print("From String:", from_string)
print("From Set (duplicates removed):", from_set)