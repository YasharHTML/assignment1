#getting inputs ready
print("Determine your zodiac sign") # this is the title of the program
n = input("Enter month [ex. March]: ") # getting the month
m = int(input("Enter the day [ex. 12]: ")) # getting the day

# months used to be a string, but now they are an int (-1 for false names)
def change_to_month(month): # this is the function to change the month to an int
    if month == "January": # if the month is January
        return 1 # we return 1
    elif month == "February": # if the month is February
        return 2 # we return 2
    elif month == "March": # if the month is March
        return 3 # we return 3
    elif month == "April": # if the month is April
        return 4 # we return 4
    elif month == "May": # if the month is May
        return 5 # we return 5
    elif month == "June": # if the month is June
        return 6 # we return 6 
    elif month == "July": # if the month is July
        return 7 # we return 7
    elif month == "August": # if the month is August
        return 8 # we return 8
    elif month == "September": # if the month is September
        return 9 # we return 9
    elif month == "October": # if the month is October
        return 10 # we return 10 
    elif month == "November": # if the month is November
        return 11 # we return 11 
    elif month == "December": # if the month is December
        return 12 # we return 12 
    else:   # if the month is invalid
        return -1 # we return -1
# changing it to an int
month_in_number = change_to_month(n) # this is the month in number


# day validation, for the month of january has only 31 days

def isValid(day, month): # this is the function to check if the day is valid
    if month == 1 and day <= 31:    # if the month is January
        return True # we return True
    elif month == 2 and day <= 28: # if the month is February
        return True # we return True
    elif month == 3 and day <= 31: # if the month is March
        return True # we return True
    elif month == 4 and day <= 30: # if the month is April
        return True # we return True
    elif month == 5 and day <= 31: # if the month is May
        return True # we return True
    elif month == 6 and day <= 30: # if the month is June
        return True # we return True
    elif month == 7 and day <= 31: # if the month is July
        return True # we return True
    elif month == 8 and day <= 31:  # if the month is August
        return True # we return True
    elif month == 9 and day <= 30: # if the month is September
        return True # we return True
    elif month == 10 and day <= 31: # if the month is October
        return True # we return True
    elif month == 11 and day <= 30: # if the month is November
        return True # we return True
    elif month == 12 and day <= 31: # if the month is December
        return True # we return True
    else: # if the month is invalid
        return False # if the day is not valid

# if the day is valid, then it will be used to determine the zodiac sign

if isValid(m, month_in_number): # if the day is valid
    if month_in_number == 1: # if the month is January
        if m >= 20: # if the day is greater than or equal to 20
            print("Your zodiac sign is Aquarius") # we print Aquarius
        else: # if the day is less than 20
            print("Your zodiac sign is Capricorn") # we print Capricorn
    elif month_in_number == 2: # if the month is February
        if m >= 19: # if the day is greater than or equal to 19
            print("Your zodiac sign is Pisces") # we print Pisces
        else: # if the day is less than 19
            print("Your zodiac sign is Aquarius") # we print Aquarius
    elif month_in_number == 3:  # if the month is March 
        if m >= 21: # if the day is greater than or equal to 21
            print("Your zodiac sign is Aries") # we print Aries
        else: # if the day is less than 21
            print("Your zodiac sign is Pisces") # we print Pisces
    elif month_in_number == 4: # if the month is April
        if m >= 20: # if the day is greater than or equal to 20
            print("Your zodiac sign is Taurus") # we print Taurus
        else: # if the day is less than 20 
            print("Your zodiac sign is Aries") # we print Aries
    elif month_in_number == 5: # if the month is May
        if m >= 21: # if the day is greater than or equal to 21
            print("Your zodiac sign is Gemini") # we print Gemini
        else: # if the day is less than 21
            print("Your zodiac sign is Taurus") # we print Taurus
    elif month_in_number == 6: # if the month is June 
        if m >= 21: # if the day is greater than or equal to 21
            print("Your zodiac sign is Cancer") # we print Cancer 
        else: # if the day is less than 21 
            print("Your zodiac sign is Gemini") # we print Gemini
    elif month_in_number == 7: # if the month is July
        if m >= 23: # if the day is greater than or equal to 23
            print("Your zodiac sign is Leo") # we print Leo
        else: # if the day is less than 23
            print("Your zodiac sign is Cancer") # we print Cancer
    elif month_in_number == 8: # if the month is August
        if m >= 23: # if the day is greater than or equal to 23
            print("Your zodiac sign is Virgo")  # we print Virgo
        else: # if the day is less than 23
            print("Your zodiac sign is Leo") # we print Leo
    elif month_in_number == 9: # if the month is September
        if m >= 23: # if the day is greater than or equal to 23
            print("Your zodiac sign is Libra") # we print Libra
        else: # if the day is less than 23
            print("Your zodiac sign is Virgo") # we print Virgo
    elif month_in_number == 10: # if the month is October
        if m >= 23: # if the day is greater than or equal to 23
            print("Your zodiac sign is Scorpio") # we print Scorpio
        else: # if the day is less than 23
            print("Your zodiac sign is Libra") # we print Libra
    elif month_in_number == 11: # if the month is November
        if m >= 22: # if the day is greater than or equal to 22
            print("Your zodiac sign is Sagittarius") # we print Sagittarius
        else: # if the day is less than 22
            print("Your zodiac sign is Scorpio") # we print Scorpio
    elif month_in_number == 12: # if the month is December
        if m >= 22: # if the day is greater than or equal to 22
            print("Your zodiac sign is Capricorn") # we print Capricorn
        else: # if the day is less than 22 
            print("Your zodiac sign is Sagittarius") # we print Sagittarius
else: # if the day is invalid
    print("Either a month or a day is invalid!") # we print this message, because theuser entered an invalid month or day