def pol(n): # this is the function to convert to polindrome
    return n == n[::-1] # if this satisfies the condition, it returns True

def toBin(n): # this is the function to convert to binary
    if n == 0: # if the number is 0 
        return "" # if the number is 0, we return an empty string
    return toBin(n//2) + str(n % 2) # this is the recursive function, and it returns the binary version of the number n

print("Decimal and Binary Polindroms") # this is the title of the program
n = input("Enter a number (N>0): ") # getting the number
flag1 = pol(n) # this is the first condition to check if the number is polindrom
n_but_bin = toBin(int(n)) # this is the binary version of the number
flag2 = pol(toBin(int(n))) # this is the second condition to check if the binary version of the number is polindrom
print("Decimal ->", n) # printing the decimal version of the number
print("Binary ->", n_but_bin) # printing the binary version of the number
if flag1 and flag2: # if both conditions are satisfied
    print("Polindron type is Decimal and Binary.") # printing the result
elif flag1: # if only the first condition is satisfied
    print("Polindron type is only Decimal.") # printing the result
elif flag2: # if only the second condition is satisfied
    print("Polindron type is only Binary.") # printing the result
else: # if none of the conditions are satisfied
    print("Polindron type is neither Decimal nor Binary.") # printing the result