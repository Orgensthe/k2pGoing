# Enter your code here. Read input from STDIN. Print output to STDOUT

dic = {}

t = int(input())
for idx in range(t):
    name, phone_number = input().split(' ')
    dic[name] = phone_number

for idx in range(t):
    name = input()
    if name in dic:
        print(name + '=' + dic[name])
    else:
        print('Not found')
