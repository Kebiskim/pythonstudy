# 컬렉션, 자료구조 => list, tuple, dictionary, set
#                   []     ()    {키: 값}    {}
# Set : 집합, 중복허용X, 순서유지X

myset = {1, 2, 3}
print(type(myset))

# 추가 (add)
myset.add(4.0)
myset.add("one")

print(myset)

# 존재 유무
if myset.__contains__(5):
    print("있다")
else:
    print('존재하지 않음')

# set 자료형에 저장된 값을 인덱싱으로 접근하려면 list나 tuple로 만들어야 한다.
# set을 list로 변경하는 코드
mylist = list(myset)
print(type(mylist))
print(mylist[0])

mytuple = tuple(myset)
print(type(mytuple))
print(mytuple[2])

print('*' * 50)
# 교집합, 합집합, 차집합을 구할 때 유용하다
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(type(s1), type(s2))

print()

# 교집합 : &
print(s1 & s2)
print(s1.intersection(s2))
# 위랑 같은 뜻
print(s2.intersection(s1))

# 합집합 : |
print(s1|s2)
print(s1.union(s2))
print(s2.union(s1))

# 차집합 : -
print(s1-s2)
print(s2-s1)
print(s1.difference(s2))
print(s2.difference(s1))

