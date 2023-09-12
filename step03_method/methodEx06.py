# 1차원배열
car = ['소나타', '그랜저', '스파크', '모닝', 'EV9']
print(car)

car[3] = '팰리'
print(car)

car.append('팰리2')
print(car)

# 이런 식으로 문자열 하나를 하나의 배열로 보고, 또 배열처럼 꺼내쓸 수 있음(substring 처럼)
print(car[0][0]) # 문자열을 배열 취급 가능