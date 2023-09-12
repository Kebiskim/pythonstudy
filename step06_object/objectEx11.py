def add(a,b):
    return a+b

def sub(a,b):
    return a-b

# 이렇게 하면 __main__ 이라고 찍고, 안의 내용 실행됨
print(__name__)

if __name__ == '__main__':
    print(add(1,4 ))
    print(sub(19,4 ))