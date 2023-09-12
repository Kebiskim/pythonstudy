class Book:
    # 초기화 메서드 : 생성자, 객체가 생성될 때 무조건 자동으로 실행(호출)
    def __init__(self):
        print("책 객체를 새로 생성한다!")

    # 여기서 self는 => b를 뜻한다 (Ex08에서의)
    # 전역변수 안쓰고 지역변수 써도 꺼내 쓸 수 있게 되는 것!
    def setData(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author
        
    def printData(self):
        print('제목 하이')
        print(self.title)
        print(self.price)
        print(self.author)