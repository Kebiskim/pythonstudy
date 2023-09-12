from step04_dictionary.dictionary01 import dic

dict_emp = {'name':'뽀로로', 'phone':'010-1234-3241', 'addr':'강남구'}

print(dict_emp)

# 딕셔너리를 list로 바꿔보자 (keys : 키 리스트 만들기)
key = dict_emp.keys()
print(key)
print(type(key))

# keys를 활용한 출력
for i in dict_emp.keys():
    print(i)

# keys를 활용한 리스트 만들기
# 생성자를 뜻하는 것
key2 = list(dict_emp.keys())
print(key2)
print(type(key2))

# values()를 활용
value = dict_emp.values()
print(value)
print(type(value))

for i in dict_emp.values():
    print(i)

# 키를 이용한 value값 얻기
print('get() 이용 : ', dict_emp.get('name'))
print('[키값] 이용 : ', dict_emp['phone'])

# 해당 key가 딕셔너리에 있는지 조사 (in)
print('name' in dict_emp) # name이라는 key가 있으면, True 반환
print('age' in dict_emp) # age라는 key가 없어서, False 반환!!

# clear() : key, value 모두 지워버리기
dict_emp.clear()
print(dict_emp)

mydict = {'홍길동':20, '일지매':25, '임꺽정':31, '장길산': 38}
for i in mydict.items():
    print(i)

for i in mydict:
    print(i, end=' ')
    print(mydict[i], end=' ')
    print()

# 나이가 30 이상
for i in mydict:
    if mydict[i] >= 30:
        print(i, mydict[i])

print()
print('*' * 30)
print()

for name, age in mydict.items():
    if age == 31:
        print(name)
print('*' * 30)
# 딕셔너리 컴프리헨션
[print(name) for name, age in mydict.items() if age != 31]