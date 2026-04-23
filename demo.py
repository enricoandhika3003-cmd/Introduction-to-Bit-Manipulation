num1 = 10
num2 = 4

print("num1 & num2 =", num1 & num2)

print("\nnum1 | num2 =", num1 | num2)

print("\n~num1 =", ~num1)

print("\nnum1 ^ num2 =", num1 ^ num2)

num1 = 10
num2 = 4

print("\nnum1 >> 1 =", num1 >> 1)

print("\nnum2 >> 1 =", num2 >> 1)

num1 = 10
num2 = 4

print("\nnum1 << 1 =", num1 << 1)

print("\nnum2 << 1 =", num2 << 1)

#Odd or Even Bitwise
def odd_or_even(n):
    if (n^1 == n+1):
        return True;
    else:
        return False;

num = int(input("Enter a random value: "))

if odd_or_even(num):
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

#Number of Bits
def numofBits(x):
    count = 0
    while (n):
        count += 1
        n >>= 1
    return count
number = int(input("Enter a number: "))
print("Total bits: ", numofBits)

#Implement Circuits
A & B = A*B
B | C = B+C
B & C = B*C
B|C & B&C = (B+C)*(B*C)
A&B | (B|C & B&C) = (A*B)+((B+C)*(B*C))
(B+C)*(B*C) = B*C
(A*B) + (B*C) = B(A+C)
