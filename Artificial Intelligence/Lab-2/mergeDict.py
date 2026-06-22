d1 = {'a': 10 , 'b': 20}
d2 = {'b': 30, 'c': 40}

result = d1.copy()

for key, value in d2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value

print(f"Outcome: {result}")