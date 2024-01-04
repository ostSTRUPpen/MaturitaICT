from random import randint

# https://realpython.com/sorting-algorithms-python/#implementing-quicksort-in-python
def quicksort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)

print(quicksort([1, 5, 4, 8, 10,2]))

'''
1) Vrátí pokud je délka listu menší než 2
2) Vybere náhodný item v listu a určí ho jako dělící bod
3) Porovnává jednotlivé items listu s pivotem (porovná každý item)
    3.1) Pokud je menší, tak jej přidá do listu low
    3.2) Pokud je stejný, tak jej přidá do listu same
    3.3) Pokud je větší, tak jej přidá do listu high
4) Zavolá sebe sama na list "low" připojí k výsledku list "same" a připojí výsledek zavolání sebe sama na list "high"
'''