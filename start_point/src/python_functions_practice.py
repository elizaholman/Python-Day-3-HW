def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def length_of_string(test_string):
    return len(test_string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
def number_to_full_month_name(number):
    return months[number-1]
#This function works for two tests

def number_to_short_month_name(number):
    return months[number-1][:3]

def volume_cube(side_1, side_2, side_3):
    return side_1 * side_2 * side_3

def reverse_string(string_1):
    return string_1[::-1]

def f_to_c(f):
    return (f-32)* 1.8