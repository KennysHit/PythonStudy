if __name__ == '__main__':
    def recursion(n, a, b, c):
        def move(x, y):
            print(x + "-->" + y)

        if n == 1:
            move(a, c)
        else:
            recursion(n - 1, a, c, b)  # 将a上的n-1个盘子借助c移动到b上
            move(a, c)  # 将a上的第n个盘子移动到c上
            recursion(n - 1, b, a, c)  # 将b上的n-1个盘子借助a移动到c上


    n = int(input("请输入汉诺塔的层数>"))
    print("移动步骤为：", end="\n")
    recursion(n, "a", "b", "c")
