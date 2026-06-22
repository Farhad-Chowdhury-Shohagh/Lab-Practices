data = ((1,5), (2,1), (4,3), (3,2))

result = []

for x in range(1,6):
    for item in data:
        if item[1] == x:
            result.append(item)

print(f"Outcome: {result}")