#Function as a parameter
def sum_number(nums):
    return sum(nums)


def higher_order_function(f,lst):
    sumation = f(lst)
    return sumation
result = higher_order_function(sum_number, [1,2,3,4,5])
print("ham goi 1 ham khac va 1 list: ",result)

#Function as a return value : function như giá trị trả về

def square(x):
    return x ** 2

def cube(x):
    return x **3

def absolute(x):
    if x >= 0 :
        return x
    else:
        return -(x)
    
def higher_order_function(type):
    if type == 'square':
        return square
    elif type == "cube":
        return cube
    elif type == "absolute":
        return absolute

result = higher_order_function('square')
print("ham nay can duoc goi",result(3))


result = higher_order_function('cube')
print("ham nay can duoc goi",result(5))

result = higher_order_function("absolute")
print("ham nay can duoc goi",result(-7))

#Python closures : Python cho phép một hàm lồng nhau truy cập vào phạm vi bên ngoài của hàm bao quanh. Điều này được gọi là Closure. Chúng ta hãy xem cách thức hoạt động của closure trong Python. Trong Python, closure được tạo ra bằng cách lồng một hàm vào bên trong một hàm bao quanh khác và sau đó trả về hàm bên trong. Xem ví dụ bên dưới.
def add_ten():
    ten = 10
    def add(num):
        return num+ten
    return add
closure_result = add_ten()
print(closure_result(5))
print(closure_result(15))

#Python Decorators : Decorator là một mẫu thiết kế trong Python cho phép người dùng thêm chức năng mới vào một đối tượng hiện có mà không cần sửa đổi cấu trúc của nó. Decorator thường được gọi trước khi định nghĩa hàm mà bạn muốn trang trí.
# Normal function
def greeting():
    return "welcome to my python"
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())

#
## Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to python'
print(greeting())

#Accepting Parameters in Decorator Functions
#Most of the time we need our functions to take parameters, so we might need to define a decorator that accepts parameters.

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')

#Built-in Higher Order Functions
#Một số hàm bậc cao được tích hợp sẵn mà chúng tôi đề cập trong phần này là map(), filter và less. Hàm Lambda có thể được truyền dưới dạng tham số và trường hợp sử dụng tốt nhất của hàm lambda là trong các hàm như bản đồ, bộ lọc và thu nhỏ.

#Python-map function

#Hàm map() là một hàm tích hợp có một hàm và có thể lặp lại làm tham số.

number = [1,2,3,4,5]
def square(x):
    return x ** 2
number_squared = map(square,number)

print(list(number_squared))

numbers_squared = map(lambda x: x **2,number)
print(list(numbers_squared))

#example 2 
lst = ['1','2','3','4','5']
float_map = map(float,lst)
print(list(float_map))

#example 3
names = ["ploi","hehe","hihi","haha"]

def change_to_upper(name):
    return name.upper()

names_upper_case = map(change_to_upper,names)
print(list(names_upper_case))

#PYTHON - Filter Function
#Hàm filter() gọi hàm đã chỉ định và trả về boolean cho từng mục của (danh sách) có thể lặp được chỉ định. Nó lọc các mục thỏa mãn tiêu chí lọc.

#example 1
# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]

#Example:2

numbers = [1, 2, 3, 4, 5]  # iterable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]
# Filter long name
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']


#PYTHON - Reduce Function
#Hàm less () được xác định trong mô-đun functools và chúng ta nên nhập nó từ mô-đun này. Giống như bản đồ và bộ lọc, nó có hai tham số, một hàm và một lần lặp. Tuy nhiên, nó không trả về một lần lặp khác, thay vào đó nó trả về một giá trị duy nhất. Ví dụ 1

numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15

        



