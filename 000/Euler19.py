month_length = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 31, 31]

def get_month_length(index, year):
  if index is 1:
    if year % 100 is 100:
      return 29 if year % 400 is 0 else 28
    return 29 if year % 4 is 0 else 28
  return month_length[index]

current_day = 1
sunday_count = 0;
for year in range(1901,2001):
  for month in range(12):
    if current_day % 7 is 0:
      sunday_count += 1
    current_day += get_month_length(month, year)
    
print sunday_count