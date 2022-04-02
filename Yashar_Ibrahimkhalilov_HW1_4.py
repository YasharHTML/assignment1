print("Look and Say Numbers") # this is the title of the program
n = input("Enter a number (N>0): ") # getting the number
if len(n) % 2 != 0: # if the length of the number is odd
    print("invalid") # we don't want numbers with odd length
else: # if the length is even
    for i in range(0, len(n)-1, 2): # we are going through the number in pairs
        print(n[i+1] * int(n[i]), end="") # using string method to achieve the task