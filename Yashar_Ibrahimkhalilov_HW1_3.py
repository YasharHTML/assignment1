sum_ = 0
i = 0
while True:
    n = input("Enter the grade (blank to quit): ")
    if n == "":
        break
    i += 1
    if n == "A+":
        sum_ += 4.0
    elif n == "A":
        sum_ += 4.0
    elif n == "A-":
        sum_ += 3.7
    elif n == "B+":
        sum_ += 3.3
    elif n == "B":
        sum_ += 3.0
    elif n == "B-":
        sum_ += 2.7
    elif n == "C+":
        sum_ += 2.3
    elif n == "C":
        sum_ += 2.0
    elif n == "C-":
        sum_ += 1.7
    elif n == "D+":
        sum_ += 1.3
    elif n == "D":
        sum_ += 1.0
    elif n == "F":
        sum_ += 0.0
    else:
        print("Invalid grade")
        i -= 1
print("\nA grade point average {:.1f}".format(sum_/i))