'''
튜플 : 리스트와 비슷한 자료형
      리스트는 [], 튜플은 () 사용
      리스트는 요소의 값 변경(수정, 삭제, 생성 가능)
      튜플은 요소의 값 변경이 불가능

# 빈 값이 들어있는 형태
t1 = ()
t2 = (1,)
t3 = (10,20,30,40)
t4 = 10,20,30
t5 = ("국제시장", "스폰지밥", (10,20,30))
'''

t1 = ()
t2 = (1,)
t3 = (10,20,30,40)
t4 = 10,20,30
t5 = ("국제시장", "스폰지밥", (10,20,30))
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t5[0])
print(t5[-1])

t2 = ('a', 'b', 'c')

# 튜플의 연산(+, *)
print(t5+t2)
print(t2*3)

# 수정 안됨
# TypeError: 'tuple' object does not support item assignment
# t2[1] = 'k'

# 삭제 안됨
# del t2[1]

# 불린(참과 거짓)
# 문자열 : "aaa" => 참, "" => 거짓
# 리스트 : [1,2,3] => 참, [] => 거짓
# 튜필 : (1,2,3) => 참, () => 거짓
# dictionary : {1,2,3} => 참, {} => 거짓
# 숫자 : 1(참), 0(거짓)
# None : 거짓