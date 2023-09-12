num = [10, 20, 30, 40, 50]
print(type(num))     # 해당 변수의 type 출력

num2 = (10, 20, 30, 40, 50)
print(type(num2))

for i in num:
    print(i)    # 자동으로 줄바꿈 처리

print('*' * 30)

for i in num:
    print(i, end = ' ')     # 자동으로 줄바꿈 안됨!! (띄어쓰기가 됨)

print()
print('*' * 30)

# 인덱스 값 이용 (num의 길이만큼, 마지막 값은 포함 X)
for i in range(0, num.__len__()):
    print(num[i], end= ' ')  # 자동으로 줄바꿈이 아니라 띄어쓰기가 됨
print()

# 역순으로 찍기
for i in range(0, num.__len__()-1, -1, -1):
    print(num[i], end= ' ')  # 자동으로 줄바꿈이 아니라 띄어쓰기가 됨
print()