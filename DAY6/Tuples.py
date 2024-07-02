#Tuple là tập hợp các kiểu dữ liệu khác nhau được sắp xếp theo thứ tự và không thể thay đổi (không thay đổi). Các bộ dữ liệu được viết bằng dấu ngoặc tròn, (). Khi một bộ dữ liệu được tạo, chúng ta không thể thay đổi giá trị của nó. Chúng ta không thể sử dụng các phương thức thêm, chèn, xóa trong Tuple vì nó không thể sửa đổi (có thể thay đổi). Không giống như danh sách, tuple có ít phương thức. Các phương thức liên quan đến bộ dữ liệu:

# khởi tạo tuple

#empty tuple : tạo 1 tuple rỗng
#cú pháp
emty_tuple = ()
#sử dụng hàm tuple()
empty_tuple = tuple()

print("empty duoc tao boi cu phap ",emty_tuple)
print("empty duoc tao boi ham empty()",empty_tuple)

print("######################\n\n")

#Khởi tạo giá trị tuple()
tuple_ = ("loi","mai","phuoc",'abc','xyz','blabla')
lenght = len(tuple_)
print("do dai cua tuple ",lenght)
print("gia tri trong tuple ",tuple_)

#Truy cập tuple
#truy cập bằng index

print(tuple[0])
print(tuple[-1])
last_index = len(tuple_)-1
print("gia tri cuoi cung cua tuple ",tuple_[last_index])

#Cắt tuple
#cắt giống với list
print("gia tri cua tuple o vi tri index 0 va khong bao gom 1",tuple_[0:1])
print("gia tri cua tuple o index 1 va 2",tuple_[1:3])

print("dao nguoc tuple",[tuple_[::-1]])


#Chuyển Tuple thành list 
Tuple_to_list = list(tuple_)
print("sau khi chuyen tuple thanh list",Tuple_to_list)

#chuyen list thanh tuple
List_to_Tuple = tuple(Tuple_to_list)

if "phuoc" in List_to_Tuple:
    print("'phuoc' o trong  ",List_to_Tuple)


#Nối Tuple()
tuple2 = ("abc",5,6)

tuple3 = ("xyz",8,9)

sum_tuple = tuple2+tuple3
print("sau khi noi 2 tuple voi nhau",sum_tuple)

#xoa tuple 
del tuple2
del tuple3
print("tuple sau khi xoa",tuple2)






