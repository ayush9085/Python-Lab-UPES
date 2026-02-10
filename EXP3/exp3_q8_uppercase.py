s = input("Enter a string: ")
result = ""
for ch in s:
    if 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)
    else:
        result += ch
print(result)
