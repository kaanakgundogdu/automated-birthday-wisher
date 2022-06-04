import datetime as dt


current_time = dt.datetime.now()
year = current_time.year
print(current_time)
print(year)

date_of_birth = dt.datetime(year=1995, month=7, day=27, hour=8)

print(date_of_birth)
