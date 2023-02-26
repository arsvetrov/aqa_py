"""
    Написати функцію, яка обчислює суму двох чисел.
    Написати функцію, яка перевіряє, чи є задане число простим.
    Написати функцію, яка розраховує середнє арифметичне список чисел.
    Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
    Написати функцію, яка перевіряє, чи є заданий рядок паліндромом.
    Написати функцію, яка приймає список і повертає його, відсортований в порядку зростання.
    Написати функцію, яка знаходить найбільший спільний дільник двох чисел.
    Написати функцію, яка приймає список чисел та повертає кількість від'ємних чисел у списку.
    Написати функцію, яка приймає список рядків та повертає найдовший рядок у списку.
    Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
    у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
    не є підрядком першого рядка.
"""
# def multiplication_table(number):
#     # Initialize the appropriate variable
#     multiplier = 1

#     # Complete the while loop condition.
#     while multiplier <= number:
#         result = number * multiplier
#         if  result > 25 :
#             # Enter the action to take if the result is greater than 25
#             break
#         print(str(number) + "x" + str(multiplier) + "=" + str(result))

#         # Increment the appropriate variable
#         multiplier += 1


# multiplication_table(3)
# # Should print:
# # 3x1=3
# # 3x2=6
# # 3x3=9
# # 3x4=12
# # 3x5=15

# multiplication_table(5)


import os
import csv

# Create a file with data in it
def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type")
        file.write("carnation,pink,annual")
        file.write("daffodil,yellow,perennial")
        file.write("iris,blue,perennial")
        file.write("poinsettia,red,perennial")
        file.write("sunflower,yellow,annual")

# Read the file contents and format the information about each row
def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open the file
    with open(filename) as f:
        # Read the rows of the file
        rows = f.readlines()
        # Process each row
        for row in rows[1:]:
            print(row)
            a,b,c = row.split(",")
            print(a,b,c)
            # Format the return string for data rows only
            return_string += "a {0} {1} is {2}\n".format(b,a,c)
    return return_string

#Call the function
print(contents_of_file("flowers.csv"))