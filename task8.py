slovo = input("введите слово: ")
key = len(slovo)
# print(key)
if 2 < key:
    print(slovo[:2], slovo[-2::])
elif 2 == key:
    print(slovo * 2)
else:
    print('Error')