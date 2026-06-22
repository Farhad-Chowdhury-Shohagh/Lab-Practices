students = {
    "Alice": 'A',
    "Bob": 'B',
    "Charlie": 'A',
    "David": 'C',
    "Eva": 'B'
}

result = {}

for name, grade in students.items():
    if grade not in result:
        result[grade] = []
    result[grade].append(name)

print(f"Outcome: {result}")