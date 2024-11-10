# שם: דניאל מורגוליס ת"ז 308867548

# תנאים: 1

num1 = float(input("Enter the first decimal number: "))
num2 = float(input("Enter the second decimal number: "))

small = min(num1, num2)

print(f"{small} {small} {small}")


# תנאים: 2

num1 = int(input("הכנס מספר שלם ראשון: "))
num2 = int(input("הכנס מספר שלם שני: "))

average = (num1 + num2) / 2

print("הממוצע של שני המספרים הוא:", average)


# תנאים: 3

num1 = float(input("הכנס מספר עשרוני ראשון: "))
num2 = float(input("הכנס מספר עשרוני שני: "))
num3 = float(input("הכנס מספר עשרוני שלישי: "))

max_num = max(num1, num2, num3)

print("המספר הגדול ביותר הוא:", max_num)


# תנאים: 4

minutes = int(input("Enter the length of the movie in minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print(f"{hours} hour(s) and {remaining_minutes} minute(s)")


# תנאים: 5

number = input("Enter a 4-digit number: ")

if len(number) == 4 and number.isdigit():
    rightmost_digit = number[-1]
    print(f"The rightmost digit is: {rightmost_digit}")
else:
    print("Invalid input. Please enter a 4-digit number.")


# תנאים: 6

number = input("Enter a 4-digit number: ")

if len(number) == 4 and number.isdigit():
    second_rightmost_digit = number[-2]
    print(f"The second rightmost digit is: {second_rightmost_digit}")
else:
    print("Invalid input. Please enter a 4-digit number.")


# תנאים: 7

number = input("Enter a 2-digit number: ")

if len(number) == 2 and number.isdigit():
    digit_sum = int(number[0]) + int(number[1])
    print(f"The sum of the digits is: {digit_sum}")
else:
    print("Invalid input. Please enter a 2-digit number.")


# תנאים: 8

number = input("Enter a 2-digit number: ")

if len(number) == 2 and number.isdigit():
    reversed_number = number[::-1]
    print(f"The reversed number is: {reversed_number}")
else:
    print("Invalid input. Please enter a 2-digit number.")


# תנאים: 9

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# תנאים 10:  - מס הכנסה

salary = float(input("הכנס את המשכורת החודשית שלך: "))

tax = 0

if salary <= 6000:
    tax = 0
elif salary <= 12000:
    tax = (salary - 6000) * 0.10
elif salary <= 18000:
    tax = (12000 - 6000) * 0.10 + (salary - 12000) * 0.20
elif salary <= 25000:
    tax = (12000 - 6000) * 0.10 + (18000 - 12000) * 0.20 + (salary - 18000) * 0.30
elif salary <= 35000:
    tax = (12000 - 6000) * 0.10 + (18000 - 12000) * 0.20 + (25000 - 18000) * 0.30 + (salary - 25000) * 0.35
else:
    tax = (12000 - 6000) * 0.10 + (18000 - 12000) * 0.20 + (25000 - 18000) * 0.30 + (35000 - 25000) * 0.35 + (salary - 35000) * 0.40

print(f"המס שעליך לשלם הוא: {tax:.2f} ")

# אופציה שניה

income = float(input("Enter income: "))
tax = 0

if income <= 6000:
    tax = 0
elif income <= 12000:
    tax = income * 0.1
elif income <= 18000:
    tax = income * 0.2
elif income <= 25000:
    tax = income * 0.3
elif income <= 35000:
    tax = income * 0.4
elif income <= 50000:
    tax = income * 0.5
else:
    tax = income * 0.51

print(f"Income tax: {tax}")



# תנאים 11: רכבת הרים

age = int(input("Enter your age: "))
height = int(input("Enter your height in cm: "))

if 8 <= age <= 18:
    if height > 115:
        print("You are allowed to ride the roller coaster.")
    else:
        print("You are not allowed to ride the roller coaster (Height too short).")
elif age > 18:
    if height > 100:
        print("You are allowed to ride the roller coaster.")
    else:
        print("You are not allowed to ride the roller coaster (Height too short).")
else:
    print("You are not allowed to ride the roller coaster (Age too young).")





# לולאות 1:

# For

top = int(input("הכנס מספר שלם חיובי: "))

for i in range(1, top + 1):
    print(i)

# Wile

top = int(input("הכנס מספר שלם חיובי: "))

i = 1
while i <= top:
    print(i)
    i += 1


# לולאות 2:

num1 = int(input("הכנס מספר שלם ראשון: "))
num2 = int(input("הכנס מספר שלם שני: "))

start = min(num1, num2)
end = max(num1, num2)

for i in range(start, end + 1):
    print(i)


# לולאות 3:

n = int(input("הכנס מספר: "))

for i in range(0, n + 1, 2):
    print(i)


# לולאות 4:

max_num = int(input("הכנס את המספר הראשון (max): "))
den = int(input("הכנס את המספר השני (den): "))

for i in range(den, max_num + 1, den):
    print(i)




# איבוד נתונים 1: עד שיקלט -99

total = 0

first_input = int(input("הכנס מספר: "))

if first_input == -99:
    print(None)
else:
    total += first_input
    while True:
        num = int(input("הכנס מספר: "))
        if num == -99:
            break
        total += num
    print("סכום המספרים הוא:", total)


# איבוד נתונים 2: שלילי או 0

numbers = []

while True:
    num = int(input("הכנס מספר: "))

    if num == -99:
        print(None)
        break
    elif num <= 0:
        break

    numbers.append(num)

if num != -99 and numbers:
    highest = max(numbers)
    lowest = min(numbers)
    print(f"הערך הגבוה ביותר הוא: {highest}")
    print(f"הערך הנמוך ביותר הוא: {lowest}")


# איבוד נתונים 3: 5 מספרים

numbers = []
for i in range(5):
    num = int(input(f"הכנס מספר {i + 1}: "))
    numbers.append(num)

max_value = max(numbers)
max_index = numbers.index(max_value)

print("המספר הסידורי של הערך הגבוה ביותר הוא:", max_index + 1)


# איבוד נתונים 4: כפל, חיבור בלבד

a = int(input("הכנס את המספר הראשון: "))
b = int(input("הכנס את המספר השני: "))

result = 0
for _ in range(abs(b)):
    result += a

if b < 0:
    result = -result

print("תוצאת המכפלה היא:", result)


# איבוד נתונים 5: חזקות, כפל בלבד

a = int(input("הכנס את המספר הראשון: "))
b = int(input("הכנס את המספר השני (החזקה): "))

for _ in range(abs(b)):
    result *= a

if b < 0:
    result = 1 / result

print(f"תוצאת החזקה היא: {result}")


# איבוד נתונים 6 אתגר : סמפר וספרה נכון לא נכון

digit = input("הכנס ספרה: ")
number = input("הכנס מספר: ")

if digit in number:
    print("True")
else:
    print("False")


# איבוד נתונים 7 אתגר : 2 סמפרים והמחלק

num1 = int(input("הכנס את המספר הראשון: "))
num2 = int(input("הכנס את המספר השני: "))

while num2 != 0:
    num1, num2 = num2, num1 % num2

print("המחלק המשותף הגדול ביותר הוא:", num1)


# איבוד נתונים 8: מספר ראשוני

import math

num = int(input("הכנס מספר: "))

if num < 2:
    print("False")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break

    print(is_prime)


# לולאות מורכבות 1: טמפרטורה

temperatures = []
count = 0
previous_temp = None

while count < 12:
    try:
        temp = input(f"הכנס את הטמפרטורה הממוצעת לחודש {count + 1}: ")
        temp = float(temp)

        if temp == 0 and previous_temp == 0:
            print("זוהתה טעות - קלט חוזר, נסה שוב.")
            continue

        previous_temp = temp

        if temp < 5 or temp > 40:
            print("wrong data")
            break
        else:
            temperatures.append(temp)
            count += 1

    except ValueError:
        print("wrong data - אנא הכנס מספר תקין.")

else:
    print("correct data")
    average_temp = sum(temperatures) / len(temperatures)
    max_temp = max(temperatures)
    min_temp = min(temperatures)

    print(f"ממוצע הטמפרטורה השנתי הוא: {average_temp:.2f}")
    print(f"הטמפרטורה הגבוהה ביותר שנקלטה היא: {max_temp}")
    print(f"הטמפרטורה הנמוכה ביותר שנקלטה היא: {min_temp}")


# לולאות מורכבות 2: עצרת האו"ם

votes = []
in_favor_count = 0
against_count = 0
abstain_count = 0
veto_count = 0
first_in_favor = None
first_against = None

topic = input("הכנס את נושא ההצבעה: ")

for i in range(1, 45):
    try:
        vote = int(input(f"הצבעה של מדינה מספר {i} (1-בעד, 2-נגד, 3-נמנע, 4-וטו): "))

        if vote not in [1, 2, 3, 4]:
            print("הצבעה לא חוקית, אנא נסה שוב.")
            continue

        votes.append(vote)

        if vote == 1:
            in_favor_count += 1
            if first_in_favor is None:
                first_in_favor = i
        elif vote == 2:
            against_count += 1
            if first_against is None:
                first_against = i
        elif vote == 3:
            abstain_count += 1
        elif vote == 4:
            veto_count += 1
            print(f"הצבעה נפסקה - מדינה מספר {i} הצביעה וטו.")
            break

    except ValueError:
        print("קלט לא חוקי - יש להכניס מספר תקין (1-4).")

else:
    print("תוצאות ההצבעה:")
    print(f"בעד: {in_favor_count}")
    print(f"נגד: {against_count}")
    print(f"נמנע: {abstain_count}")
    print(f"וטו: {veto_count}")

    if first_in_favor is not None:
        print(f"המדינה הראשונה שהצביעה בעד היא מדינה מספר {first_in_favor}")
    else:
        print("לא היו הצבעות בעד")

    if first_against is not None:
        print(f"המדינה הראשונה שהצביעה נגד היא מדינה מספר {first_against}")
    else:
        print("לא היו הצבעות נגד")

