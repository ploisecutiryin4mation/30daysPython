#FUNCTION : Hàm là một khối mã hoặc câu lệnh lập trình có thể tái sử dụng được thiết kế để thực hiện một tác vụ nhất định. Để định nghĩa hoặc khai báo một hàm, Python cung cấp từ khóa def. Sau đây là cú pháp để xác định một hàm. Khối mã chức năng chỉ được thực thi nếu hàm đó được gọi hoặc được gọi

#Declaring and calling a function : Khai báo và gọi hàm
#Khi ta tạo 1 hàm , ta gọi nó là khai báo 1 hàm . chúng ta bắt đầu sử dụng nó , chúng ta bắt đầu sử dụng nó , hàm có thể được khai báo có hoặc không có tham số

#syntax
#declaring a function :
def sum_of_num():
    a = 3
    b = 4
    c = a + b
    print(c)
sum_of_num()

def generate_full_name():
    first_name = "Phuoc Loi"
    last_name = "Tran"
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name()


#FUNCTION returning a value 
def generate_full_name():
    fisrt_name = "Phuoc"
    last_name = "Loi"
    space = ' '
    full_name = fisrt_name + space + last_name
    return full_name
print(generate_full_name())


#Function with paremeters
#Trong một hàm , chúng ta có thể truyền các kiểu dữ liệu khác nhau (số, chuỗi, boolean, danh sách, bộ, từ điển hoặc tập hợp) làm tham số

def greetings(name):
    message = name + ',welcome to Python for everyone'
    return message
print(greetings("Loi"))


def add_ten(num):
    ten = 10
    return num+ten
print(add_ten(10))


#Two Parameter : Hai tham số: Một hàm có thể có hoặc không có tham số hoặc các tham số. Một hàm cũng có thể có hai hoặc nhiều tham số. Nếu hàm của chúng ta nhận tham số thì chúng ta nên gọi nó bằng các đối số. Chúng ta hãy kiểm tra một hàm có hai tham số:
def generating_name(first_name,last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print("full name: ",generating_name("Phuoc","Loi"))

#Passsing argument with Key and Value
#Nếu chúng ta truyền các đối số có khóa và giá trị thì thứ tự của các đối số không quan trọng.
def print_fullname(first_name,last_name):
    space = ' '
    full_name =  first_name + space + last_name
    return full_name
print("Key and value with function",print_fullname(last_name="Loi",first_name="Phuoc"))


#Function returning a value - part 2
#Nếu chúng ta không trả về một giá trị bằng một hàm thì hàm của chúng ta sẽ trả về None theo mặc định. Để trả về một giá trị bằng hàm, chúng ta sử dụng từ khóa return theo sau là biến chúng ta đang trả về. Chúng ta có thể trả về bất kỳ loại dữ liệu nào từ một hàm.
def sum(first_number,second_number):
    return first_number,second_number
print(sum(7,8))

#return a boolean
def check_is_even(n):
    if n % 2 == 0 :
        print("even")
        return True
    return False
print(check_is_even(8))

#Return a list
def find_even_numbers(n):
    evens = []
    for i in range(n+1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(11))


#Function with Default parameters:
#Đôi khi chúng ta chuyển các giá trị mặc định cho các tham số khi gọi hàm. Nếu chúng ta không truyền đối số khi gọi hàm thì giá trị mặc định của chúng sẽ được sử dụng.
def gretting_name(name = "Phuoc Loi"):
    return name
print("truyen theo mac dinh",gretting_name())
print("truyen theo gia tri khac",gretting_name("Bich Mai"))

#Arbitrary Number of Arguments : Số lượng đối số tùy ý
#Nếu không biết số lượng đối số truyền vào hàm, chúng ta có thể tạo một hàm có thể nhận số lượng đối số tùy ý bằng cách thêm * trước tên tham số.
def sum_numbers(*nums):
    total = 0 
    for i in nums:
        total += i
    return total
print("sum = ",sum_numbers(4,5,6))

#Default and Arbitrary Number of Parameters in Functions 

def generate_groups(team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups("Team - 1","Phuoc loi","Bich Mai","Mai","Loi"))


#Function as a Parameter of Another Function
#You can pass function around as parameters
def square_number(n):
    return n*n
def do_something(f,x):
    return f(x)
print(do_something(square_number,3))