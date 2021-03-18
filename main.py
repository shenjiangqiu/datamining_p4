fruit = ["apple", "banana", "orange"]
price = ["1", "2.5", "3"]
# zip 把两个list糅合在一起 并列输出
for f, p in zip(fruit, price):
    print("{}'s price is {}".format(f, p))
# enumerate 便利list的同时输出序号
for i, f in enumerate(fruit):
    print("No.{},name: {}".format(i, f))
# [ exp1 for exp2 in exp3] :从迭代器中构造数组，exp1是狗造规则，exp2 in exp3是前面的迭代声明
fruit_with_price = ["{}:{}".format(f, p) for f, p in zip(fruit, price)]
print(fruit_with_price)
