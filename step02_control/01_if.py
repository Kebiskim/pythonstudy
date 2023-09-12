import sys

s1 = int(input('수를 입력하세요 : '))


# if s1 == 0:
#     print('0은 나눗셈을 이용할 수 없습니다.')
#     sys.exit();
#
# # 파이썬에서 type 확인
# print(type(s1))
#
# print('3/', s1, '=', 3/s1)

# if ~ else로 쓰기
# if s1 == 0:
#     print('0은 나눗셈을 이용할 수 없습니다.')
# else:
#     print('3/', s1, '=', 3/s1)

# 다중 if
if s1 >= 90:
    print('90%');
elif s1 >= 80:
    print("빵점")
elif s1 >= 70:
    print("70점")
else:
    print("9점")