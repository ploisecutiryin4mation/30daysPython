#string
#có nhiều phương thức chuỗi và hàm tích hợp khác nhau để xử lý kiểu dữ liệu

#vd : kiểm tra độ dài chuỗi 
print(len("Phuoc Loi dep trai"))

#tạo chuỗi nhiều dòng ( tạo bằng cách sử dụng ba dấu nháy đơn hoặc 3 dấu nháy kép)
#vd : 
Multiline_string =  """beautiful day yeah yeah yeah 1 2 3 4.
12312312321233222222222222222.
32222222222222222222222222132.
dsdsaddddddddddddddddddddddds.
dsaaaaaaaaaaaaaaaaaaaaaaaaads.
"""
print(Multiline_string)
#vd2 :
Multiline_string_2 = '''312312121213233223312313113
31131313323123321132
32123233333333323212
322222222222222222221
'''
print("This is Multiline_string 2 :",Multiline_string_2)


#định dạng chuỗi 
#dùng toán tử %
# %s - Chuỗi (hoặc bất kỳ đối tượng nào có biểu diễn chuỗi, như số)
# %d - Số nguyên
# %f - Số dấu phẩy động
# "%.number of digitsf" - Số dấu phẩy động có độ chính xác cố định

#vd : chỉ mỗi chuỗi
leesin = "yasuo"
stack_ov = "rsp"
got = "PLT"
format_string = "hom nay la mot ngay thich hop de %s %s %s" %(leesin,stack_ov,got)
print(format_string)

#vd : string and numbers
pi = 3.14
pl = 5 
bm = 10
formated_string = "hom nay la thu may %d %d %.3f" %(pl,bm,pi)
print(formated_string)

#định dạng chuỗi kiểu mới 
#vd
first_name = "Phuoc Loi"
last_name = "Bich Mai"
laguage =  "python"
format_stringg = 'I am {} {}.I know {}'.format(first_name,last_name,laguage)
print(format_stringg)

#vd khác :
a =  3
b=4
print("{} + {} = {}".format(a,b,a+b))
print("{} - {} = {}".format(a,b,a-b))


#1 cách khác ( python 3.6+)
a = 4 
b = 5
print(f'{a} + {b} = {a+b}')

#truy cập chỉ mục của chuỗi
#vd : 
a = "Python"
print(a[0])
print(a[1])
print(a[2])
#or
print(a[-1])
print(a[-2])
print(a[-3])

#cắt chuỗi
#vd :
A = "Python Laguage"
first_three = A[:3] #cat tu dau den vi tri 3 nhung khong bao gom 3
print(first_three)

last_three = A[3:] #cat tu vi tri thu 3 den cuoi
print(last_three)

#dao nguoc chuoi
print(A[::-1])

#bo qua index trong khi cat 
print(A[:14:3])

#các hàm phổ biến trong Python
#Capitalize() chuyển kí tự đàua tiên của chuỗi thành chữ in hoa
A = "phuoc loi dep trai"
print(A.capitalize())

# count() trả về số lần xuất hiện của chuỗi con trong chuỗi , count(substring,start=,end=)
A = 'loi dep loi trai loi phuoc'
print(A.count('loi',0,12))

#split() tách chuỗi , sử dụng chuỗi hoặc dấu cách đã cho làm dấu phân tách 
A = "Phuoc Loi dep trai"
print(A.split())
A = "Phuoc$Loi$Dep$Trai"
print(A.split("$"))

#Strip()xóa tất cả các kí tự đã cho bắt đầu từ đầu chuỗi và cuối chuỗi
A = 'Python is dza best  '
print(A.strip("Piz"))

#Join() Trả về một chuỗi được nối
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

#title() trả về những chữ cái đầu được viết hoa
Loi = "phuoc loi dep trai"
print(Loi.title())

#replace(): Thay thế chuỗi con bằng một chuỗi đã cho
Loi = " Bich mai dep gai"
print(Loi.replace('Bich mai','loi'))


