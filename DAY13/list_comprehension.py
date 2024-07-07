#List Comprehension

# la 1 cách nhỏ gọn để tạo danh sách từ 1 chuỗi , nhanh hơn đáng kể nếu sử dụng for

# vd : neu muon change a string to a list char . can use a couple of methods . lets see:
#one way :
language = "Viet nam"
lst = list(language)
print(type(lst))
print(lst) #output : ['V','i',.....]

#second way:
lst = [i for i in language]
print(type(lst))
print(lst)

#create a list of numbers
numbers = [i for i in range(1,11)]
print(type(numbers))
print(numbers)

#it is possible to do mathematical operations during iteraction : có thể thực hiện phép toán trong quá trình lặp
#thay vi nhu the nay :
squares = []
for i in range(11):
    i = i*i
    squares.append(i)
print("vi du iteraction: ", squares)

#thi ta co the nhu the nay :
squares = [i * i for i in range(11)]
print("1 vi du khac ve interaction: ",squares)
squares = [i + 2 for i in range(11)]
print("1 vi du khac nua ve interaction: ",squares)


#it is also impossible to make a list of tuple
number = [(i,i+i)for i in range(11)]
print("list of tuple: ",number)



#list comprehension can be combined with if expression
# Generating even numbers
even_number = [i for i in range(30) if i % 2 == 0]
print("neu chia het cho 2 thi se them vao list ",even_number)

odd_num = [i for i in range(30) if i % 2 != 0 ]
print("neu khong chia het cho 2 ",odd_num)

# Filter numbers : let's filter out positive even num from the list below
numbers =  [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numer = [i for i in range (21) if i > 0 and i % 2 == 0]
print(positive_even_numer)

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]


#Lambda function 
#Để tạo hàm lambda, chúng ta sử dụng từ khóa lambda theo sau là (các) tham số, theo sau là một biểu thức. Xem cú pháp và ví dụ bên dưới. Hàm Lambda không sử dụng return nhưng nó trả về biểu thức một cách rõ ràng.
#syntax:
x = lambda param1,param2,param3: param1+param2+param3
print(x(1,2,3))

#example
#name function :
def add_two_nums(a,b):
    return a+b

print(add_two_nums(4,5))

#lambda
add_two_num_1 = lambda a,b:a+b
print(add_two_num_1(3,4))

#self invoking lambda function
print((lambda a,b:a+b)(2,3))

square = lambda x:x**2
print(square(3))

#mupltile variable
muptiple_var = lambda a, b,c: a ** 2 - 3 * b + 4 * c
print(muptiple_var(3,4,5))
    
    
#lambda function inside another function
def power(x):
    return lambda n: n*x
print("function in function",power(2)(3)) #function need to 2 arg to run , trong dau ngoac tron rieng biet
print(power(3)(4))
