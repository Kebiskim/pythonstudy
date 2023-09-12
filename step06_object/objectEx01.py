'''
    클래스  안에는 상태값과 기능이 존재한다.
    상태값: 변수와 상수
    기능: 메서드
'''

class Person:
    name='홍길동'
    age = 24
    score = 176.8

    # 자바로 이야기하면 self는 this를 뜻함
    def setPerson(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    # 출력하는 함수
    # self는 this와 같은 효과!! 지우면 오류 난다! (자바에서 this 생략 가능한 것과 다름!)
    def viewPerson(self):
        print('이름 : ', self.name)
        print('나이 : ', self.age)
        print('점수 : ', self.score)

# 클래스를 객체로 만들어야 사용 가능
if __name__ == '__main__':
    ps = Person()
    # 객체 주소가 나옴!
    print(ps)
    print(ps.name, ',', ps.age, ',', ps.score)

    ps.setPerson('임꺽정', 39, 196.2)
    print(ps.name, ',', ps.age, ',', ps.score)

    ps.viewPerson()