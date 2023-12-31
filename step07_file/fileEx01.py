'''
* 파일 처리
파일객체 = open(파일이름, 모드)
-- 모드 : 'r' : 읽기모드
         'w' : 쓰기모드 (파일이 존재하는 경우, 원래 내용이 지워지고 열린다.) * 파일이 없는 경우 생성해줌
         'a' : 추가모드
'''

# fp = open("test01.txt" ,'w')
# for i in range(1, 5):
#     content = "%d 번째 줄...\n" %i
#     fp.write(content)
#
# fp.close()

# fp = open("test01.txt" ,'r')
# while True:
#     data = fp.readline()    # 한줄 읽기
#     if not data:
#         break;
#     print(data, end = '')
# fp.close()

# fp = open("test01.txt" ,'r')
# # 모든 정보가 리스트에 담아서 나옴
# datas = fp.readlines()
# print(datas)
# for i in datas:
#     print(i, end="")
# fp.close()

# fp = open("test01.txt", 'r')
# # read()함수는, for문 없이 파일 전체내용을 문자열로 return 한다.
# data = fp.read()
# print(data)

# a 모드를 이용해서 기존 파일에 내용 추가하기
# a는 append의 약자!
# a는 append (뒤에 내용 붙임), w는 write(전체 내용 삭제 후 덮어씀)
fp = open("test01.txt", 'a')
for i in range(5, 8):
    data = "%d 번째 줄...\n" %i
    fp.write(data)
# 반드시 마지막에 close는 해주자
fp.close()

fp = open("test01.txt", 'r')
data = fp.read()
print(data)

print("=" * 30)

# with문을 이용해서 파일 객체 다루기 : close를 할 필요가 없다.
with open("test02.txt", 'w') as f:
    f.write('with문을 이용해서 파일 쓰기 테스트')