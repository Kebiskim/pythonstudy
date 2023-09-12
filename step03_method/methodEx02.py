def show1(a, b, c, d):
    print(a, b, c, d)

def show2(k, e, m):
    avg = (k+e+m)/3
    print('평균 : %.2f' %avg)
    if avg >= 60:
        return '합격'
    else:
        return '불합격'

def show3(avg):
    avg = int(avg/10)
    return{
        10:'A',
        9:'A',
        8:'B',
        7:'C'
    # .get => else 역할을 함.
    # get 메서드는 딕셔너리에서 주어진 키(avg의 값)에 대응하는 값을 반환하며,
    # 딕셔너리에 해당 키가 없을 경우 뒤에 제공된 기본 값인 'F'를 반환합니다.
    }.get(avg, 'F')

show1(10, 'A', 100.4, True)

res = show2(90, 80, 60)
print('결과 : ', res)

res2 = show3(55.42)
print(res2)