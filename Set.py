if __name__ == '__main__':
    num1 = [1, 2, 3, 4, 5, 5, 1, 2, 3, 2, 0]
    temp = []
    for each in num1:
        if each not in temp:
            temp.append(each)
    print(temp)
    num1 = list(set(num1))
    print(num1)

    set1 = {1, 2, 3, 4, 5, 5, 5, 2, 3}
    print(set1)
    set1.remove(5)
    print(set1)
    set1.add(0)
    print(set1)

    set2 = frozenset(num1)  # 不可改变的集合
