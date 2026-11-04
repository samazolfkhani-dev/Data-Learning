# int
age = 20
print(int('32'))
print(abs(-67))
print(round(2.356))


# float 
price = 12.34
float('345.9')
print(round(44.90))
print(abs(-90.67))


# str
string = "Hello World"
print(string.upper())
print(string.lower())
print(string.capitalize())
print(string.title())
print(string.find('e'))
print(string.index('W'))
print(string.count('o'))
print(string.startswith('Hallo'))
print(string.endswith('old'))
print(string.isdigit())
print(string.isalnum())
print(string.isalpha())
print(string.split())

# list
l1=[10 , 20 , True , False , 'Hello']
print(l1)
print(l1[0:])
print(l1[1:4])
l1.append(99)
l1.extend(['World' , 'Sama'])
l1.insert(0 , 5)
print(l1)
print(l1.remove(99))
print(l1)

# set
s1 = {1 , 2, 3 , 4 , 5 , 6 , 7 , 8}
print(s1)
s1.add(99)
s1.remove(1)
s1.discard(40)
s1.update({30 , 33 , 34})
print(s1.pop())

# dict
d1 = {'name' : 'Sama' , 'age' : 20}
print(d1.get('name'))
print(d1['age'])
d1['nickname'] = 'no'
print(d1)

print(3 in s1)