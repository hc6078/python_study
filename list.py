
if __name__ == '__main__':
    list = []
    list.append(11)
    list.append("234")
    list.append(12.34)
    print(len(list))  # len = 3
    print(list[1])  # 下标索引元素
    list[2] = 10000  # 通过下标修改元素的值
    for lr in list:
        print(lr)

    list_2 = [1, 2, 3, 4]
    list_2.append(11)  # 追加元素
    list_2.remove(3)  # 移除元素
    list_2.clear()  # 清空元素
    print(list_2)  # []

    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # 列表切片
    fruits2 = fruits[1:4]  # 跟golang一样，前闭后开 ,取不到4下标
    print(fruits2)  # apple strawberry waxberry
    fruits3 = sorted(fruits2)  # 列表排序

    # 列表推导式添加元素
    lst = [i for i in range(1, 11)]
    print(lst) # 输出结果为： [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    


