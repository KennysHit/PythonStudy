if __name__ == '__main__':
    fileReader = open("Io.txt")
    str1 = fileReader.read()
    str1 = "A" + str1
    fileReader.close()

    fileWriter = open("Io.txt", "wt")
    fileWriter.write(str1)
    fileWriter.close()

    fileReader = open("Io.txt")
    print(fileReader.read())
