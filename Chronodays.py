def find(month, year):
    dict={ "January":31,
           "February":28,
           "March":31,
           "April":30,
           "May":31,
           "June":30,"July":31,
           "August":31,
           "September":30,
           "October":31,
           "November":30,
           "December":31}

    if ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)) and month == "February":
            return 29
    else:
        return dict[month]
        


year=int(input ("enter a year"))
month=input ("enter a month").title()
s=find(month,year)
print(f"{month} contains {s} days")






























