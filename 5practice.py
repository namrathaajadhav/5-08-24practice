#help('modules')
#random

import random

random_number = random.randint(1, 100)
print(random_number)



import random
roll_numbers = random.randint(115, 220)
print("your roll:", roll_numbers)



#math

import math
number = 36
square_root = math.sqrt(number)
print(square_root)


import math
number = 3.4
square_root = math.ceil(number)
print(square_root)



import math
number = 10.8
square_root = math.floor(number)
print(square_root)

#datetime

import datetime

today = datetime.date.today()
print(today)

#time
now = datetime.datetime.now()
print(now)


#calendar
import calendar

year = 2024
month = 5
print(calendar.month(year, month ))



#shuffle
import random

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)
