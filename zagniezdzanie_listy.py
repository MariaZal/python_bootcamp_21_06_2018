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


napis = input("podaj zdanie: ")
i = 0
samogloski = "aeiouy"

ile_samoglosek=0

for l in napis:
    if l in samogloski:
        ile_samoglosek += 1

for l in napis:
    if l == "a" or l == "e" or l == "i" or l == "o" or l == "u" or l == "y":
        i += 1

print(ile_samoglosek)

print(f'w napisie występuje {i} samogłosek ')

print(f'a występuje {napis.count("a")} razy')

print(f'e występuje {napis.count("e")} razy')

print(f'i występuje {napis.count("i")} razy')

print(f'o występuje {napis.count("o")} razy')

print(f'u występuje {napis.count("u")} razy')

print(f'y występuje {napis.count("y")} razy')


