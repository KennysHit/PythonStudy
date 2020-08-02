if __name__ == '__main__':
    stu = dict(((1, "小红"), (2, "小张"), (3, "小明")))
    scl = {
        "a": "国防科技大学",
        "b": "复旦大学",
        "c": "电子科技大学"
    }

    print(f"{stu[1]}就读于{scl['a']}\n{stu[2]}就读于{scl['b']}\n{stu[3]}就读于{scl['c']}")

    scl = scl.fromkeys(('a', 'b'), "人民大学")
    print(scl)
    for eachKeys in stu.keys():
        print(stu.get(eachKeys, "木有"))
