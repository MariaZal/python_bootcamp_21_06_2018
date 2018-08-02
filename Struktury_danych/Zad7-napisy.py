# Zadanie 7
# Napisz program zliczający liczbę wystąpień samogłosek (a, e, i, o, u, y)
# w podanym przez użytkownika napisie
#
#
#
# x = [[1,2,3],[4,5,6]]
# print(x)
# a = [1,2,4]
# b = [4,4,1]
# x = [a,b]
#
# print(x)
#
# print(x[1][2])
#
# assert len(x) == 2
#
# napis = "ala ma kota"
#
# print (dir(napis))
#
# print(napis.center(80), "| center")
# print(napis.capitalize())

#
napis = input("podaj zdanie: ")
i = 0
SAMOGLOSKI = "aeiouy"

ile_samoglosek=0

for l in napis:
    if l in SAMOGLOSKI:
        ile_samoglosek += 1

# for l in napis:
#     if l == "a" or l == "e" or l == "i" or l == "o" or l == "u" or l == "y":
#         i += 1

print(ile_samoglosek)
# print(i)

print(f'''w napisie występuje {ile_samoglosek} samogłosek
a występuje {napis.count("a")} razy
e występuje {napis.count("e")} razy
i występuje {napis.count("i")} razy
o występuje {napis.count("o")} razy
u występuje {napis.count("u")} razy
y występuje {napis.count("y")} razy''')
