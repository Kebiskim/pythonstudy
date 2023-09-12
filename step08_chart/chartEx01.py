import matplotlib.pyplot as plt

# 모듈 : 함수들이 쫙 모여있는 것
# pip 하는 방법 => pycharm과 다르다. (파이참은 파이썬 중점으로 맞춰 만든 것)

names = ["Python", "Java", "Spring", "Flask"] # x축의 값
score = [155, 301, 125, 98] # y축의 값

plt.plot(names, score)
plt.show()