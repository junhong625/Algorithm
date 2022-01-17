leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]
not_leap_year = [31,28,31,30,31,30,31,31,30,31,30,31]
week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
day = 1 # 1901년 1월 1일은 화요일
count = 0
for year in range(1901, 2001):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            for d in range(12):
                if week[day] == 'sunday':
                    count += 1
                day = (day + not_leap_year[d]) % 7
        else:
            for d in range(12):
                if week[day] == 'sunday':
                    count += 1
                day = (day + leap_year[d]) % 7
    else:
        for d in range(12):
            if week[day] == 'sunday':
                count += 1
            day = (day + not_leap_year[d]) % 7
print(count)