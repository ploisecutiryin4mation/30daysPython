#conditional : điều kiện
#theo mặc định , các câu lệnh trong python sẽ thực thi từ tuần tự từ trên xuống , nếu logic xử lý yêu cầu như vậy, luồng thực thi tuần tự có thể thay đổi theo 2 cách
# cách 1 : thực thi có điều kiện , một khối gồm một hoặc nhiều câu lệnh sẽ được thực thi nếu một biểu thức nào đó là đúng 
# cách 2 : thực thi lặp lại : một khối gồm 1 hoặc nhiều câu lệnh sẽ đc lặp đi lặp lại miễn là 1 biểu thức là đúng . 

#if 
a = 3
if a > 0:
    print("A is a positive number")
# Trong ví dụ trên , 3 lớn hơn 0 , điều kiện đúng nên mã khối đã đc thực thi . tuy nhiên nếu dk sai chúng ta không thấy kqua , để thấy kết quả của đk sai , chúng ta phải có 1 khối khác , đó là else.
# if else
print("A is a positive number " if a > 0 else "A not is a positive number")
 
# if elif else
#Trong cuộc sống hằng ngày , chúng ta đưa ra quyết định hàng ngày . chúng ta đưa ra quyết định không phải bằng cách kiểm tra 1 hoặc hai điều kiện mà là nhiều điều kiện , tương tự như cuộc sống , lập trình cũng đầy rẫy các điều kiện . chúng ta sử dụng elif khi chúng ta có nhiều điều kiện
a = 0
if a > 0:
    print("a > 0")
elif a < 0:
    print('a is a negative number')
else:
    print('a = 0 ')
    
# Short hand : viet tat 

a = 3
print('a > 0 ' if a > 0 else 'a<=0')

#Nested conditions : Điều kiện lồng nhau
a = 0 
if a > 0:
    if a % 2 ==0:
        print("a is positive and even integer")
elif a < 0:
    
        print("A is negative and odd integer")
else:
    print("a is zero")
    
user = "Phuoc Loi"
password =  "1234"
if user == "Phuoc Loi" and password == "1234":
    print("tai khoan va mat khau dung")
else: 
    print("error")
    
