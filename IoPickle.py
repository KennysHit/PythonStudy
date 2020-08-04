import pickle
if __name__ == '__main__':
    dct = {
        "stu1": "小明",
        "stu2": "小红",
        "stu3": "小刚"
    }
    f = open("IoPickle.txt", "wb")
    pickle.dump(dct, f)
    f.close()

    f = open("IoPickle.txt", "rb")
    dct = dict(pickle.load(f))
    print(f"{dct.get('stu3')}和{dct.get('stu2')}是一对小情人")
