#Operators ( toán tử )
#Arithmetic operators ( toán tử số học)
# ngoài ra python còn sử dụng ( is , is not , in , not in)
print('1 is 1',1 is 1)
print('1 is not 2',1 is not 2)
print('A in ABCDFJJJ','A' in 'ABCDFJJJJ')
print('H not in ABCDFJJJ','H' not in 'ABCDFJJJJ')


#tricks operators:
#thay vì code như thế này :
age = 12
if age >= 18:
    adult = True
else:
    adult = False
if adult:
    print("You are an Andult")
else:
    print("you are not an adult")

#ta có thể code như này
age = 12 
adult = True if age >= 18 else False

if adult:
    print("You are an adult")
else:
    print("you are not an adult") 
#và còn có thể rút ngắn hơn nữa 
age = 12 
adult = True if age >= 18 else False
print("you are an adult " if adult else "You are not an adult")
#tương tự với các toán tử so sánh 
number = 121312
print("this number is very large" if number > 1000000 else "this number is quite large")