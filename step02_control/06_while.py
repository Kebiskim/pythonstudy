# 1. 사각형 2. 삼각형 3. 원 4. 종료
# 선택하세요 : 1
# 사각형을 선택하셨습니다.
#
# 4를 선택하면 프로그램 종료
import sys

# while 문은 무한루프
while True:
    n = int(input('1. 사각형 2. 삼각형 3. 원 4. 종료\n 선택하쇼 :'))
    
    if n == 1:
        print('사각형 선택')
    elif n == 2:
        print('삼각형 선택')
    elif n == 3:
        print('원 선택')
    elif n == 4:
        print('종료')
        sys.exit();
    else:
        print('잘못 입력')
