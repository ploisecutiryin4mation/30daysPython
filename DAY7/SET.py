#Set là một tập hợp các vật phẩm. Hãy để tôi đưa bạn trở lại bài học Toán tiểu học hoặc trung học của bạn. Định nghĩa Toán học của một tập hợp cũng có thể được áp dụng bằng Python. Set là tập hợp các phần tử riêng biệt không có thứ tự và không được lập chỉ mục. Trong Python, tập hợp được sử dụng để lưu trữ các mục duy nhất và có thể tìm thấy tập hợp, giao điểm, hiệu, hiệu đối xứng, tập hợp con, siêu tập hợp và tập hợp rời rạc giữa các tập hợp.

#Khởi tạo set
#use the set() to build-in function

#tạo 1 set() rỗng
empty_set = set()
#tạo set với các giá trị được khởi tạo
set_init = {"ploi","bmai","hihi","hoho","hehe"}

print("set empty",empty_set)
print("init item in set",set_init)

#như list và tumple , sử dụng len() để tìm độ dài của set
lenght = len(set_init)

print("do dai cua set: ",lenght)

#truy cap set bang vong lap , se thay trong bai vong lap

#kiem tra item trong sett
checking_set = {"what","is","this"}
print("'what' in checking_set ","what" in checking_set)

#them item vao set
#khi set được tạo thì ta không thể thay đổi bất kì item nào mà chỉ có thể thêm vào
add_set = {"hehe","hihi","huhu"}
print("set truoc khi add item: ",add_set)
add_set.add("ploi")
print("set sau khi add item",add_set)

#update() cho phep add nhieu item vao set
add_set = {1,2,3,4}
print("set truoc khi update()",add_set)
add_set.update('5','6','7')
print("set sau khi update",add_set)

#removing items from a set
#neu remove sai item thi se xay ra loi , con su dung discard() se khong gay bat ki loi nao
remove_set = {'a','b','c','d'}
remove_set.remove('d')
print("sau khi remove",remove_set)

#su dung pop de random remove 
remove_set.pop()
print("sau khi pop",remove_set)

#CLEAR items in set
#if we want to clear or empty the set , we can use clear method
clear_set = {"a","b","c"}
clear_set.clear()
print("sau khi clear",clear_set)

#delte set
del_set = {"b","c","d"}
del del_set

#converting list to set
lst = [4,5,6,7,8]
list_to_set = set(lst)
print("sau khi convert",list_to_set)

#joining set
#use union() or update() to joining in set 
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print("sau khi joining",st3)

#update()
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1

#finding intersection items(tìm các mục giao nhau)
#itersection tra ve cac gia tri giong nhau
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
print("cac gia tri giao nhau",st1.intersection(st2))


# #tham khao con lai
# Checking Subset and Super Set
# A set can be a subset or super set of other sets:

# Subset: issubset()
# Super set: issuperset
# # syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item2', 'item3'}
# st2.issubset(st1) # True
# st1.issuperset(st2) # True
# Example:

# whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# even_numbers = {0, 2, 4, 6, 8, 10}
# whole_numbers.issubset(even_numbers) # False, because it is a super set
# whole_numbers.issuperset(even_numbers) # True

# python = {'p', 'y', 't', 'h', 'o','n'}
# dragon = {'d', 'r', 'a', 'g', 'o','n'}
# python.issubset(dragon)     # False
# Checking the Difference Between Two Sets
# It returns the difference between two sets.

# # syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item2', 'item3'}
# st2.difference(st1) # set()
# st1.difference(st2) # {'item1', 'item4'} => st1\st2
# Example:

# whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# even_numbers = {0, 2, 4, 6, 8, 10}
# whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

# python = {'p', 'y', 't', 'o','n'}
# dragon = {'d', 'r', 'a', 'g', 'o','n'}
# python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
# dragon.difference(python)     # {'d', 'r', 'a', 'g'}
# Finding Symmetric Difference Between Two Sets
# It returns the the symmetric difference between two sets. It means that it returns a set that contains all items from both sets, except items that are present in both sets, mathematically: (A\B) ∪ (B\A)

# # syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item2', 'item3'}
# # it means (A\B)∪(B\A)
# st2.symmetric_difference(st1) # {'item1', 'item4'}
# Example:

# whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# some_numbers = {1, 2, 3, 4, 5}
# whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

# python = {'p', 'y', 't', 'h', 'o','n'}
# dragon = {'d', 'r', 'a', 'g', 'o','n'}
# python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
# Joining Sets
# If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method.

# # syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item2', 'item3'}
# st2.isdisjoint(st1) # False
# Example:

# even_numbers = {0, 2, 4 ,6, 8}
# even_numbers = {1, 3, 5, 7, 9}
# even_numbers.isdisjoint(odd_numbers) # True, because no common item

# python = {'p', 'y', 't', 'h', 'o','n'}
# dragon = {'d', 'r', 'a', 'g', 'o','n'}
# python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}