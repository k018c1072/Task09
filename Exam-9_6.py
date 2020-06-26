words = []
while True:
    word = input('単語＞ ')
    if word in words:
        break
    words.append(word)

print('終了')
print(words)
