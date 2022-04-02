sum_ = 0 # this is the sum of the grades
i = 0 # amount of grades
while True: # this is the loop to get the grades
    n = input("Enter the grade (blank to quit): ") # getting the grade
    if n == "": # if the grade is blank
        break # we are breaking the loop
    i += 1 # we are increasing the amount of grades
    if n == "A+": # if the grade is A+
        sum_ += 4.0 # 4.0 is the value of the grade
    elif n == "A": # if the grade is A
        sum_ += 4.0 # 4.0 is the value of the grade
    elif n == "A-": # if the grade is A-
        sum_ += 3.7 # 3.7 is the value of the grade
    elif n == "B+": # if the grade is B+
        sum_ += 3.3 # 3.3 is the value of the grade
    elif n == "B": # if the grade is B
        sum_ += 3.0 # 3.0 is the value of the grade
    elif n == "B-": # if the grade is B-
        sum_ += 2.7 # 2.7 is the value of the grade
    elif n == "C+": # if the grade is C+
        sum_ += 2.3 # 2.3 is the value of the grade
    elif n == "C": # if the grade is C
        sum_ += 2.0 # 2.0 is the value of the grade
    elif n == "C-": # if the grade is C-
        sum_ += 1.7 # 1.7 is the value of the grade
    elif n == "D+": # if the grade is D+
        sum_ += 1.3 # 1.3 is the value of the grade
    elif n == "D": # if the grade is D
        sum_ += 1.0 # 1.0 is the value of the grade
    elif n == "F": # if the grade is F
        sum_ += 0.0 # 0.0 is the value of the grade
    else: # if the grade is invalid
        print("Invalid grade") # if the grade is invalid
        i -= 1 # we don't count it
print("\nA grade point average {:.1f}".format(sum_/i)) # printing the average