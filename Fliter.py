if __name__ == '__main__':

    def fun(x):
        def fun2():
            if x > 5:
                return 1
            else:
                return 0
        return fun2()
    
    fil = filter(fun, (1, 9, 2, 7, 10, 23))
    print(list(fil))

    print(list(filter(lambda x: x % 2, range(10))))
