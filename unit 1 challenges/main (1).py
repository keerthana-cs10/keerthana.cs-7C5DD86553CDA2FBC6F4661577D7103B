def is Leapyear(year):
  if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
    return True
  else:
    return false


year = 2013

if isLeapyear(year):
  print('{} is a Leap year.'.format(year))
else:
  print('{} is not a Leap Year 
  .'.format(year))
      