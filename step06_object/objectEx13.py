# 예외처리
from builtins import Exception

# try:
#     # 오류가 발생할 수 있는 구문
# except Exception as e:
#     # 오류 발생 시 처리할 구문
# else:
#     # 오류 발생하지 않음
# finally:
#     # 무조건 마지막에 실행

try:
    4/0
except Exception as e:
    print(e)
    print(f'예외가 발생했습니다: {e}')
else:
    print("오류 발생 안함")
# finally:
#     print("무조건 마지막")