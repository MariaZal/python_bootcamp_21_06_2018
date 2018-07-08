# x = [[1,2,3],[4,5,6]]
# print(x)
# a = [1,2,3]
# b = [4,5,6]
# x = [a,b]
#
# print(x)
#
# print(x[0][2])
#
# assert len(x) == 2
#
# napis = "Ala ma kota"
#
# print (dir(napis))
#
# print(napis.center(80), "| center")
# print(napis.capitalize(1))

#
# napis = input("podaj zdanie: ")
# i = 0
# SAMOGLOSKI = "aeiouy"
#
# ile_samoglosek=0
#
# for l in napis:
#     if l in SAMOGLOSKI:
#         ile_samoglosek += 1
#
# for l in napis:
#     if l == "a" or l == "e" or l == "i" or l == "o" or l == "u" or l == "y":
#         i += 1
#
# print(ile_samoglosek)
#
# print(f'''w napisie występuje {i} samogłosek
# a występuje {napis.count("a")} razy
# e występuje {napis.count("e")} razy
# i występuje {napis.count("i")} razy
# o występuje {napis.count("o")} razy
# u występuje {napis.count("u")} razy
# y występuje {napis.count("y")} razy''')
#

napis = "ohgfds<kiuy>fjhgh<hjffj>"#input("Wpisz napis: ")
print(napis.index(">") - napis.index("<") - 1)

znak = 0

for i in napis:
    if i == "<":
        for i in range(napis.index(">") - napis.index("<") - 1):
            znak += 1
        print(znak)
    continue
