
#python program to find number of days bettwen two given days


from datetime import date as date_n

def number_of_days(date_1,date_2):
    return (date_2-date_1).days

date_1=date_n(2023,1,23)
date_2=date_n(2026,1,30)

print("number of days bettween the given dates are",number_of_days(date_1,date_2))