
name = input('Enter name: ')
age = input('Enter age: ')

print('Hello, my name is ' + name + ' and I am ' + str(age))

print('My name is {name} and I am {age}'.format(name=name, age=age))

print(f"Hello {name}, you are {age} years old")

number = [1, 2, 3, 4, 5]

numbers2 = list((1, 2, 3, 4, 5))

print(number, numbers2)
