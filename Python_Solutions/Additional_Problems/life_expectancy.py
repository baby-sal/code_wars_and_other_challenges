# __ Time Left to Live __
#
# Take a users input, in date format, of their date of birth (DDMMYYYY).
# Then take that users life expectancy.
#
# Provide them with the dire news of how long they have left to live.
#
# Provide the news in the format of;
# - First: Years left to live
# - Second: Minutes left to live
# - Third: Seconds left to live
from datetime import datetime

def life_expectancy():
    dob = input("What is your date of birth? (DDMMYYYY): ")
    date_of_birth = datetime.strptime(dob, "%d%m%Y")
    dod = input("What date will you pass away? (DDMMYYYY): ")
    date_of_death = datetime.strptime(dod, "%d%m%Y")
    difference = (date_of_death - date_of_birth).days
    diff_years = difference / 365
    print(f"You will live {diff_years} more years")
    diff_minutes = difference * 24 * 24
    print(f"You will live {diff_minutes} more minutes")
    diff_seconds = diff_minutes * 60
    print(f"You will live {diff_seconds} more seconds")
    return

if __name__ == "__main__":
    print(life_expectancy())


