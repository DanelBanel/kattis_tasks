data = input().lower()
total_letters = 0
for char in data:
    if char.isalpha():
        total_letters += 1
print(total_letters)