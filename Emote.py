if __name__ == '__main__':
    def emote_transform(message):
        emote = {
            "yes": "😀",
            "no": "😕"
        }
        words = message.split(" ")
        str1 = ""
        for word in words:
            str1 += emote.get(word, word) + " "
        return str1


    print(emote_transform(input("\nAre you happy？（yes or no）>")))
