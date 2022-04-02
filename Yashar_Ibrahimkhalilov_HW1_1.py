print("Determine your zodiac sign")
n = input("Enter month [ex. March]: ")
m = int(input("Enter the day [ex. 12]: "))

def change_to_month(month):
    if month == "January":
        return 1
    elif month == "February":
        return 2
    elif month == "March":
        return 3
    elif month == "April":
        return 4
    elif month == "May":
        return 5
    elif month == "June":
        return 6
    elif month == "July":
        return 7
    elif month == "August":
        return 8
    elif month == "September":
        return 9
    elif month == "October":
        return 10
    elif month == "November":
        return 11
    elif month == "December":
        return 12

month_in_number = change_to_month(n)

def isValid(day, month):
    if month == 1 and day <= 31:
        return True
    elif month == 2 and day <= 28:
        return True
    elif month == 3 and day <= 31:
        return True
    elif month == 4 and day <= 30:
        return True
    elif month == 5 and day <= 31:
        return True
    elif month == 6 and day <= 30:
        return True
    elif month == 7 and day <= 31:
        return True
    elif month == 8 and day <= 31:
        return True
    elif month == 9 and day <= 30:
        return True
    elif month == 10 and day <= 31:
        return True
    elif month == 11 and day <= 30:
        return True
    elif month == 12 and day <= 31:
        return True
    else:
        return False

if isValid(m, month_in_number):
    if month_in_number == 1:
        if m >= 20:
            print("Your zodiac sign is Aquarius")
        else:
            print("Your zodiac sign is Capricorn")
    elif month_in_number == 2:
        if m >= 19:
            print("Your zodiac sign is Pisces")
        else:
            print("Your zodiac sign is Aquarius")
    elif month_in_number == 3:
        if m >= 21:
            print("Your zodiac sign is Aries")
        else:
            print("Your zodiac sign is Pisces")
    elif month_in_number == 4:
        if m >= 20:
            print("Your zodiac sign is Taurus")
        else:
            print("Your zodiac sign is Aries")
    elif month_in_number == 5:
        if m >= 21:
            print("Your zodiac sign is Gemini")
        else:
            print("Your zodiac sign is Taurus")
    elif month_in_number == 6:
        if m >= 21:
            print("Your zodiac sign is Cancer")
        else:
            print("Your zodiac sign is Gemini")
    elif month_in_number == 7:
        if m >= 23:
            print("Your zodiac sign is Leo")
        else:
            print("Your zodiac sign is Cancer")
    elif month_in_number == 8:
        if m >= 23:
            print("Your zodiac sign is Virgo")
        else:
            print("Your zodiac sign is Leo")
    elif month_in_number == 9:
        if m >= 23:
            print("Your zodiac sign is Libra")
        else:
            print("Your zodiac sign is Virgo")
    elif month_in_number == 10:
        if m >= 23:
            print("Your zodiac sign is Scorpio")
        else:
            print("Your zodiac sign is Libra")
    elif month_in_number == 11:
        if m >= 22:
            print("Your zodiac sign is Sagittarius")
        else:
            print("Your zodiac sign is Scorpio")
    elif month_in_number == 12:
        if m >= 22:
            print("Your zodiac sign is Capricorn")
        else:
            print("Your zodiac sign is Sagittarius")
else:
    print("Either a month or a day is invalid!")