#googling하는 법
"""
오늘날짜 구하기를 파이썬으로 할 것.
https://www.programiz.com/python-programming/datetime/current-datetime
스택오버플로우 사이트를 참고하면 더 좋다.
"""
#Example 1: Python get today's date
from datetime import date

today = date.today()
print("Today's date:", today)

#Example 2: Current date in different formats
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)

#Example 3: Get the current date and time
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	