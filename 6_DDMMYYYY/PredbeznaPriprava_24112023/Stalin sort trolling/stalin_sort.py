

def stalin_sort(array):
    if len(array) < 2:
        return array
    result = []
    #storedElement = min(array)
    storedElement = array[0]
    for item in array:
        if storedElement <= item:
            result.append(item)
            storedElement = item
    return result            

print(stalin_sort([2, 1, 5, 4, 8, 10,2]))

# [2, 1, 5, 4, 8, 10,2]

'''
1) Zkontroluje, že list obsahuje minimálně dva itemy
2) Nastaví uložený item result listu
    2.1) první ve vstupu
    2.2) nejmenší hodnotu ve vstupu
3) Pro každý item
    3.1) Porovná s uloženým itemem
        3.1.1) Pokud je větší nebo roven uloženému itemu
            3.1.1.1) Přidá item do resultu
            3.1.1.2) Nastaví item, jako uložený item
        3.1.2) Pokud je menší, tak jej ignoruje
'''