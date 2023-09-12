'''
    딕셔너리는 key와 value로 이루어져 있다.
    key는 불변하는 값만 넣을 수 있다.
    {} 형식으로 되어있다.
'''
d1 = {1:"Hello!!", 2:"bye"}
print(d1)
# 이렇게 쓰면 뒤에 있는 value만 불러옴
print(d1[1])
print(d1[2])

# 추가
print(d1);

d1['둘리'] = 24
d1['마이콜'] = 38
print(d1)

# 키는 중복이 안됨 (같은 키의 다른 값이 들어오면, 덮어쓴다!)
d1['num'] = [1,2,3]
print(d1)

# 키를 이용해서 삭제할 수 있다.
del d1['num']
print(d1)

# 키에 리스트는 사용할 수 없다. (tuple은 사용 가능!!)

d2 = {"name" : "홍길동", "hp" : "010-7979-7979", "age" : 24}
# keyList 만드는 함수 => keys()
res = d2.keys();
print(res)

for k in d2.keys():
    print(k)

# dict_keys를 list 변환할 수 있다
res2 = list(d2.keys())
print("res2 : " , res2)

# value를 list로 변환
res3 = d2.values();
print(res3)

# key와 value 한쌍을 얻기 (items())
res4 = d2.items()
print(res4)

# 삭제 : clear() => 모두 삭제
# d2.clear()
# print(d2)

# key를 이용해서 값을 얻어오기(get)
k1 = d2.get('age')
print(k1)

k2 = d2['age']
print(k2)

# 없는 키를 넣으면
k3 = d2.get('gender')
print(k3)

# 없는 key를 넣으면 오류 발생
# k4 = d2['gender']
# print(k4)

# 딕셔너리에서 해당 key가 존재하는지 알아보기
# d2에 age key가 존재하는지 물어본다
res5 = 'age' in d2
print(res5)

res6 = 'gender' in d2
print(res6)

# 파이썬에서 True, False는 무조건 첫글자가 대문자!

# 삭제 : clear() => 모두 삭제
# d2.clear()
# print(d2)

del d2["age"]
print(d2)

# res7 = d2.pop('name')
# name의 value만 삭제
print(d2)

# 항목의 갯수 구하기
res8 = len(d2)
print(res8)