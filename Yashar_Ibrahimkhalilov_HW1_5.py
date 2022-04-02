def pol(n):
    return n == n[::-1] # if this satisfies the condition, it returns True

def toBin(n):
    if n == 0:
        return ""
    return toBin(n//2) + str(n % 2)  

print("Decimal and Binary Polindroms")
n = input("Enter a number (N>0): ")
flag1 = pol(n)
n_but_bin = toBin(int(n))
flag2 = pol(toBin(int(n)))
print("Decimal ->", n)
print("Binary ->", n_but_bin)
if flag1 and flag2:
    print("Polindron type is Decimal and Binary.")
elif flag1:
    print("Polindron type is only Decimal.")
elif flag2:
    print("Polindron type is only Binary.")
else:
    print("Polindron type is neither Decimal nor Binary.")