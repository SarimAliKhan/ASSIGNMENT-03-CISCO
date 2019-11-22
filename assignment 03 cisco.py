#QS 01
operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
** for power
''')

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

elif operation == '**':
    print('{} ** {} = '.format(number_1, number_2))
    print(number_1 ** number_2)
else:
    print('You have not typed a valid operator, please run the program again.')

#QS 2
num = []
for i in range(10000):
    num.append(i)
list = [1,'s',22,3,'a']
for i in list:
    if i in num:
        print('numeric value : ',i)

#QS 3
dic = {'c': 'cycle','b': 'bat'}
print(dic)
dic['a'] = 'apple'
print(dic)

#QS 4
num = []
for i in range(10000):
    num.append(i)
s = 0
list = {1:'jon','j':5,6:0}
for i,j in list.items():
    if i in num:
        s += i
    elif j in num:
        s += j

print(s)

#QS 5
l = [1,23,23,100,4,67,100]
leng = len(l)
rep = []
for i in range(leng):
    for j in range(i+1,leng):
        if l[i] == l[j] and l[i] not in rep:
            rep.append(l[i])
print(rep)

#QS 6
keyy = {'sarim':1,'ammar' : 2}
inp = input('key :')
if inp in keyy.keys():
    print('Present')
else:
    print('Not present')
