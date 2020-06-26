seireki = int(input("西暦＞ "))

if seireki >= 1896 and seireki % 4 == 0:
    print("開催年です")
else:
    print("開催年ではありません")
