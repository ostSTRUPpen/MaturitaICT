# https://realpython.com/sorting-algorithms-python/#implementing-merge-sort-in-python
def merge(left, right):
    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right

    # If the second array is empty, then nothing needs
    # to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Now go through both arrays until all the elements
    # make it into the resultant array
    while len(result) < len(left) + len(right):
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def merge_sort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))

'''
1) Zkontroluje délku listu
2) Rozdělí list na dva v půlce
    2.1) Znovu volá sebe sama na levou a pravou část listu
    2.2) Kroky 1 a 2 se opakují dokud není délka listu menší než 2
3) Nakonec zavolá merge()

4) Pokud je délka jednoho z listů rovná 0, tak vrátí ten druhý
5) Opakuje se dokud není součet délek rozdělených listů roven výsledku
    4.1) Pokud dojde index pointer na konec listu, tak se k výsledku přidá druhý list a ukončí se opakování
6) Pokud je element vlevo menší než vpravo, tak je vložen do výsledku a index levého listu se zvětší o jedna
7) Pokud je element vpravo menší než vlevo, tak je vložen do výsledku a index pravého listu se zvětší o jedna


'''

print(merge_sort([1, 5, 4, 8, 10,2]))