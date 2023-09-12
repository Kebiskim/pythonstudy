class Calc:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self, first, second):
        result = first + second
        return result

    def sub(self, first, second):
        result = first - second
        return result

    def div(self, first, second):
        result = first / second
        return result
    
# 상속(Calc 클래스는 부모클래스가 된다.)
class MoreCalc(Calc):
    # 이렇게 하면 겹쳐버려서 오류
    def __init__(self):
        print("자식 객체 생성")

    # 오버라이딩 : 부모메서드를 가져와서 자기에 맞게 변경 (자식이 우선순위가 높음)

    def div(self, first, second):
        if second == 0:
            return "0으로 나눌 수 없습니다."
        else:
            result = first / second
            return result

# 자식은 부모의 것을 마음대로 사용할 수 있다.
# MoreCalc가 자식임.
a = MoreCalc()
# 자식을 호출했지만 부모 것을 가져다 쓰는 것
# print(a.add())
# a => self, 7 => first, 3 => second
b = a.add(7, 3)
print(b)

c = a.sub(7, 3)
print(c)

# 함수 선언에서 self. 붙인 거 지워야 됨. 그래야 아래 오류 안남.
d = a.div(7,0)
print(d)