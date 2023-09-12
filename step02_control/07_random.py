# 난수 함수
from random import *
# from random import *
# 아래처럼 import 하면 random.random() 처럼 써야 함
# import random

# 0.0 이상 1.0 미만의 임의의 실수
# while True:
    # print(random())

# 1.0 이상 3.0 미만
print(random)
print(uniform(1.0, 3.0))
# 1 이상 50 이하(포함)의 정수
print(randint(1, 2))
# random 범위 (7은 안나옴!!)
print(randrange(1, 7, 3))

# [] 안에 존재하는 하나 선택
print(choice([1,54,9,32,75,11]))