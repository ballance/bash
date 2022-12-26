from datetime import date, timedelta, datetime
import decimal

start_date = date(2018, 5, 25) 
end_date = datetime.now().date()

delta = end_date - start_date   # returns timedelt
#print(start_date)
#print(end_date)

txt = 'Sebastian is {age:.0f} days old.'
print(txt.format(age = delta.days))

txt2 = 'Sebastian is {age:.2f} years old.'
age_in_years =  delta.days / decimal.Decimal('365')
print(txt2.format(age = age_in_years))
# for i in range(delta.days + 1):
#    day = start_date + timedelta(days=i)
#    print(day)
