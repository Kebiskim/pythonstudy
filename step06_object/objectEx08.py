import objectEx07

# 객체를 새로 만들면 무조건 __init__ 메서드가 실행된다!
b = objectEx07.Book()
b.setData('올림픽의 영웅', '5000', '김상우')
b.printData()

c = objectEx07.Book()
c.setData('양궁의 정석', '12500', '양궁협회')
c.printData()