A = [1, 2, 3, 4, 5, 5]
B = [4, 5, 6, 7, 8, 8]

A = set(A)
B = set(B)

print(A ^ B) # Unique for each
print(A | B) # Unique for union
print(A & B) # Intersecting