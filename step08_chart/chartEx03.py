import matplotlib.pyplot as plt
from matplotlib import font_manager

plt.rcParams['font.family'] = 'Malgun Gothic'
# plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 15


names = ["Python", "Java", "Spring", "Flask"] # x축의 값
score = [155, 301, 125, 98] # y축의 값

plt.plot(names, score, color="tomato")

# 한글 깨짐 처리

# # 한글 폰트 설정
# font_path = "C:/Windows/Fonts/malgun.ttf"  # 사용하려는 한글 폰트 경로
# font_name = font_manager.FontProperties(fname=font_path).get_name()
# plt.rc('font', family=font_name)


plt.bar(names, score, color="tomato")
plt.title("2022년도 개발언어 순서")
plt.xlabel("Language")
plt.ylabel("Preference")
plt.show()
