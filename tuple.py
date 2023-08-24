# 元组不可修改
if __name__ == '__main__':
    tuple = (11, "22", 33.33)
    for t in tuple:
        print(t)

    for t in range(len(tuple)):
        print(tuple[t])
