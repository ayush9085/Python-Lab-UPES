s = input("Enter a string: ").upper()

for ch in sorted(set(s)):
    if ch.isalpha():
        print(s.count(ch), ch, sep="")
