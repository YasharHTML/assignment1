print("Look and Say Numbers")
n = input("Enter a number (N>0): ")
if len(n) % 2 != 0:
    print("invalid")
else:
    for i in range(0, len(n)-1, 2):
        print(n[i+1] * int(n[i]), end="")