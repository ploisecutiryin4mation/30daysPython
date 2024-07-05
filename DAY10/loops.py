#Cuộc sống toàn là những thói quen . Trong lập trình , ta cũng cần lặp đi lặp lại những hành động 

#có 2 loại vòng lặp trong python :
#while loop
#for loop

# WHILE :sử dụng để thực hiện 1 khối lệnh lặp đi lặp lại cho đến đi một điều kiện nhất định được thõa mãn . Khi điều kiện trở thành sai , các dòng mã sau vòng lặp sẽ đươc tiếp tục thực hiện
a = 5
while a > 0 :
    print("Phuoc Loi dep trai")
    a = a-1
print("vong lap ket thuc")

# BEARK and Continue 
# su dung break khi muon thoat khoi vong lap 
a =3
while a > 0:
    print(a)
    a -=1
    if a == 1:
        print("khi a  = 1 thi vong lap ket thuc ")
        break
#continue se khong thuc thi vòng lặp hiện tại mà nhảy sang vòng lặp tiếp theo
a = 5
while a > 0:
    a-=1
    if a ==3:
        print("khi a = 3 se nhay sang vong lap tiep theo")
        continue
    print(a)
    
# FOR LOOP
# từ khóa for được sử dụng để tạo vòng lặp for , sử dụng để lặp 1 chuỗi ( có thể là danh sách , bộ từ điển , tập hợp hoặc chuỗi)

# list loop
number = [0,1,2,3,4,5]
for i in number:
    print(i)
    
#string loop
pl = "Phuoc Loi"
for i in pl:
    print(i)


#tuple loop
tuple_ = (0,1,2,3,4,5)
for i in tuple_:
    print(i)
    
#dic loop : nó sẽ duyệt qua cho bạn key của từ điển đó 
person = {
    'fisrt name':"phuoc loi",
    'last name': "bich mai",
    'living': 'bac lieu',
    'user':'ploi',
    'password':'a',
    'skill':['html','python','java','c++'],
    'address': {
        "street":'space street',
        "zip code": "1234"
    }
}
for key in person:
    print(key)
print("\n")
for key,value in person.items():
    print(key,value)

print("\n")
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items())

#set loop
set_ = {"facebook","zalo",'twich',"tele"}
for i in set_:
    print(i)
    
#nhắc lại break , chúng ta muốn dừng nó trước khi vòng lặp hoàn tất
number = (1,2,3,4,5)
for i in number:
    print(i)
    if i == 3:
        break
print("\n")
numbers = (0,1,2,3,4,5)
for number in numbers:
    if number == 3:
        continue
        print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
    print(number)
print('outside the loop')
    
# RANGE() : hàm range để liệt kê các số . range(start,end,step) , theo mặc định start là 0 và step là 1 . range cần ít nhất 1 đối số là end

lst = list(range(11))
print(lst)

set_ = set(range(1,11,2))
print(set_)

for i in range(11):
    print(i)
    
#vong lap long nhau:
for i in range(5):
    for j in range(2):
        print(j)


person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == "skills":
        for skill in person["skills"]:
            print(skill)
    
# For else : khi muốn thông báo vòng lặp kết thúc chúng ta sử dụng else"
for i in range(10):
    print(i)
else:
    print("The loops stop at",i)
    
#pass :Câu lệnh này passđược sử dụng như một chỗ giữ chỗ cho mã trong tương lai.

# Khi passcâu lệnh được thực thi, không có gì xảy ra, nhưng bạn sẽ tránh được lỗi khi không cho phép mã rỗng.

# Không được phép sử dụng mã rỗng trong vòng lặp, định nghĩa hàm, định nghĩa lớp hoặc trong câu lệnh if.

for number in range(6):
    pass

