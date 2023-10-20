array_2D = [[1, 2, 3], [4, 5, 6], [7, 20, 9]]

number_count = 0
addition = 0
all_numbers = []
final_numbers = []

for row in array_2D:
    for colum in row:
        number_count+=1
        addition+= colum
        all_numbers.append(colum)

average = addition/number_count

for number in all_numbers:
    if abs(number-average) <= 3:
        final_numbers.append(number)
        
print(final_numbers)
print(average)
cords = ""
print(len(final_numbers))
while 0 < len(final_numbers):
    for row_cords in enumerate(array_2D):
        #print(row_cords)
        # FIXME stuckne se v nekonečneém loopu po proběhnutí jednoho loopu
        for colum_cords, colum in enumerate(row):
            if colum in final_numbers:
                final_numbers.remove(colum)
                print(colum)
                print(final_numbers)
                cords += f"Číslo: {colum}, Souřadnice řádku {row_cords}, Souřadnice sloupce: {colum_cords}\n"
print(cords)