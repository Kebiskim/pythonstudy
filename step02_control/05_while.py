'''
  조건식이 참일 동안 실행문장 반복 수행
    while 조건식:
        실행문장
        [탈출조건]
'''

# n = 10
# while n>0:
#     print(n)
#     n = n-1

# 단을 입력받아서 해당 단을 1~9까지 계산한 결과를 출력하시오.
su1 = int(input('단을 입력하세요'));
row = 1;
result = 0;
while row < 10:
    result = su1 * row
    print(f'{su1} * {row} = {result}')
    row += 1;