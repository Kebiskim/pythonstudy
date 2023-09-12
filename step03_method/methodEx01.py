'''
    def 함수명(인자):
'''

def view():            # 함수 정의
    print('hello')
    return

def view2():            # 함수 정의
    print('hello')
    # return    => return은 생략 가능!

def view3():            # 함수 정의
    return 10

def view4():            # 함수 정의
    return 'Hi~~~'


# 메인함수 : 프로그램의 엔트리 포인트
# __main__ => 자바의 main 메서드와 같음!! (얘부터 실행한다!!)
if __name__ == '__main__':
    view()  # 함수 호출
    view2()
    # 리턴값 그냥 받기
    print(view3())
    str = view4()
    print(str)

# 메인이 있을 때만 함수를 호출하는 것은 아니며, 메인 없어도 실행은 가능!