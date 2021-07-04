from datetime import  datetime, timedelta


now = datetime.now()

print(now)
print(now.year)
print(now.month)
print(now.date())
print(now.day)
print(now.hour)
print(now.date())

# FORMATTING DATETIME
print("FORMATTING DATE AND TIME")
print(now.strftime("%D"))
print(now.strftime("Today is %B %d %Y %H:%M:%S %p"))


# FUTURE AND PAST DATE AND TIME

future_date = datetime.now() + timedelta(days=1)
print(future_date.strftime("Tomorrow is %B %d %Y"))
past_date = datetime.now() - timedelta(days=1)
print(past_date.strftime("Yesterday was %B %d %Y"))


if __name__ == '__main__':
    pass

