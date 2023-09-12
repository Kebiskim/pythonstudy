# 1~10까지의 합, 홀수의 합
sum2 = 0;

for i in range(1, 11):
    sum2 += i

# <built-in function sum>
print(sum)

sum2 = 0;

for i in range(1, 11):
    if i % 2 == 1:
        sum2 = sum2 + i

print(sum2);

print(sum(range(1, 11)))