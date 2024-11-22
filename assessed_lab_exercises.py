def calculator(num1, num2, operator):
    result = "No Result"
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num1 and num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
    elif operator == "%":
        result = num1 % num2
    elif operator == ">":
        if num1 > num2:
            result = True
        else:
            result = False
    elif operator == ">=":
        if num1 >= num2:
            result = True
        else:
            result = False
    elif operator == "<":
        if num1 < num2:
            result = True
        else:
            result = False
    elif operator == "<=":
        if num1 <= num2:
            result = True
        else:
            result = False
    else:
        print("Invalid operator")
    return result

def max_of_three(num1, num2, num3):
    maximum = max(num1,num2,num3)
    return maximum

def winning_numbers(user_list, winning_list):
    list_content = -1
    amount_correct = 0
    list_contents = len(winning_list) - 1
    while list_content < list_contents:
        list_content += 1
        if user_list[list_content] in winning_list:
            amount_correct +=1


    if amount_correct == 3:
        result = "First"
    elif amount_correct == 2:
        result = "Second"
    elif amount_correct == 1:
        result = "Third"
    else:
        result = "Nothing"
    return result

def sum_of_evens(min_value, max_value):
    total = 0

    for i in range(min_value,max_value):
        if (i < min_value):
            continue
        if (i % 2 == 0):
            total += i
    return total

def are_anagrams(str1, str2):
    counter = 0
    for a in range(len(str1)):
        for b in range(len(str2)):
            if str1[a] == str2[b]:
                counter += 1

    if counter == len(str1):
        output = True
    else:
        output = False
    return output

def is_prime(num):
    num = int()
    if num <= 1:
        output = False
    else:
        if num % 2 or 0 == 0:
            output = True
        else:
            output = False
    return output

def calculate_average(numbers):
    sum = 0
    list_amount = -1
    average = 0
    list_contents = len(numbers) - 1
    division_number = len(numbers)

    while list_amount < list_contents:
        sum += (numbers[list_amount])
        list_amount += 1
        if list_amount == list_contents:
            average = sum / division_number
    return average

def calculate_weekly_pay(hours_worked):
    regular_rate = 12  # £12 per hour for up to 35 hours
    overtime_rate = 18  # £18 per hour for hours worked beyond 35 hours
    
    standard_hours = 35  # Threshold for regular pay
    overtime = 0

    total_pay = 0
    over_pay = 0

    if hours_worked < standard_hours:
        total_pay = hours_worked * regular_rate
    elif hours_worked > standard_hours: 
        total_pay = standard_hours * regular_rate
        overtime = hours_worked - standard_hours    
        total_pay += overtime * overtime_rate
    return total_pay

def celsius_to_fahrenheit(celsius):
    output = (celsius * 9)/5 + 32
    return output

def annual_net_income(gross_salary):
    if gross_salary >= 45000:
        net_salary = gross_salary * 0.5
    elif 30000 <= gross_salary and gross_salary < 45000:
        net_salary = gross_salary * 0.7
    elif gross_salary < 30000:
        net_salary = gross_salary * 0.85

    return net_salary

def letter_occurrence(input_string):
    # complete function implementation...

    count = 0
    for i in range(len(input_string)):
        if input_string[i] == "A" or input_string[i] == "a":
            count += 1
    return count

def km_to_miles(kilometers):
    # complete function implementation here...
    mile = 0.62
    miles = kilometers * mile
    return miles

def fuel_cost(distance_miles):

    MPG = 50
    LITERS_PER_GALLON = 4.5
    PRICE_PER_LITER = 1.49

    distance_travelled = (distance_miles / MPG)
    total_cost = (LITERS_PER_GALLON * PRICE_PER_LITER)
    

    return total_cost

def decrypt_cypher_text(encrypted_text, key):
    decrypted_text = ""
    for i in range(len(encrypted_text)):
        character = ord(encrypted_text[i])
        subtraction_number = character - key
        divided_number = subtraction_number % 256
        decrypted_text += chr(divided_number)
    return decrypted_text

def find_maximum_difference(a, b):
#     # code implementation here...
     maximum_a = max(a)
     minimum_a = min(a)
     maximum_b = max(b)
     minimum_b = min(b)

     if maximum_a > maximum_b:
        maximum = maximum_a - minimum_b
     else:
        maximum = maximum_b - minimum_a
     return maximum

def is_golden_number(n):
#     # function implementation ...
    loop_end = n-1
    a = 1

    while a < loop_end:
        a += 1
        if (a+(n-a)==n):
            if ((a*(n-a))%1000==0):
                return True
    return False    