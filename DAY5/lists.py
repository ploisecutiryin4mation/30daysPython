#có 4 collection data types trong python
# List : là 1 tập hợp được xếp và cos thể thay đổi hoặc co thể đổi . cho phép các thành viên trùng lặp
#Tuple : là 1 tập hợp được sắp xếp và không thể thay đổi hoặc không thể sửa đổi . cho phép các thành viên trùng lặp
#Set : là 1 bộ sưu tập không có thứ tự , không lập chỉ mục và không thể sửa đổi , những chúng ta có thể thêm các mục mới vào tập hợp . Thành viên trùng lặp không được phép
#Dictionary : là 1 bộ sưu tập không có thứ tự , có thể thay đổi ( sửa đổi) và được lập chỉ mục , không có thành viên trùng lặp


#Tạo danh sách theo 2 cách
#cách 1 : sử dụng hàm list()
A = list()
print(len(A)) #output : 0

#cách 2 : sử dụng dấu ngoặc vuông [
empty_list = [] # this is an empty list, no item in the list
print(len(empty_list)) # 0

#vd rõ hơn
fruits = ['banana','apple','mango','lemon']
vegetables = ['tomato','Potato','Cabbage','Carrot']
laguage = ['python','Assembly','c++','c']
print(fruits)
print(vegetables)
print(laguage)

#danh sách cũng có thể là các kiểu dữ liệu khác nhau 
Number_string = ['Phuoc Loi',5,True,{'Bich mai' : 'Phuoc Loi'}]
print(Number_string)

#Truy cập danh sách bằng chỉ mục 
print(type(Number_string[0]))
print(type(Number_string[2]))
print(type(Number_string[3])) #dictionary
print(type(Number_string[-1])) #vi tri cuoi
print(type(Number_string[-2])) 

#Unpacking List Items
lst = ['Phuoc Loi','Bich Mai', 'Nguyen Thu','Tran Phuoc','AAAAA']
first_name,second_name,third_name,*four_name = lst
print(first_name)
print(second_name)
print(third_name)
print(four_name)

# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10


#cắt các mục từ list
fruits = ['banana', 'orange', 'mango', 'lemon']
all = fruits[0:4]
three = fruits[1:4]
# Or
negative = fruits[-1:]
orange_lemon = fruits[::2]
reverse_fruits = fruits[::-1]
test = fruits[::-2]
print(all)
print(three)
print(negative)
print(orange_lemon)
print(reverse_fruits)
print(test)
print("\n\n")

#sửa đổi list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'loi'
last_index = len(fruits)-1
print(fruits[0])
print(fruits[last_index])
print(fruits)

#them item vao cuoi list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append(1)
fruits.append(2)
print(fruits)

#them item vao list
# vd: A.insert(index,item)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(1,'1')
fruits.insert(3,2)
print(fruits)

#xoa cac item khoi list
# A.remove(item)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
fruits.remove('orange')
print(fruits)

#xoa item bang pop
#xóa mục đã chỉ định hoặc cuối ds nếu k dc chỉ định
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop(0)
fruits.pop()
print(fruits)

#xoa bằng del 
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]
del fruits[1:2]

#lenh nay se xoa all
#del fruits

#xóa các item trong danh sách
#clear làm trống danh sách
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)

#sao chép danh sách
#ta có thể coppy theo cách A = B , tuy nhiên nếu A thay đổi thi B cũng thay đổi vì vậy ta xài coppy()
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_coppy = fruits.copy()
print(fruits_coppy)

#tham gia danh sách ( nối các danh sách)
#có một số cách để nối
#sử dụng toán tử cộng
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
int_num = negative_numbers + zero +positive_numbers
#output -5 -4 ...

#Tham gia bằng phương thức Extend() Phương thức Extend() cho phép nối thêm danh sách vào một danh sách. Xem ví dụ dưới đây.
num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print(num1)

#đếm các muc trong list
num1 = [0, 1, 2, 3]
num2= [4,4,5,5, 5, 6]
print(num1.count('4'))
print(num2.count(4))


#tìm kiếm chỉ mục của item đó
num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
print(num1.index(1))
print(num2.index(4))



