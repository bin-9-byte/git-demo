# print("hello,world")
n = 100

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为： %d" % (n, sum))

# 无限循环
# var = 1
# while var == 1:
#     num = int(input("输入一个数字："))
#     print("你输入的数字是：", num)

count = 0
while count < 5:
    print(count, "小于5")
    count += 1
else:
    print(count, "大于或等于5")
