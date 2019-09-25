months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

count = 0
days = 1  # first day is Monday on 1 Jan 1900
days += 365  # skip 1900
for year in range(1901, 2001):
    for month in range(12):
        if days % 7 == 0:
            count += 1
        if month == 1 and year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
            days += 29
        else:
            days += months[month]
print(count)
