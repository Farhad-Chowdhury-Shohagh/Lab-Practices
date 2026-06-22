A = [1,2,3,4,5]
B = [2,3,5,7]
C = [2,5,8]

common = set(A) & set(B) & set(C)

print(f"Common Elements: {common}")