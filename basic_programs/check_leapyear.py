# Check Leap year
def check_leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

try:
    year = int(input("Enter a year: "))
    if 1000 <= year <= 9999: 
        check_leapyear(year)
        exit(0)
    print("Please entre the 4 digit year")
except: 
    print("Please enter the valid number")