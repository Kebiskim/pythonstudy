import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_xlim([0.,10.])   # x축에 대해서 0부터 10까지 값을 지정
ax.set_ylim([0,2.5])   # y축에 대해서 지정
ax.set_xlabel('x-axis', size=10)
ax.set_title("차트 연습", size=15)

plt.show()