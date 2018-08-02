# Zadanie 8
# Napisz program zliczający liczbę znaków w podanym przez użytkownika napisie
# pomiędzy nawiasami<>. Nawiasy mogą wystąpić tylko raz



napis=input("Wpisz napis:")

print(napis.index(">")-napis.index("<")-1)





# napis = "ohgfds<kiuy>fjhgh<hjffj>"#input("Wpisz napis: ")
# print(napis.index(">") - napis.index("<") - 1)
#


for i in napis:
    znak = 0
    if i == "<":
        for i in napis:
            if i!=">":
                znak+=1
            else:
                print(znak)
                break
        # for i in range(napis.index(">") - napis.index("<") - 1):
        #     znak += 1

