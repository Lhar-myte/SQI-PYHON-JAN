# with open("manual.txt", "r") as f:
#     content = f.readlines()

# print(content)


# with open("employee_records.csv", "r") as f:
#     rows = f.readlines()
#     header = rows[0]
#     data = rows[1:]

#     processed_data = []

#     for row in data:
#         print(row)
#         employee_id, name, age, dept = row.split(",")
#         dept = dept.strip()
#         age = int(age)
#         name = name.upper()
#         processed_data.append((employee_id, name, age, dept))

#     print(processed_data)

# employees_above_29 = []

# for row in processed_data:
#     employee_id, name, age, _ = row

#     if age > 29:
#         employees_above_29.append((employee_id, name))

# print(employees_above_29)

# sum_of_ages = 0

# for row in processed_data:
#     _, _, age, _ = row
#     sum_of_ages += age

# mean_age = sum_of_ages / len(processed_data)
# print(mean_age)

# print(processed_data)

# with open("processed_employee_records.csv", "w") as f:
#     f.write(header)
#     for record in processed_data:
#         employee_id, name, age, dept = record
#         f.write(f"{employee_id},{name},{age},{dept}\n")


# nums = ['1', '2', '3']

# for i, num in enumerate(nums):
#     nums[i] = int(num)


# print(nums)



# Python Gotcha
# nums = ['1', '2', '3']

# for i, num in enumerate(nums):
#     print(i)
#     print(nums)
#     nums.append(int(num))


# print(nums)


# with open("manual.txt", "r") as f:
#     # line = f.readline()
#     # print(line)
#     # line = f.readline()
#     # print(line)
#     # content = f.read()

#     lines = f.readlines()
#     # for i, line in enumerate(lines):
#     #     lines[i] = line.strip()
#     # print(lines)

#     stripped = [line.strip() for line in lines]

#     print(stripped)



# with open("automatic.txt", "a") as f:
#     f.write("""This is the appended line.
#     This is the second appended line.
# """)
    
# with open("automatic.txt", "a") as f:
#     f.write("""
# I just appended this line.
# """)

# f = open("automatic.txt", "w")
# f.close()


# import os

# import sys


# i = 0

# while i <= 10:
#     print(i)
#     if i == 7:
#         break
#     i += 1

# print("This is the end of the file")


# import math


# print(math.sqrt(9))

# # print(math.sin()

# print(math.log(1000, 10))


import datetime

current_year = datetime.datetime.now().year

birth_day = datetime.date(current_year, 2, 19)

today = datetime.datetime.today().date()

if birth_day < today:
    print("Your birthday has passed")
elif birth_day == today:
    print("Happy bIrthday")
else:
    print("Your birthday is coming.")


str_date = "2025-02-19 11:40"

parsed_date = datetime.datetime.strptime(str_date, "%Y-%m-%d %H:%M")

print(parsed_date)

# 2025/02/19

today = datetime.datetime.today()
str_today = datetime.datetime.strftime(today, "%Y/%m/%d")
print(str_today)