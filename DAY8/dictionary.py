#Dictionary is a collection , không có thứ tự , có thể thay đổi , kiểu dữ liệu ghép nối (key:value)

#Tạo dictionaries
#syntax :
empty_dic = {}

dic = {'a':'loi','b':'phuoc'}
#example
person = {
    'first name':'Loi',
    'last name': 'phuoc',
    'age': 15,
    'living': 'bac lieu',
    'skill':['java','python','c++'],
    'address': {
        'street':'space street',
        'zip code': '02210'
    }
}
#the dictionary above shows that a value could be any data types:string , boolean , list ,tuple,set

#kiem tra do dai cua dic
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct))
#Việc truy cập một mục theo tên khóa sẽ gây ra lỗi nếu khóa không tồn tại. Để tránh lỗi này trước tiên chúng ta phải kiểm tra xem khóa có tồn tại hay không hoặc chúng ta có thể sử dụng phương thức get. Phương thức get trả về Không, là kiểu dữ liệu đối tượng NoneType, nếu khóa không tồn tại.
person1 = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person1.get('first_name'))
print(person1.get('address'))

#add item to a dictionary
#chung ta co the them new key and value vao dic
#syntax :
pl = {'a':1,
      "b":2,
      'vai':['java','python','c++'],
      'c':3,
      'd':4
}
pl['e']=5
print(pl)
#use append neu value la list
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
}
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)


#modifying item in a dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 5
print(dct)


#checking keys in a dictionary
# use in operator to check if a key in a dictionary

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('true' if 'key1' in dct else 'false')
print('true' if 'key2' in dct else 'false')

#removing key and value pairs from a dictionary
# pop(key): removes the item with the specified key name:
# popitem(): removes the last item
# del: removes an item with specified key name

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print("truoc khi dung pop",dct)
dct.pop('key1')
print("sau khi pop",dct)
dct.popitem()
print("sau khi use popitem()",dct)
del dct['key2']
print("sau khi del",dct)


#Changing dic to a list of item
#use items() changes dic to a list of tuples
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items())


#clearing a dictionary
#if we don't want the items in a dic we can clear them using clear() method
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) #none

#deleting a dic
#if we don't use the dic we can del it completely
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct





