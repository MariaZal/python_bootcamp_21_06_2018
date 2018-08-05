# jeśli chcemy pracować w konsoli

# # python zad3-clean_file.py emails.txt cleaned_emails.txt
# # sys.argv - tablica która zwraca nam zadeklarowane pliki
# # sys.argv[0] - Zad3-clean_file.py
# # sys.argv[1] - emails.txt
# # sys.argv[2] - cleaned_emails.txt
# #
# # import sys
# # plik_we = sys.argv[1]
# # plik_wy = sys.argv[2]
# #
corrected_emails = set()
with open("emails.txt", encoding='utf8') as f:
    for line in f:
        line = str(line).lower().strip()
        print(line)
        x = line.count('@')

        if x == 1:
            corrected_emails.add(line)
            # clean.write(line)
            # clean.write('\n')

with open("cleaned_emails.txt", 'w') as f:
    output = "\n".join(sorted(corrected_emails))
    f.write(output)


# #SORTOWANIE
# lista = [[1, 'c'], [3, 'a'], [2, 'b']]
# # 1 sortuj po 1 elemencie
# print(sorted(lista))
# #
# # sortuj po 2 elemencie
# def my_key(x):
#     return x[1]
# print(sorted(lista, key=my_key))
#
# # sortuj po 2 elemencie - II sposob
# print(sorted(lista, key=lambda x: x[1]))
#
# #sorted zmienia naszą liste z kolei sorted generuje nową, posotrowaną wersję pierwotnej listy
