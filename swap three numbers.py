# Swap three numbers

print("Enter three numbers to swap:")

a = int(input("Enter value of A: "))
b = int(input("Enter value of B: "))
c = int(input("Enter value of C: "))

print("\nBefore swapping:")
print("A =", a)
print("B =", b)
print("C =", c)

# Swapping logic
temp = a
a = b
b = c
c = temp

print("\nAfter swapping:")
print("A =", a)
print("B =", b)
print("C =", c)
